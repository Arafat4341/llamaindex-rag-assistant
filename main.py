from llama_index.llms.ibm import WatsonxLLM
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.ibm import WatsonxEmbeddings
from llama_index.core import VectorStoreIndex
from dotenv import load_dotenv
import os

# load it into LlamaIndex. We'll use the SimpleDirectoryReader for this purpose.
documents = SimpleDirectoryReader(input_files=["data/lora_paper.pdf"]).load_data()
print(documents[0])

# splitting - setting up splitter and see how it divides document into manageable chunks.
splitter = SentenceSplitter(chunk_size=500)
nodes = splitter.get_nodes_from_documents(documents) # transforming our document
# print(len(nodes))

node_metadata = nodes[0].get_content(metadata_mode=True)
# print(str(node_metadata))

# Indexing
# i. Embedding
load_dotenv(os.path.join(os.path.dirname(__file__), 'config', '.env'))

# define embedding model
watsonx_embedding = WatsonxEmbeddings(
    model_id="ibm/slate-125m-english-rtrvr",
    url=os.getenv("IBM_URL"),
    project_id=os.getenv("IBM_PROJECT_ID"),
    apikey=os.getenv("IBM_API_KEY"),
    truncate_input_tokens=3,
)

# ii. Transfroming (embedding) our nodes and Storing them in VectorStoreIndex
"""
 `VectorStoreIndex` will automatically handle the embedding process.
  It converts the nodes into vector representations and stores these embeddings in a vector store.
"""
index = VectorStoreIndex(
    nodes=nodes, 
    embed_model=watsonx_embedding, 
    show_progress=True
)

# # Retrieveing example
# # For this example, we’ll configure the retriever to return the top 3 results for a query about "GPT-2."
# base_retriever = index.as_retriever(similarity_top_k=3) # 3 for top 3 results
# source_nodes = base_retriever.retrieve("GPT-2") # querying about GPT-2

# for node in source_nodes:
#     # print(node.metadata)
#     print(f"---------------------------------------------")
#     print(f"Score: {node.score:.3f}")
#     print(node.get_content())
#     print(f"---------------------------------------------\n\n")

# Querying
# define the model
# In this project, you use ibm/granite-3-8b-instruct
temperature = 0.1
max_new_tokens = 75
additional_params = {
    "decoding_method": "sample",
    "min_new_tokens": 1,
    "top_k": 50,
    "top_p": 1,
}

watsonx_llm = WatsonxLLM(
    model_id="meta-llama/llama-3-3-70b-instruct",
    url=os.getenv("IBM_URL"),
    project_id=os.getenv("IBM_PROJECT_ID"),
    apikey=os.getenv("IBM_API_KEY"),
    temperature=temperature,
    max_new_tokens=max_new_tokens,
    additional_params=additional_params,
)
# response = watsonx_llm.complete("What is a Generative AI?")
# print(response)

# integrate this LLM into our query engine.
query_engine = index.as_query_engine(
  streaming=False, 
  similarity_top_k=7, 
  llm=watsonx_llm
)

response = query_engine.query("What is the lora paper about?")
print(str(response))

response = query_engine.query("List all the evaluation datasets that where used in the lora paper. Only consider the paper.")
print(str(response))
