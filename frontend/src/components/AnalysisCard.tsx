import ReactMarkdown from "react-markdown";

type Props = {
  title: string;
  content: string;
};

export default function AnalysisCard({
  title,
  content,
}: Props) {
  return (
    <div className="border rounded-xl p-6 bg-zinc-900">
      <h2 className="text-xl font-bold mb-4">
        {title}
      </h2>

      <div className="prose prose-invert max-w-none">
        <ReactMarkdown>
          {content}
        </ReactMarkdown>
      </div>
    </div>
  );
}