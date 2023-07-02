import streamlit as st
from llama_index import StorageContext, load_index_from_storage
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.storage.docstore import SimpleDocumentStore
from llama_index.vector_stores import SimpleVectorStore
from llama_index.storage.index_store import SimpleIndexStore
from llama_index import KeywordTableIndex
from llama_index.indices.keyword_table import SimpleKeywordTableIndex
from llama_index import ResponseSynthesizer
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index.retrievers import VectorIndexRetriever
from llama_index.retrievers import ListIndexRetriever
from llama_index.retrievers import TreeRootRetriever
from llama_index.indices.keyword_table.retrievers import KeywordTableGPTRetriever
from llama_index.indices.keyword_table.retrievers import KeywordTableRAKERetriever
from llama_index.indices.keyword_table.retrievers import KeywordTableSimpleRetriever
from llama_index import LLMPredictor
from langchain.chat_models import ChatOpenAI
from llama_index import ServiceContext
from llama_index import Prompt


st.title("Josaa Query App")
index_options = ["Vector Index", "Table Index", "Tree Index", "List Index"]
selected_indexes = st.multiselect("Select Index", index_options)

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
        retriever = KeywordTableGPTRetriever(index=index, similarity_top_k=2)
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

query = st.text_input("Enter your query")

for index in indices:
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=True))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, chunk_size=512)
    response_synthesizer = ResponseSynthesizer.from_args()
    TEMPLATE_STR = (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given this information, please answer the question: {query_str}\n"
    )
    QA_TEMPLATE = Prompt(TEMPLATE_STR)
    query_engine = index.as_query_engine(service_context=service_context, text_qa_template=QA_TEMPLATE, similarity_top_k=3, streaming=True)

    response = query_engine.query(query)
    st.subheader(f"Results from {index.__class__.__name__}")
    st.write(response)
    st.markdown("---")
