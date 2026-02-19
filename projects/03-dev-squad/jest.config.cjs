// Jest configuration for JavaScript/TypeScript projects
/** @type {import('jest').Config} */
module.exports = {
  preset: 'ts-jest/presets/js-with-ts',
  testEnvironment: 'node',
  coverageDirectory: './coverage',
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  collectCoverageFrom: [
    'src/**/*.{ts,js}',
    '!src/**/*.d.ts',
    '!src/**/__tests__/**',
    '!src/**/node_modules/**',
    '!src/__mocks__/**'
  ],
  testMatch: [
    '**/__tests__/**/*.test.ts',
    '**/?(*.)+(spec|test).ts',
    '**/*.test.js'
  ],
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json'],
  transform: {
    '^.+\\.tsx?$': ['ts-jest', {
      useESM: false,
      tsconfig: {
        allowJs: true,
        esModuleInterop: true,
        module: 'commonjs',
        target: 'es2020'
      }
    }]
  },
  moduleNameMapper: {
    // Handle SvelteKit path aliases
    '^\\$lib/(.*)$': '<rootDir>/src/lib/$1',
    '^\\$env/static/private$': '<rootDir>/src/__mocks__/env/static/private.ts',
    '^\\$env/static/public$': '<rootDir>/src/__mocks__/env/static/public.ts',
    '^@sveltejs/kit$': '<rootDir>/src/__mocks__/sveltejs-kit.ts'
  },
  testTimeout: 30000,
  verbose: true,
  extensionsToTreatAsEsm: []
};
