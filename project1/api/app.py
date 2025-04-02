from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import OllamaLLM
from pydantic import RootModel


load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

app = FastAPI(
    title="LangChain Local ChatBot",
    version="1.0",
    description="A simple chatbot using LangChain and Ollama.",
)

add_routes(
    app,
    ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY")),
    path="/gemini"
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

llm = OllamaLLM(model="llama3.2:1b")

prompt1 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Write me an essay about {input} with 100 words.")
])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a creative poet."),
    ("human", "Write me a poem about {input} with 100 words.")
])

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
