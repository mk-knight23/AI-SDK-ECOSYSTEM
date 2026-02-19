// Mock for @sveltejs/kit module
export function json(data: any, init?: ResponseInit): Response {
  return new Response(JSON.stringify(data), {
    ...init,
    headers: { 'Content-Type': 'application/json', ...init?.headers }
  });
}

export function error(status: number, message?: string): Error {
  return new Error(message || `Error ${status}`);
}

export function redirect(status: number, location: string): never {
  throw new Error(`Redirect ${status} to ${location}`);
}
