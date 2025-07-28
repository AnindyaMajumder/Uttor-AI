import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import sys
import os
from tqdm import tqdm

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag.core.model import model as get_model
from rag.core.retriever import retriever
from ragas.evaluation import evaluate
from ragas import SingleTurnSample, EvaluationDataset
from langchain_core.documents import Document
from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    answer_correctness,
    answer_similarity
)

# List of metrics to use
metrics_to_use = [
    faithfulness,
    answer_relevancy,
    answer_correctness,
    answer_similarity
]

# Load CSV file containing QA pairs
df = pd.read_csv("qa.csv")

prompt, llm = get_model()
samples = []
for idx, row in tqdm(df.iterrows(), total=len(df)):
    question = row["question"]
    true_answer = row["answer"]

    docs = retriever(question)
    context_docs = []
    for doc in docs["matches"]:
        meta = doc.get("metadata", {})
        text = meta.get("text") or meta.get("content") or meta.get("page_content") or ""
        context_docs.append(Document(page_content=text))
    context_text = "\n\n".join([doc.page_content for doc in context_docs])

    messages = prompt.format_messages(
        context=context_text,
        question=question,
        history=""
    )

    response = llm.invoke(messages)
    model_answer = response.content.strip()

    samples.append(
        SingleTurnSample(
            user_input=question,
            response=model_answer,
            ground_truth=true_answer,
            reference=true_answer,
            retrieved_contexts=[doc.page_content for doc in context_docs]
        )
    )

# Create EvaluationDataset
dataset = EvaluationDataset(samples)

# Run RAGAS evaluation for groundedness and relevance
ragas_scores = evaluate(dataset, metrics=metrics_to_use)
ragas_scores.to_pandas().to_csv("evaluation_scores.csv", index=False)
print("RAGAS evaluation completed and saved")