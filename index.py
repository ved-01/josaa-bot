import streamlit as st
from llama_index import StorageContext, load_index_from_storage
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.storage.docstore import SimpleDocumentStore
from llama_index.vector_stores import SimpleVectorStore
from llama_index.storage.index_store import SimpleIndexStore
from llama_index.indices.keyword_table.retrievers import KeywordTableGPTRetriever
from llama_index.retrievers import VectorIndexRetriever, TreeRootRetriever, ListIndexRetriever
from llama_index import ResponseSynthesizer
from llama_index.indices.keyword_table.retrievers import KeywordTableRAKERetriever


# Set up Streamlit layout
st.title("LLAMA Index Query App")
index_options = ["Vector Index", "Table Index", "Tree Index", "List Index"]
selected_indexes = st.multiselect("Select Index(es)", index_options)

# Load indexes based on user selection
indices = []
retrievers = []
for index in selected_indexes:
    if index == "Vector Index":
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore.from_persist_dir(persist_dir="vector_store"),
            vector_store=SimpleVectorStore.from_persist_dir(persist_dir="vector_store"),
            index_store=SimpleIndexStore.from_persist_dir(persist_dir="vector_store"),
        )
        index = load_index_from_storage(storage_context)
        retriever = VectorIndexRetriever(index=index, similarity_top_k=2)
        indices.append(index)
        retrievers.append(retriever)
    elif index == "Table Index":
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore.from_persist_dir(persist_dir="table"),
            vector_store=SimpleVectorStore.from_persist_dir(persist_dir="table"),
            index_store=SimpleIndexStore.from_persist_dir(persist_dir="table"),
        )
        index = load_index_from_storage(storage_context)
        retriever = KeywordTableRAKERetriever(index=index, similarity_top_k=2)
        indices.append(index)
        retrievers.append(retriever)
    elif index == "Tree Index":
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore.from_persist_dir(persist_dir="tree"),
            vector_store=SimpleVectorStore.from_persist_dir(persist_dir="tree"),
            index_store=SimpleIndexStore.from_persist_dir(persist_dir="tree"),
        )
        index = load_index_from_storage(storage_context)
        retriever = TreeRootRetriever(index=index)
        indices.append(index)
        retrievers.append(retriever)
    elif index == "List Index":
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore.from_persist_dir(persist_dir="list"),
            vector_store=SimpleVectorStore.from_persist_dir(persist_dir="list"),
            index_store=SimpleIndexStore.from_persist_dir(persist_dir="list"),
        )
        index = load_index_from_storage(storage_context)
        retriever = ListIndexRetriever(index=index, similarity_top_k=2)
        indices.append(index)
        retrievers.append(retriever)

# Query input
query = st.text_input("Enter your query")

# Perform query and display results
for index, retriever in zip(indices, retrievers):
    response_synthesizer = ResponseSynthesizer.from_args(
    # node_postprocessors=[
    # ]
    )

    query_engine = RetrieverQueryEngine(retriever, response_synthesizer=response_synthesizer)
    response = query_engine.query(query)
    st.subheader(f"Results from {type(index).__name__}")
    st.write(response)
    st.markdown("---")
