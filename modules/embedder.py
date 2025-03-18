from llama_index.embeddings.ibm import WatsonxEmbeddings
import os
from dotenv import load_dotenv

def get_watsonx_embedder():
    load_dotenv(os.path.join(os.path.dirname(__file__), '../config/.env'))
    return WatsonxEmbeddings(
        model_id="ibm/slate-125m-english-rtrvr",
        url=os.getenv("IBM_URL"),
        project_id=os.getenv("IBM_PROJECT_ID"),
        apikey=os.getenv("IBM_API_KEY"),
        truncate_input_tokens=3
    )
