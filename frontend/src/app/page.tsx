import CompanyForm from "@/components/CompanyForm";

export default function Home() {
  return (
    <main className="min-h-screen p-10">
      <h1 className="text-4xl font-bold">
        AI Investment Research Agent
      </h1>

      <CompanyForm />
    </main>
  );
}