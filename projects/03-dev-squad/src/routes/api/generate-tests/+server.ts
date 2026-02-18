import { json } from '@sveltejs/kit';
import { generateTests } from '$lib/openai';

export async function POST({ request }) {
    const { code, language } = await request.json();
    try {
        const result = await generateTests(code, language);
        return json({ tests: result });
    } catch (error) {
        return json({ error: 'Test generation failed' }, { status: 500 });
    }
}
