from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-3.6-flash'
)

response = model.invoke("What is the capital city of India")
 
print(response.content)
