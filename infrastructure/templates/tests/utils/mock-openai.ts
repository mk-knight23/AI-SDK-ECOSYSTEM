// OpenAI mock utility for testing
export class MockOpenAI {
  private responses: Map<string, any> = new Map();

  setResponse(prompt: string, response: any) {
    this.responses.set(prompt, response);
  }

  async createChatCompletion(params: any) {
    const prompt = params.messages?.[params.messages.length - 1]?.content;
    const response = this.responses.get(prompt) || {
      choices: [{ message: { content: 'Mock response' } }],
      usage: { total_tokens: 10 }
    };
    return response;
  }
}

export const mockOpenAI = new MockOpenAI();
