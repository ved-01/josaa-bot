from llama_index import Document
from llama_index import GPTKeywordTableIndex
# from llama_index import GPTRAKEKeywordTableIndex
from llama_index import GPTVectorStoreIndex
from llama_index import GPTTreeIndex
from llama_index import GPTListIndex
from llama_index.retrievers import VectorIndexRetriever
from llama_index.retrievers import ListIndexRetriever
from llama_index.retrievers import TreeRootRetriever
from llama_index.indices.keyword_table.retrievers import KeywordTableGPTRetriever
from llama_index.storage.docstore import SimpleDocumentStore
from llama_index.vector_stores import SimpleVectorStore
from llama_index.storage.index_store import SimpleIndexStore
# from llama_index import RAKEKeywordTableIndex
from llama_index import GPTSimpleKeywordTableIndex

from llama_index import SimpleDirectoryReader
import time

# documents = SimpleDirectoryReader('./data').load_data()


# document = Document(
#     'The cyclonic storm had a total life of 13 days and three hours (depression to depression), more than double the average life of severe cyclonic storms of six days and three hours over the Arabian Sea, the IMD said in a report on Biparjoy.', 
#     extra_info={
#         'filename': 'data.txt',
#         'category': 'Data about Biparjoy Cyclone'
#     }
# )



# document = Document(
#     os.path.join('data', 'data.txt'), 
#     extra_info={
#         'filename': 'data.txt',
#         'category': 'Data about Biparjoy Cyclone'
#     }
# )


# document_2 = Document(
#     'text', 
#     extra_info={
#         'filename': '2022.txt',
#         'category': 'year 2022'
#     }
# )

# documents = [document, document_2]

############################################### working code
# documents = [document]

from llama_index.node_parser import SimpleNodeParser

# parser = SimpleNodeParser()

# nodes = parser.get_nodes_from_documents(documents)

#################################################


from llama_index import SimpleDirectoryReader, Document
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# document = SimpleDirectoryReader('data').load_data()[0]

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=100)
# text_chunks = text_splitter.split_text(document.text)

# doc_chunks = [Document(text=t,extra_info={'filename': 'output.txt','category': 'Cutoff of the year 2022'}) for t in text_chunks]

# parser = SimpleNodeParser()

# nodes = parser.get_nodes_from_documents(doc_chunks)

documents = SimpleDirectoryReader('data').load_data()
parser = SimpleNodeParser()

nodes = parser.get_nodes_from_documents(documents)



# index = llama_index.GPTKeywordTableIndex(nodes)

from llama_index import StorageContext
# time.sleep(2)
storage_context = StorageContext.from_defaults()
storage_context.docstore.add_documents(nodes)
# storage_context.docstore.add_documents(nodes)
# storage_context.persist(persist_dir="./data")

# index1 = GPTVectorStoreIndex(nodes, storage_context=storage_context)
# index2 = GPTTreeIndex(nodes, storage_context=storage_context)
# index3 = GPTKeywordTableIndex(nodes, storage_context=storage_context)
# index4 = GPTListIndex(nodes, storage_context=storage_context)

index1 = GPTVectorStoreIndex(nodes)
index2 = GPTTreeIndex(nodes)
# index3 = GPTRAKEKeywordTableIndex(nodes)
# index3 = GPTSimpleKeywordTableIndex(nodes)
index3 = GPTKeywordTableIndex(nodes)
index4 = GPTListIndex(nodes)

# index1.save("./data/vector_store_index.json")
# index2.save("./data/tree_index.json")
# index3.save("./data/keyword_table_index.json")

index1.storage_context.persist(persist_dir="vector_store")
index2.storage_context.persist(persist_dir="tree")
index3.storage_context.persist(persist_dir="table")
index4.storage_context.persist(persist_dir="list")
