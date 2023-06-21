from llama_index import GPTKeywordTableIndex
from llama_index import ResponseSynthesizer
from llama_index.indices.keyword_table.retrievers import KeywordTableGPTRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor

from llama_index import SimpleDirectoryReader

documents = SimpleDirectoryReader('D:/NLP/practice/data').load_data()

# build index
index = GPTKeywordTableIndex.from_documents(documents)

# configure retriever
retriever = index.as_retriever(retriever_mode="default")

# configure response synthesizer
response_synthesizer = ResponseSynthesizer.from_args(
    node_postprocessors=[
    SimilarityPostprocessor(similarity_cutoff=0.7)
   ]
)

query_engine = RetrieverQueryEngine(retriever, response_mode= 'compact')
response = query_engine.query("What was the tenure of Dr. kalam?")

# get response
# response.response
str(response)

print(response)

