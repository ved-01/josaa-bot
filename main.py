from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader(r'D:\NLP\practice\data').load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("IIT Bombay Mechanical Engineering cutoff for General Category Gender neutral in the year 2022")
print(response)