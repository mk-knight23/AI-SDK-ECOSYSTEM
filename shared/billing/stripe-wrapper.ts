import Stripe from 'stripe';

export class StripeBilling {
  private stripe: Stripe;

  constructor(apiKey: string) {
    this.stripe = new Stripe(apiKey);
  }

  async createCustomer(email: string, name: string) {
    return await this.stripe.customers.create({
      email,
      name,
      metadata: { source: 'ai-sdk-saas' }
    });
  }

  async createSubscription(customerId: string, priceId: string) {
    return await this.stripe.subscriptions.create({
      customer: customerId,
      items: [{ price: priceId }],
      payment_behavior: 'default_incomplete',
    });
  }

  async createUsageRecord(subscriptionId: string, units: number) {
    return await this.stripe.subscriptionItems.createUsageRecord(
      subscriptionId,
      { quantity: units, action: 'increment' }
    );
  }

  async cancelSubscription(subscriptionId: string) {
    return await this.stripe.subscriptions.cancel(subscriptionId);
  }
}
