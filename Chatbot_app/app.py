from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 

import streamlit as st
import os 
from dotenv import load_dotenv 

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
#Langsmith tracking 
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a expert assistant.Please give the response in clear manner"),
        ("user","Question:{question}")
    ]
)

#streamlit code
st.title("Chatbot using Langchain OpenAI")
input_text=st.text_input("Search the topic you want")

#OpenAI LLM code
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser 

if input_text:
    st.write(chain.invoke({'question':input_text}))