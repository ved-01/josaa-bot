from llama_index import Document
from llama_index import GPTKeywordTableIndex
from llama_index import VectorStoreIndex
from llama_index import TreeIndex
import llama_index

document = Document(
    'text', 
    extra_info={
        'filename': '2020.txt',
        'category': 'year 2020'
    }
)

document_2 = Document(
    'text', 
    extra_info={
        'filename': '2022.txt',
        'category': 'year 2022'
    }
)

documents = [document, document_2]

from llama_index.node_parser import SimpleNodeParser

parser = SimpleNodeParser()

nodes = parser.get_nodes_from_documents(documents)

# index = llama_index.GPTKeywordTableIndex(nodes)

from llama_index import StorageContext

storage_context = StorageContext.from_defaults()
storage_context.docstore.add_documents(nodes)
# storage_context.persist(persist_dir="./data")

index1 = VectorStoreIndex(nodes, storage_context=storage_context)
index2 = TreeIndex(nodes, storage_context=storage_context)
index3 = GPTKeywordTableIndex(nodes, storage_context=storage_context)

# index1.save("./data/vector_store_index.json")
# index2.save("./data/tree_index.json")
# index3.save("./data/keyword_table_index.json")

index1.storage_context.persist(persist_dir="vector_store")
index2.storage_context.persist(persist_dir="tree")
index3.storage_context.persist(persist_dir="table")
