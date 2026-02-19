import { test, expect } from '@playwright/test';

test.describe('VentureGraph E2E', () => {
  test('user can create venture plan', async ({ page }) => {
    await page.goto('http://localhost:8000');
    await page.fill('[data-testid="venture-idea"]', 'AI-powered fitness app');
    await page.click('[data-testid="submit-btn"]');
    await page.waitForSelector('[data-testid="market-analysis"]', { timeout: 30000 });
    await expect(page.locator('[data-testid="market-analysis"]')).toBeVisible();
    await expect(page.locator('[data-testid="business-model"]')).toBeVisible();
    await expect(page.locator('[data-testid="pitch-deck"]')).toBeVisible();
  });
});
