#!/usr/bin/python3
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()

api_key=os.getenv("github-token")

#create llm
llm=ChatOpenAI(
    model="gpt-4o",
    openai_api_key=api_key,
    base_url="https://models.inference.ai.azure.com"
)



result=llm.invoke("Hello there?")

print(f"AI: {result.content}")