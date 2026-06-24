"use client";

import { useState } from "react";
import AnalysisCard from "./AnalysisCard";
import LoadingSpinner from "./LoadingSpinner";

export default function CompanyForm() {
  const [company, setCompany] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function analyzeCompany() {
    if (!company.trim()) return;

    try {
      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            company,
          }),
        }
      );

      const data = await response.json();

      setResult(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  const recommendation =
    result?.investment_decision?.match(
      /INVEST|WATCHLIST|PASS/i
    )?.[0] || "UNKNOWN";

  const confidence =
    result?.investment_decision?.match(
      /\b\d{1,3}\b/
    )?.[0] || "N/A";

  const riskLevel =
    result?.risk_analysis?.match(
      /LOW|MEDIUM|HIGH/i
    )?.[0] || "UNKNOWN";

  const badgeColor =
    recommendation === "INVEST"
      ? "bg-green-900"
      : recommendation === "WATCHLIST"
      ? "bg-yellow-700"
      : "bg-red-900";

  return (
    <div className="mt-8">

      <div className="flex gap-4">
        <input
          value={company}
          onChange={(e) => setCompany(e.target.value)}
          placeholder="Enter company name"
          className="border p-3 rounded w-96"
        />

        <button
          onClick={analyzeCompany}
          disabled={loading}
          className="bg-black text-white px-6 py-3 rounded disabled:opacity-50"
        >
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </div>

      {loading && <LoadingSpinner />}

      {result && (
        <div className="mt-8">

          {/* Recommendation Badge */}

          <div
            className={`border rounded-xl p-6 mb-6 ${badgeColor}`}
          >
            <h2 className="text-4xl font-bold">
              {recommendation}
            </h2>

            <p className="mt-3 text-lg">
              Confidence: {
                confidence === "N/A"
                  ? "N/A"
                  : `${confidence}%`
              }
            </p>
          </div>

          {/* Stats Row */}

          <div className="grid md:grid-cols-4 gap-4 mb-6">

            <div className="border rounded-xl p-4">
              <h3 className="font-bold">
                Company
              </h3>

              <p>{result.company}</p>
            </div>

            <div className="border rounded-xl p-4">
              <h3 className="font-bold">
                Recommendation
              </h3>

              <p>{recommendation}</p>
            </div>

            <div className="border rounded-xl p-4">
              <h3 className="font-bold">
                Confidence
              </h3>

              <p>
                {confidence === "N/A"
                  ? "N/A"
                  : `${confidence}%`}
              </p>
            </div>

            <div className="border rounded-xl p-4">
              <h3 className="font-bold">
                Risk Level
              </h3>

              <p>{riskLevel}</p>
            </div>

          </div>

          {/* Analysis Cards */}

          <div className="grid md:grid-cols-2 gap-6">

            <AnalysisCard
              title="Company Analysis"
              content={result.company_analysis}
            />

            <AnalysisCard
              title="Financial Analysis"
              content={result.financial_analysis}
            />

            <AnalysisCard
              title="News Analysis"
              content={result.news_analysis}
            />

            <AnalysisCard
              title="Risk Analysis"
              content={result.risk_analysis}
            />

          </div>

          {/* Final Decision */}

          <div className="mt-6">
            <AnalysisCard
              title="Investment Decision"
              content={result.investment_decision}
            />
          </div>

        </div>
      )}
    </div>
  );
}