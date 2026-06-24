from langchain_groq import ChatGroq
from pydantic import SecretStr
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=SecretStr(os.environ["GROQ_KEY"])
)