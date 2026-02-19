export class UsageTracker {
  private usage: Map<string, number> = new Map();

  recordUsage(userId: string, units: number = 1) {
    const current = this.usage.get(userId) || 0;
    this.usage.set(userId, current + units);
  }

  getUsage(userId: string): number {
    return this.usage.get(userId) || 0;
  }

  resetUsage(userId: string) {
    this.usage.set(userId, 0);
  }
}
