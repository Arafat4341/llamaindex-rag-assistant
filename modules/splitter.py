from llama_index.core.node_parser import SentenceSplitter

def split_documents(documents, chunk_size=500):
    splitter = SentenceSplitter(chunk_size=chunk_size)
    return splitter.get_nodes_from_documents(documents)
