import os
from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from your .env file
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")



prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Input: {input}")
])

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))


output_parser = StrOutputParser()


chain = prompt | llm | output_parser


st.title("LangChain Gemini ChatBot")
input_text = st.text_input("Enter your question:")

if input_text:
    # Invoke the chain with the user's input
    result = chain.invoke({"input": input_text})
    st.write(result)









# # Streamlit app to interact with the chatbot


# if st.button("Submit"):
    # Load environment variables from .env file
    # load_dotenv()

    # Get the API key from the environment variable
   

    # Initialize the ChatGoogleGenerativeAI model with the API key
    

    # Create a prompt template
# prompt_template = prompt.format_prompt(input=input_text)

    # Generate a response using the LLM
# response = llm(prompt_template.to_messages())

    # Parse the response
# parsed_response = output_parser.parse(response)

    # Display the response
# st.write(parsed_response)

