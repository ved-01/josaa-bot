from llama_index import Document
from llama_index import GPTKeywordTableIndex
from llama_index import GPTVectorStoreIndex
from llama_index import GPTTreeIndex
from llama_index import GPTListIndex
import llama_index

document = Document(
    'text', 
    extra_info={
        'filename': 'data.txt',
        'category': 'Data about DRAM'
    }
)

# document_2 = Document(
#     'text', 
#     extra_info={
#         'filename': '2022.txt',
#         'category': 'year 2022'
#     }
# )

# documents = [document, document_2]
documents = [document]

from llama_index.node_parser import SimpleNodeParser

parser = SimpleNodeParser()

nodes = parser.get_nodes_from_documents(documents)

# index = llama_index.GPTKeywordTableIndex(nodes)

from llama_index import StorageContext

storage_context = StorageContext.from_defaults()
storage_context.docstore.add_documents(nodes)
# storage_context.persist(persist_dir="./data")

# index1 = GPTVectorStoreIndex(nodes, storage_context=storage_context)
# index2 = GPTTreeIndex(nodes, storage_context=storage_context)
# index3 = GPTKeywordTableIndex(nodes, storage_context=storage_context)
# index4 = GPTListIndex(nodes, storage_context=storage_context)

index1 = GPTVectorStoreIndex(nodes)
index2 = GPTTreeIndex(nodes)
index3 = GPTKeywordTableIndex(nodes)
index4 = GPTListIndex(nodes)

# index1.save("./data/vector_store_index.json")
# index2.save("./data/tree_index.json")
# index3.save("./data/keyword_table_index.json")

index1.storage_context.persist(persist_dir="vector_store")
index2.storage_context.persist(persist_dir="tree")
index3.storage_context.persist(persist_dir="table")
index4.storage_context.persist(persist_dir="list")

