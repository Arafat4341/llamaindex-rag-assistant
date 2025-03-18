def get_query_engine(index, llm, top_k=7):
    return index.as_query_engine(
        streaming=False,
        similarity_top_k=top_k,
        llm=llm
    )
