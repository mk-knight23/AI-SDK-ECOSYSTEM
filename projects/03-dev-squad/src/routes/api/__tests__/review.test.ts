// Mock the openai module before importing the route
jest.mock('$lib/openai', () => ({
  reviewCode: jest.fn()
}));

// Mock SvelteKit's json helper
jest.mock('@sveltejs/kit', () => ({
  json: (data: any, init?: ResponseInit) => {
    const response = new Response(JSON.stringify(data), {
      ...init,
      headers: { 'Content-Type': 'application/json', ...init?.headers }
    });
    // Add json() method for convenience
    Object.defineProperty(response, 'json', {
      value: async () => data,
      writable: false
    });
    return response;
  }
}));

import { reviewCode } from '$lib/openai';
import { POST } from '../review/+server';

describe('POST /api/review', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should return review result on successful request', async () => {
    const mockResult = {
      score: 8,
      issues: ['Issue 1'],
      suggestions: ['Suggestion 1'],
      improved_code: 'const x = 1;'
    };

    (reviewCode as jest.Mock).mockResolvedValue(mockResult);

    const request = new Request('http://localhost/api/review', {
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
    expect(data).toEqual(mockResult);
    expect(reviewCode).toHaveBeenCalledWith('const x = 1;', 'javascript');
  });

  it('should handle different programming languages', async () => {
    (reviewCode as jest.Mock).mockResolvedValue({ score: 9, issues: [], suggestions: [], improved_code: '' });

    const languages = ['python', 'typescript', 'rust', 'go'];

    for (const language of languages) {
      const request = new Request('http://localhost/api/review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: 'test code', language })
      });

      await POST({ request });
      expect(reviewCode).toHaveBeenCalledWith('test code', language);
    }
  });

  it('should return 500 error when reviewCode fails', async () => {
    (reviewCode as jest.Mock).mockRejectedValue(new Error('API error'));

    const request = new Request('http://localhost/api/review', {
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
    expect(data).toEqual({ error: 'Review failed' });
  });

  it('should handle complex code input', async () => {
    const complexCode = `
      function fibonacci(n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
      }
    `;

    (reviewCode as jest.Mock).mockResolvedValue({
      score: 7,
      issues: ['Inefficient algorithm'],
      suggestions: ['Use memoization'],
      improved_code: 'memoized version'
    });

    const request = new Request('http://localhost/api/review', {
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
    expect(data.score).toBe(7);
    expect(reviewCode).toHaveBeenCalledWith(complexCode, 'javascript');
  });

  it('should handle empty code input', async () => {
    (reviewCode as jest.Mock).mockResolvedValue({
      score: 0,
      issues: ['No code provided'],
      suggestions: ['Provide code to review'],
      improved_code: ''
    });

    const request = new Request('http://localhost/api/review', {
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
    expect(data.score).toBe(0);
  });

  it('should handle API errors gracefully', async () => {
    (reviewCode as jest.Mock).mockRejectedValue(new Error('Rate limit exceeded'));

    const request = new Request('http://localhost/api/review', {
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
    expect(data.error).toBe('Review failed');
  });

  it('should handle network errors', async () => {
    (reviewCode as jest.Mock).mockRejectedValue(new Error('Network error'));

    const request = new Request('http://localhost/api/review', {
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
    expect(data.error).toBe('Review failed');
  });
});
