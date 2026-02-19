// Mock the openai module before importing the route
jest.mock('$lib/openai', () => ({
  generateTests: jest.fn()
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

import { generateTests } from '$lib/openai';
import { POST } from '../generate-tests/+server';

describe('POST /api/generate-tests', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should return generated tests on successful request', async () => {
    const mockTests = `
describe('add', () => {
  it('should add two numbers', () => {
    expect(add(1, 2)).toBe(3);
  });
});
    `.trim();

    (generateTests as jest.Mock).mockResolvedValue(mockTests);

    const request = new Request('http://localhost/api/generate-tests', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        code: 'function add(a, b) { return a + b; }',
        language: 'javascript'
      })
    });

    const response = await POST({ request });
    const data = await response.json();

    expect(response.status).toBe(200);
    expect(data).toEqual({ tests: mockTests });
    expect(generateTests).toHaveBeenCalledWith('function add(a, b) { return a + b; }', 'javascript');
  });

  it('should handle different programming languages', async () => {
    (generateTests as jest.Mock).mockResolvedValue('def test(): pass');

    const languages = ['python', 'typescript', 'rust', 'go', 'java'];

    for (const language of languages) {
      const request = new Request('http://localhost/api/generate-tests', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: 'test code', language })
      });

      await POST({ request });
      expect(generateTests).toHaveBeenCalledWith('test code', language);
    }
  });

  it('should return 500 error when generateTests fails', async () => {
    (generateTests as jest.Mock).mockRejectedValue(new Error('API error'));

    const request = new Request('http://localhost/api/generate-tests', {
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
    expect(data).toEqual({ error: 'Test generation failed' });
  });

  it('should handle complex code input', async () => {
    const complexCode = `
      class Calculator {
        add(a, b) { return a + b; }
        subtract(a, b) { return a - b; }
      }
    `;

    const mockTests = `
describe('Calculator', () => {
  let calc;
  beforeEach(() => {
    calc = new Calculator();
  });
  it('should add', () => {
    expect(calc.add(1, 2)).toBe(3);
  });
});
    `.trim();

    (generateTests as jest.Mock).mockResolvedValue(mockTests);

    const request = new Request('http://localhost/api/generate-tests', {
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
    expect(data.tests).toBe(mockTests);
  });

  it('should handle empty code input', async () => {
    (generateTests as jest.Mock).mockResolvedValue('// No tests generated - no code provided');

    const request = new Request('http://localhost/api/generate-tests', {
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
    expect(data.tests).toBe('// No tests generated - no code provided');
  });

  it('should handle API rate limit errors', async () => {
    (generateTests as jest.Mock).mockRejectedValue(new Error('Rate limit exceeded'));

    const request = new Request('http://localhost/api/generate-tests', {
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
    expect(data.error).toBe('Test generation failed');
  });

  it('should handle network errors', async () => {
    (generateTests as jest.Mock).mockRejectedValue(new Error('Network error'));

    const request = new Request('http://localhost/api/generate-tests', {
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
    expect(data.error).toBe('Test generation failed');
  });
});
