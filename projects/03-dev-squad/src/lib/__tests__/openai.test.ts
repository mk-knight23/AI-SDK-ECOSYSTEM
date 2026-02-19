// Mock the environment variables before importing openai
jest.mock('$env/static/private', () => ({
  OPENAI_API_KEY: 'test-api-key'
}));

// Create mock function
const mockCreate = jest.fn();

// Mock OpenAI class
jest.mock('openai', () => {
  return jest.fn().mockImplementation(() => ({
    chat: {
      completions: {
        create: mockCreate
      }
    }
  }));
});

import { reviewCode, generateTests, explainCode, CodeReviewResult } from '../openai';

describe('OpenAI Service', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('reviewCode', () => {
    it('should return code review result with parsed JSON', async () => {
      const mockResult: CodeReviewResult = {
        score: 8,
        issues: ['Issue 1', 'Issue 2'],
        suggestions: ['Suggestion 1'],
        improved_code: 'const x = 1;'
      };

      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: JSON.stringify(mockResult)
          }
        }]
      });

      const result = await reviewCode('const x = 1;', 'javascript');

      expect(result).toEqual(mockResult);
      expect(mockCreate).toHaveBeenCalledWith({
        model: 'gpt-4o-mini',
        messages: [
          { role: 'system', content: 'You are a senior software engineer doing code reviews.' },
          {
            role: 'user',
            content: expect.stringContaining('Review this javascript code')
          }
        ],
        response_format: { type: 'json_object' }
      });
    });

    it('should handle empty response content', async () => {
      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: ''
          }
        }]
      });

      const result = await reviewCode('const x = 1;', 'javascript');

      expect(result).toEqual({});
    });

    it('should include code and language in the prompt', async () => {
      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: '{}'
          }
        }]
      });

      const code = 'function test() { return 42; }';
      const language = 'typescript';

      await reviewCode(code, language);

      const callArgs = mockCreate.mock.calls[0][0];
      const userMessage = callArgs.messages[1].content;

      expect(userMessage).toContain(code);
      expect(userMessage).toContain(language);
      expect(userMessage).toContain('```typescript');
    });

    it('should handle different programming languages', async () => {
      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: JSON.stringify({ score: 9, issues: [], suggestions: [], improved_code: '' })
          }
        }]
      });

      const languages = ['python', 'java', 'rust', 'go', 'ruby'];

      for (const language of languages) {
        await reviewCode('code', language);
        const callArgs = mockCreate.mock.calls[mockCreate.mock.calls.length - 1][0];
        expect(callArgs.messages[1].content).toContain(`Review this ${language} code`);
      }
    });
  });

  describe('generateTests', () => {
    it('should return generated tests as string', async () => {
      const mockTests = `
describe('test', () => {
  it('should work', () => {
    expect(true).toBe(true);
  });
});
      `.trim();

      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: mockTests
          }
        }]
      });

      const result = await generateTests('const x = 1;', 'javascript');

      expect(result).toBe(mockTests);
      expect(mockCreate).toHaveBeenCalledWith({
        model: 'gpt-4o-mini',
        messages: [
          { role: 'system', content: 'You are a test automation expert.' },
          {
            role: 'user',
            content: expect.stringContaining('Generate comprehensive unit tests')
          }
        ]
      });
    });

    it('should handle empty test generation response', async () => {
      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: ''
          }
        }]
      });

      const result = await generateTests('const x = 1;', 'javascript');

      expect(result).toBe('');
    });

    it('should include code in the prompt', async () => {
      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: ''
          }
        }]
      });

      const code = 'function add(a, b) { return a + b; }';

      await generateTests(code, 'javascript');

      const callArgs = mockCreate.mock.calls[0][0];
      expect(callArgs.messages[1].content).toContain(code);
    });

    it('should use correct system prompt for test generation', async () => {
      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: ''
          }
        }]
      });

      await generateTests('code', 'python');

      const callArgs = mockCreate.mock.calls[0][0];
      expect(callArgs.messages[0].content).toBe('You are a test automation expert.');
    });
  });

  describe('explainCode', () => {
    it('should return code explanation as string', async () => {
      const mockExplanation = 'This code declares a constant variable x with the value 1.';

      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: mockExplanation
          }
        }]
      });

      const result = await explainCode('const x = 1;', 'javascript');

      expect(result).toBe(mockExplanation);
      expect(mockCreate).toHaveBeenCalledWith({
        model: 'gpt-4o-mini',
        messages: [
          { role: 'system', content: 'You are a helpful coding tutor.' },
          {
            role: 'user',
            content: expect.stringContaining('Explain this javascript code')
          }
        ]
      });
    });

    it('should handle empty explanation response', async () => {
      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: ''
          }
        }]
      });

      const result = await explainCode('const x = 1;', 'javascript');

      expect(result).toBe('');
    });

    it('should include code and language in the prompt', async () => {
      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: ''
          }
        }]
      });

      const code = 'class User { constructor(name) { this.name = name; } }';
      const language = 'javascript';

      await explainCode(code, language);

      const callArgs = mockCreate.mock.calls[0][0];
      const userMessage = callArgs.messages[1].content;

      expect(userMessage).toContain(code);
      expect(userMessage).toContain(language);
    });

    it('should use correct system prompt for explanations', async () => {
      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: ''
          }
        }]
      });

      await explainCode('code', 'python');

      const callArgs = mockCreate.mock.calls[0][0];
      expect(callArgs.messages[0].content).toBe('You are a helpful coding tutor.');
    });

    it('should handle complex code explanations', async () => {
      const complexExplanation = `
This recursive function calculates the factorial of a number:
1. Base case: if n is 0 or 1, return 1
2. Recursive case: return n multiplied by factorial(n-1)
      `.trim();

      mockCreate.mockResolvedValue({
        choices: [{
          message: {
            content: complexExplanation
          }
        }]
      });

      const result = await explainCode('function factorial(n) { return n <= 1 ? 1 : n * factorial(n-1); }', 'javascript');

      expect(result).toBe(complexExplanation);
    });
  });

  describe('API error handling', () => {
    it('should propagate errors from reviewCode', async () => {
      mockCreate.mockRejectedValue(new Error('API rate limit exceeded'));

      await expect(reviewCode('code', 'javascript')).rejects.toThrow('API rate limit exceeded');
    });

    it('should propagate errors from generateTests', async () => {
      mockCreate.mockRejectedValue(new Error('Network error'));

      await expect(generateTests('code', 'javascript')).rejects.toThrow('Network error');
    });

    it('should propagate errors from explainCode', async () => {
      mockCreate.mockRejectedValue(new Error('Invalid API key'));

      await expect(explainCode('code', 'javascript')).rejects.toThrow('Invalid API key');
    });
  });

  describe('Model configuration', () => {
    it('should use gpt-4o-mini model for all functions', async () => {
      mockCreate.mockResolvedValue({
        choices: [{ message: { content: '{}' } }]
      });

      await reviewCode('code', 'javascript');
      expect(mockCreate.mock.calls[0][0].model).toBe('gpt-4o-mini');

      await generateTests('code', 'javascript');
      expect(mockCreate.mock.calls[1][0].model).toBe('gpt-4o-mini');

      await explainCode('code', 'javascript');
      expect(mockCreate.mock.calls[2][0].model).toBe('gpt-4o-mini');
    });
  });
});
