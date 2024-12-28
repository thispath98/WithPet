from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

chatllm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

basellm = OpenAI(
    model="gpt-4",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)