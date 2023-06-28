import streamlit as st
import llama_index
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
from llama_index.indices.keyword_table import GPTSimpleKeywordTableIndex
from llama_index.indices.keyword_table.retrievers import KeywordTableRAKERetriever
from llama_index.indices.keyword_table.retrievers import KeywordTableSimpleRetriever


print("1")
storage_context_1 = StorageContext.from_defaults(
    docstore=SimpleDocumentStore.from_persist_dir(persist_dir="vector_store"),
    vector_store=SimpleVectorStore.from_persist_dir(persist_dir="vector_store"),
    index_store=SimpleIndexStore.from_persist_dir(persist_dir="vector_store"),
)

storage_context_2 = StorageContext.from_defaults(
    docstore=SimpleDocumentStore.from_persist_dir(persist_dir="table"),
    vector_store=SimpleVectorStore.from_persist_dir(persist_dir="table"),
    index_store=SimpleIndexStore.from_persist_dir(persist_dir="table"),
)
storage_context_3 = StorageContext.from_defaults(
    docstore=SimpleDocumentStore.from_persist_dir(persist_dir="tree"),
    vector_store=SimpleVectorStore.from_persist_dir(persist_dir="tree"),
    index_store=SimpleIndexStore.from_persist_dir(persist_dir="tree"),
)
storage_context_4 = StorageContext.from_defaults(
    docstore=SimpleDocumentStore.from_persist_dir(persist_dir="list"),
    vector_store=SimpleVectorStore.from_persist_dir(persist_dir="list"),
    index_store=SimpleIndexStore.from_persist_dir(persist_dir="list"),
)

print("2")
from llama_index import load_index_from_storage, load_indices_from_storage, load_graph_from_storage

indices1 = load_index_from_storage(storage_context_1)
indices2 = load_index_from_storage(storage_context_2)
indices3 = load_index_from_storage(storage_context_3)
indices4 = load_index_from_storage(storage_context_4)

print("3")
retriever1 = VectorIndexRetriever(
    index=indices1, 
    similarity_top_k=2,
)


# retriever2 = KeywordTableRAKERetriever(
#     index=indices2, 
#     similarity_top_k=2,
# )

# retriever2 = KeywordTableSimpleRetriever(
#     index=indices2, 
#     similarity_top_k=2,
# )
retriever2 = KeywordTableGPTRetriever(
    index=indices2, 
    similarity_top_k=2,
)

retriever3 = TreeRootRetriever(
    index=indices3, 
#     similarity_top_k=2,
)

retriever4 = ListIndexRetriever(
    index=indices4, 
    similarity_top_k=2,
)
print("4")
from llama_index.indices.response import BaseResponseBuilder


# response_builder = BaseResponseBuilder()
# response_mode = "compact"


# configure response synthesizer
response_synthesizer = ResponseSynthesizer.from_args(
    # node_postprocessors=[
    # ]
)


    
print("5")
query_engine_1 = RetrieverQueryEngine(
    retriever1, response_synthesizer=response_synthesizer
)
query_engine_2 = RetrieverQueryEngine(
    retriever2, response_synthesizer=response_synthesizer
)
query_engine_3 = RetrieverQueryEngine(
    retriever3, response_synthesizer=response_synthesizer
)
query_engine_4 = RetrieverQueryEngine(
    retriever4, response_synthesizer=response_synthesizer
)

# response = query_engine_1.query("Tell me about Early life of Dr. Avul Pakir kalam?")
# print(response)
response = query_engine_2.query("Tell me about Early life of Dr. Avul Pakir kalam?")

# print("7")
str(response)
print(response)
response1 = query_engine_1.query("Tell me about Early life of Dr. Avul Pakir kalam?")
print(response1)
response2 = query_engine_3.query("Tell me about Early life of Dr. Avul Pakir kalam?")
print(response2)
response3 = query_engine_4.query("Tell me about Early life of Dr. Avul Pakir kalam?")
print(response3)
# print(response)
print("8")

# response.source_nodes
print(response.source_nodes)
