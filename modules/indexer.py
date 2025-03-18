from llama_index.core import VectorStoreIndex

def build_index(nodes, embed_model):
    return VectorStoreIndex(nodes=nodes, embed_model=embed_model, show_progress=True)
