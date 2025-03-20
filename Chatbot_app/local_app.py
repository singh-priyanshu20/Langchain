from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_community.llms import Ollama 
#from langchain_ollama import OllamaLLM  # Updated import
import streamlit as st 
import os
from dotenv import load_dotenv 

load_dotenv() 

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are an expert assistant.Please give the response in a clear and concise manner."),
        ("user","Question:{question}")
    ]
)

st.title("Chatbot using Langchain Gemma")
input_text=st.text_input("Search the query?")

llm=Ollama(model="gemma3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser 

if input_text:
    st.write(chain.invoke({"question":input_text}))
