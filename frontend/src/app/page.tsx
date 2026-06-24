import CompanyForm from "@/components/CompanyForm";

export default function Home() {
  return (
    <main className="min-h-screen p-10">

      <h1 className="text-4xl font-bold">
        AI Investment Research Agent
      </h1>

      <p className="mt-2 text-gray-500">
        Powered by LangGraph, Groq, FastAPI and Next.js
      </p>

      <CompanyForm />

      <footer className="mt-16 border-t pt-6 text-center text-sm text-gray-500">
        <p>
          AI Investment Research Agent
        </p>

        <p className="mt-1">
          Built using Next.js, FastAPI, LangGraph, Groq and Yahoo Finance
        </p>

        <p className="mt-1">
          Developed by Yash Anand
        </p>
      </footer>

    </main>
  );
}