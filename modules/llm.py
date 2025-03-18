from llama_index.llms.ibm import WatsonxLLM
import os
from dotenv import load_dotenv

def get_watsonx_llm():
    load_dotenv(os.path.join(os.path.dirname(__file__), '../config/.env'))
    return WatsonxLLM(
        model_id="meta-llama/llama-3-3-70b-instruct",
        url=os.getenv("IBM_URL"),
        project_id=os.getenv("IBM_PROJECT_ID"),
        apikey=os.getenv("IBM_API_KEY"),
        temperature=0.1,
        max_new_tokens=75,
        additional_params={
            "decoding_method": "sample",
            "min_new_tokens": 1,
            "top_k": 50,
            "top_p": 1,
        }
    )
