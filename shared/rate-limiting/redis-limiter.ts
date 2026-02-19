import { Redis } from 'ioredis';

export class RateLimiter {
  private redis: Redis;
  private windowMs: number;
  private maxRequests: number;

  constructor(redisUrl: string, windowMs: number, maxRequests: number) {
    this.redis = new Redis(redisUrl);
    this.windowMs = windowMs;
    this.maxRequests = maxRequests;
  }

  async checkLimit(userId: string): Promise<boolean> {
    const key = `ratelimit:${userId}`;
    const current = await this.redis.incr(key);

    if (current === 1) {
      await this.redis.expire(key, this.windowMs / 1000);
    }

    return current <= this.maxRequests;
  }

  async resetLimit(userId: string): Promise<void> {
    const key = `ratelimit:${userId}`;
    await this.redis.del(key);
  }
}
