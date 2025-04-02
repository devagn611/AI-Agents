from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Input: {input}")
])

st.title("LangChain Local ChatBot")
input_text = st.text_input("Enter your question:")

llm = Ollama(model="llama3.2:1b")
# llm = Ollama(model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"input": input_text}))