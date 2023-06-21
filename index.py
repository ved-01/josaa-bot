import streamlit as st
import llama_index
from llama_index import StorageContext, load_index_from_storage
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.storage.docstore import SimpleDocumentStore
from llama_index.vector_stores import SimpleVectorStore


# rebuild storage context
# storage_context_1 = StorageContext.from_defaults(persist_dir="vector_store")
# storage_context_2 = StorageContext.from_defaults(persist_dir="tree")
# storage_context_3 = StorageContext.from_defaults(persist_dir="table")

# index = load_index_from_storage(storage_context)

# Load the index files
# vector_store_index = load_index_from_storage(storage_context_1)
# tree_index = load_index_from_storage(storage_context_2)
# keyword_table_index = load_index_from_storage(storage_context_3)

# indexes = st.multiselect("Select the indexes", ["VectorStoreIndex", "TreeIndex", "GPTKeywordTableIndex"])

# indices = []
# for index in indexes:
#     if index == "VectorStoreIndex":
#         indices.append(vector_store_index)
#     elif index == "TreeIndex":
#         indices.append(tree_index)
#     elif index == "GPTKeywordTableIndex":
#         indices.append(keyword_table_index)

# if indexes:
#     query_engine = index.as_query_engine()
#     responses = []
#     for index in indices:
#         response = query_engine.query("What did the author do growing up?")
#         responses.append(response)

#     # Print the responses for each index
#     for index, response in zip(indexes, responses):
#         st.write(f"Index: {index}")
#         st.write(f"Response: {response}")

###################################################################################################################################

storage_context = StorageContext.from_defaults(
    docstore=SimpleDocumentStore.from_persist_dir(persist_dir="vector_store"),
    vector_store=SimpleVectorStore.from_persist_dir(persist_dir="tree"),
    index_store=SimpleIndexStore.from_persist_dir(persist_dir="table"),
)


from llama_index import load_index_from_storage, load_indices_from_storage, load_graph_from_storage


indices = load_indices_from_storage(storage_context)


