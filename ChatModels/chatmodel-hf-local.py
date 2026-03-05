from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(model="llama3.2:3b")

response = model.invoke("What is the capital of India")
print(response.content)