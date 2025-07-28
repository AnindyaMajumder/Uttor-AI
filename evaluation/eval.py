import pandas as pd
import sys
import os
from tqdm import tqdm

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag.core.model import model as get_model
from rag.core.retriever import retriever
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from ragas.evaluation import evaluate
from ragas import SingleTurnSample, EvaluationDataset
from langchain_core.documents import Document
import ragas.metrics

# List all available RAGAS metrics
print("Available RAGAS metrics:")
available_metrics = [item for item in dir(ragas.metrics) if not item.startswith('_')]
for metric in available_metrics:
    print(f"  - {metric}")
print()

# Dynamically import all available metric functions
metrics_to_use = []
for metric_name in available_metrics:
    try:
        metric_func = getattr(ragas.metrics, metric_name)
        # Check if it's callable (a function/class) and not a module or constant
        if callable(metric_func):
            metrics_to_use.append(metric_func)
            print(f"Added metric: {metric_name}")
    except Exception as e:
        print(f"Could not add metric {metric_name}: {e}")

print(f"\nUsing {len(metrics_to_use)} metrics for evaluation")
print()

# Load CSV file containing QA pairs
df = pd.read_csv("qa.csv")

# Prepare the model and prompt
prompt, llm = get_model()

# Function to create chat history (empty for now)
def get_chat_history():
    return ""


samples = []
for idx, row in tqdm(df.iterrows(), total=len(df)):
    question = row["question"]
    true_answer = row["answer"]


    # Step 1: Retrieve context
    docs = retriever(question)
    context_docs = []
    for doc in docs["matches"]:
        meta = doc.get("metadata", {})
        # Debug print to inspect metadata
        print(f"DEBUG metadata: {meta}")
        # Try multiple possible keys for text content
        text = meta.get("text") or meta.get("content") or meta.get("page_content") or ""
        context_docs.append(Document(page_content=text))
    context_text = "\n\n".join([doc.page_content for doc in context_docs])

    # Step 2: Format prompt
    messages = prompt.format_messages(
        history=get_chat_history(),
        context=context_text,
        question=question
    )

    # Step 3: Get model answer
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

# Run RAGAS evaluation
ragas_scores = evaluate(dataset, metrics=[faithfulness, answer_relevancy, context_precision])
ragas_scores.to_pandas().to_csv("ragas_evaluation_scores.csv", index=False)
print("RAGAS evaluation completed and saved to ragas_evaluation_scores.csv")