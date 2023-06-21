import streamlit as st
import llama_index
from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
storage_context_1 = StorageContext.from_defaults(persist_dir="vector_store")
storage_context_2 = StorageContext.from_defaults(persist_dir="tree")
storage_context_3 = StorageContext.from_defaults(persist_dir="table")

# index = load_index_from_storage(storage_context)

# Load the index files
vector_store_index = load_index_from_storage(storage_context_1)
tree_index = load_index_from_storage(storage_context_2)
keyword_table_index = load_index_from_storage(storage_context_3)

indexes = st.multiselect("Select the indexes", ["VectorStoreIndex", "TreeIndex", "GPTKeywordTableIndex"])

indices = []
for index in indexes:
    if index == "VectorStoreIndex":
        indices.append(vector_store_index)
    elif index == "TreeIndex":
        indices.append(tree_index)
    elif index == "GPTKeywordTableIndex":
        indices.append(keyword_table_index)

if indexes:
    query = st.text_input("Enter the query")
    documents = []
    for index in indices:
        documents.extend(index.query(query))

    # Print the results
    for document in documents:
        st.write(document)

 # Display a message if no documents are found
    if not documents:
        st.write("No documents found.")