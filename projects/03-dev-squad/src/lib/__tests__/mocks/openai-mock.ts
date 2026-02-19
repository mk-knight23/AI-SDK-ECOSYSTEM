// OpenAI mock utility for testing
export class MockOpenAI {
  private responses: Map<string, any> = new Map();

  setResponse(promptPattern: string, response: any) {
    this.responses.set(promptPattern, response);
  }

  chat = {
    completions: {
      create: async (params: any) => {
        const prompt = params.messages?.[params.messages.length - 1]?.content;

        // Find matching response by pattern
        for (const [pattern, response] of this.responses.entries()) {
          if (prompt?.includes(pattern)) {
            return response;
          }
        }

        // Default response
        return {
          choices: [{ message: { content: 'Mock response' } }],
          usage: { total_tokens: 10 }
        };
      }
    }
  };
}

export const mockOpenAI = new MockOpenAI();
