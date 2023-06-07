from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader(r'D:\NLP\practice\data').load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("Name of all Institutes?")
print(response)