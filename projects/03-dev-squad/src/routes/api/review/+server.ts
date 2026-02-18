import { json } from '@sveltejs/kit';
import { reviewCode } from '$lib/openai';

export async function POST({ request }) {
    const { code, language } = await request.json();
    try {
        const result = await reviewCode(code, language);
        return json(result);
    } catch (error) {
        return json({ error: 'Review failed' }, { status: 500 });
    }
}
