import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import PyPDFDirectoryLoader
import time

from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

st.title("Q&A with PDF")
llm=ChatGroq(
    model="llama-3.2-1b-preview",
    temperature=0.1,
    max_tokens=512,
    groq_api_key=groq_api_key
)

prompt=ChatPromptTemplate.from_messages([
    """
    You are a helpful assistant. Answer the question based on the context provided.
    please provide the most accurate response based on the question and context.
    <context>
    {context}
    </context>
    Question: {question}
    """
])




def vector_embedding():

    if "vector" not in st.session_state:
        st.session_state.embeddings = OllamaEmbeddings(model="llama3.2:1b")
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")
        st.session_state.documents = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.documents[:6])
        st.session_state.vector_store = FAISS.from_documents(
            st.session_state.final_documents,
            st.session_state.embeddings
        )


prompt1=st.text_input("Enter your question here")

if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store is ready")


    document_chain= create_stuff_documents_chain(llm,prompt)
    retriever= st.session_state.vector_store.as_retriever()
    retriever_chain=create_retrieval_chain(retriever, document_chain)

if prompt1:
    # start=time.process_time()
    response=retriever_chain.invoke({"input": prompt1})
    st.write(response["answer"])

    with st.expander("Show all context"):
        for i,doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("------------------")
