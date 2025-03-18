from modules.loader import load_documents
from modules.splitter import split_documents
from modules.embedder import get_watsonx_embedder
from modules.indexer import build_index
from modules.llm import get_watsonx_llm
from modules.query_engine import get_query_engine

def main():
    # 1. Load Documents
    documents = load_documents(["data/lora_paper.pdf"])

    # 2. Split
    nodes = split_documents(documents)

    # 3. Embedding Model
    embed_model = get_watsonx_embedder()

    # 4. Indexing
    index = build_index(nodes, embed_model)

    # 5. LLM Setup
    llm = get_watsonx_llm()

    # 6. Query Engine
    query_engine = get_query_engine(index, llm)

    # 7. Querying
    queries = [
        "What is the lora paper about?",
        "List all the evaluation datasets that were used in the lora paper. Only consider the paper."
    ]

    for q in queries:
        print(f"Q: {q}")
        response = query_engine.query(q)
        print(f"A: {response}\n")

if __name__ == "__main__":
    main()
