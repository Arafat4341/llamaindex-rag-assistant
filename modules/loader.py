from llama_index.core import SimpleDirectoryReader

def load_documents(file_paths):
    return SimpleDirectoryReader(input_files=file_paths).load_data()
