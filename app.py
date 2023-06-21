from llama_index import GPTKeywordTableIndex
from llama_index import ResponseSynthesizer
from llama_index.indices.keyword_table.retrievers import KeywordTableGPTRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor

from llama_index import SimpleDirectoryReader
import time

documents = SimpleDirectoryReader('D:/NLP/practice/data').load_data()
print("4")
# build index
index = GPTKeywordTableIndex.from_documents(documents)
print("5")
# configure retriever
retriever = index.as_retriever(retriever_mode="default")

# configure response synthesizer
response_synthesizer = ResponseSynthesizer.from_args(
    node_postprocessors=[
    SimilarityPostprocessor(similarity_cutoff=0.7)
   ],
    response_mode="compact"
)
print("3")
query_engine = RetrieverQueryEngine(retriever)
response = query_engine.query("IIT Madras Aerospace Engineering closing rank for Open category Gender Neutral?")
print("2")
# get response
# response.response
str(response)
print("1")
print(response)

time.sleep(2)
