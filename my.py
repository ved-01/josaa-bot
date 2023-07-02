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
from llama_index import Prompt
from llama_index import LLMPredictor
from langchain.chat_models import ChatOpenAI
from llama_index import ServiceContext


def main():

    st.title("Llama Index App")

    # Select indexes
    index_names = ["vector_store", "table", "tree", "list"]
    index_choices = st.multiselect("Select indexes", index_names)

    # Load indexes from storage contexts
    indices = []
    for index_name in index_choices:
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore.from_persist_dir(persist_dir=index_name),
            vector_store=SimpleVectorStore.from_persist_dir(persist_dir=index_name),
            index_store=SimpleIndexStore.from_persist_dir(persist_dir=index_name),
        )
        index = load_index_from_storage(storage_context)
        indices.append(index)

    # Prompt user for query
    query = st.text_input("Enter your query")

    # Query the indexes
    response = None
    for index in indices:
        TEMPLATE_STR = (
        "We have provided context information below. \n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Given this information, please answer the question: {query_str}\n"
        )
        QA_TEMPLATE = Prompt(TEMPLATE_STR)
        llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=True))
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, chunk_size=5000)
        query_engine = index.as_query_engine(
        service_context=service_context,
        text_qa_template=QA_TEMPLATE,
        similarity_top_k=3,
        streaming=True,
        )
        response = query_engine.query(query)
        st.subheader(f"Results from {index.__class__.__name__}")

    # Display the response
        if response:
            # formatted_sources = response.get_formatted_sources()
            
            st.text(response)
            print(response)


if __name__ == "__main__":
    main()


###### working ########