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

import { GET } from '../+server';

describe('GET /health', () => {
  it('should return health status', async () => {
    const response = await GET();
    const data = await response.json();

    expect(response.status).toBe(200);
    expect(data.status).toBe('healthy');
    expect(data.service).toBe('DevSquad');
    expect(data.timestamp).toBeDefined();
    expect(new Date(data.timestamp).toISOString()).toBe(data.timestamp);
  });
});
