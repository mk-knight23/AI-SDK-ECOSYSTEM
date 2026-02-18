import { json } from '@sveltejs/kit';
import { explainCode } from '$lib/openai';

export async function POST({ request }) {
    const { code, language } = await request.json();
    try {
        const result = await explainCode(code, language);
        return json({ explanation: result });
    } catch (error) {
        return json({ error: 'Explanation failed' }, { status: 500 });
    }
}
