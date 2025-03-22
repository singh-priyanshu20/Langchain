from fastapi import FastAPI #FastAPI handles API routes and requests.
from langchain.prompts import ChatPromptTemplate 
#from langchain.chat_models import ChatOpenAI 
from langserve import add_routes #Deploy LangChain models as APIs easily.
import uvicorn #Uvicorn runs the API server efficiently.
import os 
from langchain_community.llms import Ollama 
from dotenv import load_dotenv 

load_dotenv()

#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

#model=ChatOpenAI()
#openai_llm = ChatOpenAI(model_name="gpt-4", openai_api_key=openai_api_key)
llm=Ollama(model="gemma3")
model=Ollama(model="llama3.2")

prompt1=ChatPromptTemplate.from_template("Write me a short story about {topic} within 100 words")
prompt2=ChatPromptTemplate.from_template("write me a short poem on {topic} with 10 words")

add_routes(
    app,
    prompt1|model, 
    path="/story"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)