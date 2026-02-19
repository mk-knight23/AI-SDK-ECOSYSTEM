// Mock the openai module before importing the route
jest.mock('$lib/openai', () => ({
  explainCode: jest.fn()
}));

// Mock SvelteKit's json helper
jest.mock('@sveltejs/kit', () => ({
  json: (data: any, init?: ResponseInit) => {
    const response = new Response(JSON.stringify(data), {
      ...init,
      headers: { 'Content-Type': 'application/json', ...init?.headers }
    });
    Object.defineProperty(response, 'json', {
      value: async () => data,
      writable: false
    });
    return response;
  }
}));

import { explainCode } from '$lib/openai';
import { POST } from '../explain/+server';

describe('POST /api/explain', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should return explanation on successful request', async () => {
    const mockExplanation = 'This code declares a constant variable x with value 1.';

    (explainCode as jest.Mock).mockResolvedValue(mockExplanation);

    const request = new Request('http://localhost/api/explain', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        code: 'const x = 1;',
        language: 'javascript'
      })
    });

    const response = await POST({ request });
    const data = await response.json();

    expect(response.status).toBe(200);
    expect(data).toEqual({ explanation: mockExplanation });
    expect(explainCode).toHaveBeenCalledWith('const x = 1;', 'javascript');
  });

  it('should handle different programming languages', async () => {
    (explainCode as jest.Mock).mockResolvedValue('Explanation');

    const languages = ['python', 'typescript', 'rust', 'go', 'java'];

    for (const language of languages) {
      const request = new Request('http://localhost/api/explain', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: 'test code', language })
      });

      await POST({ request });
      expect(explainCode).toHaveBeenCalledWith('test code', language);
    }
  });

  it('should return 500 error when explainCode fails', async () => {
    (explainCode as jest.Mock).mockRejectedValue(new Error('API error'));

    const request = new Request('http://localhost/api/explain', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        code: 'const x = 1;',
        language: 'javascript'
      })
    });

    const response = await POST({ request });
    const data = await response.json();

    expect(response.status).toBe(500);
    expect(data).toEqual({ error: 'Explanation failed' });
  });

  it('should handle complex code input', async () => {
    const complexCode = `
      async function fetchData() {
        const response = await fetch('/api/data');
        return response.json();
      }
    `;

    (explainCode as jest.Mock).mockResolvedValue('This is an async function that fetches data from an API.');

    const request = new Request('http://localhost/api/explain', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        code: complexCode,
        language: 'javascript'
      })
    });

    const response = await POST({ request });
    const data = await response.json();

    expect(response.status).toBe(200);
    expect(data.explanation).toBe('This is an async function that fetches data from an API.');
  });

  it('should handle empty code input', async () => {
    (explainCode as jest.Mock).mockResolvedValue('No code provided to explain.');

    const request = new Request('http://localhost/api/explain', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        code: '',
        language: 'javascript'
      })
    });

    const response = await POST({ request });
    const data = await response.json();

    expect(response.status).toBe(200);
    expect(data.explanation).toBe('No code provided to explain.');
  });

  it('should handle API rate limit errors', async () => {
    (explainCode as jest.Mock).mockRejectedValue(new Error('Rate limit exceeded'));

    const request = new Request('http://localhost/api/explain', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        code: 'const x = 1;',
        language: 'javascript'
      })
    });

    const response = await POST({ request });
    const data = await response.json();

    expect(response.status).toBe(500);
    expect(data.error).toBe('Explanation failed');
  });

  it('should handle network errors', async () => {
    (explainCode as jest.Mock).mockRejectedValue(new Error('Network error'));

    const request = new Request('http://localhost/api/explain', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        code: 'const x = 1;',
        language: 'javascript'
      })
    });

    const response = await POST({ request });
    const data = await response.json();

    expect(response.status).toBe(500);
    expect(data.error).toBe('Explanation failed');
  });
});
