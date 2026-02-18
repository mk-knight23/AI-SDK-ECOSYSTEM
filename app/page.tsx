import { Sparkles } from "lucide-react";
import Chat from "./components/Chat";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-br from-zinc-900 via-zinc-800 to-zinc-900 px-4 py-12 text-white">
      <main className="flex w-full max-w-4xl flex-col items-center gap-8">
        {/* Header */}
        <div className="flex flex-col items-center gap-4 text-center">
          <div className="flex items-center gap-3 rounded-full bg-zinc-800/50 px-4 py-2 backdrop-blur-sm">
            <Sparkles className="h-5 w-5 text-amber-400" />
            <span className="text-sm font-medium text-zinc-300">
              Powered by Vercel AI SDK
            </span>
          </div>

          <h1 className="text-4xl font-bold tracking-tight sm:text-5xl lg:text-6xl">
            InsightStream
          </h1>

          <p className="max-w-lg text-lg text-zinc-400">
            AI-powered insights platform with real-time streaming responses
          </p>
        </div>

        {/* Chat Component */}
        <Chat />

        {/* Features Grid */}
        <div className="mt-8 grid w-full grid-cols-1 gap-4 sm:grid-cols-3">
          <div className="rounded-xl bg-zinc-800/50 p-6 backdrop-blur-sm">
            <h3 className="font-semibold text-amber-400">Streaming</h3>
            <p className="mt-2 text-sm text-zinc-400">
              Real-time AI response streaming
            </p>
          </div>
          <div className="rounded-xl bg-zinc-800/50 p-6 backdrop-blur-sm">
            <h3 className="font-semibold text-amber-400">GPT-4o-mini</h3>
            <p className="mt-2 text-sm text-zinc-400">
              Fast and efficient AI model
            </p>
          </div>
          <div className="rounded-xl bg-zinc-800/50 p-6 backdrop-blur-sm">
            <h3 className="font-semibold text-amber-400">TypeScript</h3>
            <p className="mt-2 text-sm text-zinc-400">Type-safe development</p>
          </div>
        </div>

        {/* Links */}
        <div className="flex flex-col gap-4 sm:flex-row">
          <a
            href="/api/health"
            className="rounded-lg bg-white px-6 py-3 text-center font-medium text-zinc-900 transition-colors hover:bg-zinc-200"
          >
            Check Health API
          </a>
          <a
            href="https://sdk.vercel.ai/docs"
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-lg border border-zinc-700 bg-transparent px-6 py-3 text-center font-medium text-white transition-colors hover:bg-zinc-800"
          >
            AI SDK Docs
          </a>
        </div>
      </main>

      <footer className="mt-12 text-sm text-zinc-500">
        InsightStream - Built with Next.js 15 + Vercel AI SDK
      </footer>
    </div>
  );
}
