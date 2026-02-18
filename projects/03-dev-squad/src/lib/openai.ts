import OpenAI from 'openai';
import { OPENAI_API_KEY } from '$env/static/private';

export const openai = new OpenAI({ apiKey: OPENAI_API_KEY });

export interface CodeReviewResult {
    score: number;
    issues: string[];
    suggestions: string[];
    improved_code: string;
}

export async function reviewCode(code: string, language: string): Promise<CodeReviewResult> {
    const prompt = `Review this ${language} code and provide structured feedback:\n\`\`\`${language}\n${code}\n\`\`\`\nProvide output as JSON with: score (1-10), issues (array), suggestions (array), improved_code (string)`;
    const response = await openai.chat.completions.create({
        model: 'gpt-4o-mini',
        messages: [
            { role: 'system', content: 'You are a senior software engineer doing code reviews.' },
            { role: 'user', content: prompt }
        ],
        response_format: { type: 'json_object' }
    });
    return JSON.parse(response.choices[0].message.content || '{}');
}

export async function generateTests(code: string, language: string): Promise<string> {
    const prompt = `Generate comprehensive unit tests for this ${language} code:\n\`\`\`${language}\n${code}\n\`\`\`\nProvide only the test code.`;
    const response = await openai.chat.completions.create({
        model: 'gpt-4o-mini',
        messages: [{ role: 'system', content: 'You are a test automation expert.' }, { role: 'user', content: prompt }]
    });
    return response.choices[0].message.content || '';
}

export async function explainCode(code: string, language: string): Promise<string> {
    const prompt = `Explain this ${language} code in simple terms:\n\`\`\`${language}\n${code}\n\`\`\``;
    const response = await openai.chat.completions.create({
        model: 'gpt-4o-mini',
        messages: [{ role: 'system', content: 'You are a helpful coding tutor.' }, { role: 'user', content: prompt }]
    });
    return response.choices[0].message.content || '';
}
