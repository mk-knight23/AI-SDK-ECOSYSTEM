import { Resend } from 'resend';

export class EmailClient {
  private resend: Resend;

  constructor(apiKey: string) {
    this.resend = new Resend(apiKey);
  }

  async sendEmail(to: string, subject: string, html: string) {
    await this.resend.emails.send({
      from: 'noreply@ai-sdk-saas.com',
      to,
      subject,
      html,
    });
  }

  async sendWelcomeEmail(to: string, name: string) {
    await this.sendEmail(
      to,
      'Welcome to AI SDK SaaS!',
      `<h1>Welcome ${name}!</h1><p>Your account is ready.</p>`
    );
  }

  async sendResetLink(to: string, resetLink: string) {
    await this.sendEmail(
      to,
      'Reset your password',
      `<p>Click <a href="${resetLink}">here</a> to reset.</p>`
    );
  }
}
