import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import Chroma
import time

from dotenv import load_dotenv
load_dotenv()


groq_api_key=os.getenv("GROQ_API_KEY")

if "vector" not in st.session_state:
    st.session_state.embeddings=OllamaEmbeddings(model="llama3.2:1b")
    st.session_state.loader=WebBaseLoader("https://google.com")
    st.session_state.docs=st.session_state.loader.load()

    st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)

    st.session_state.vector=Chroma.from_documents(st.session_state.final_documents,st.session_state.embeddings)


st.title("LangChain Groq ChatBot")
llm=ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=groq_api_key)

prompt=ChatPromptTemplate.from_template(
"""
Answer the question based on the context below. 
Please provide the most accurate response based on the question.
<context>
{context}
</context>
Question:{input}

"""

)

document_chain=create_stuff_documents_chain(llm,prompt)
retriever=st.session_state.vector.as_retriever()
retrieval_chain=create_retrieval_chain(document_chain,retriever)

prompt=st.text_input("Enter your question:")

if prompt:
    start=time.process_time()
    with st.spinner("Generating response..."):
        response=retrieval_chain.invoke({"input":prompt})
        print("Response Time:", time.process_time()-start)
        st.write(response["answer"])
