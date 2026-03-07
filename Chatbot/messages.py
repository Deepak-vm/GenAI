
from langchain_core.messages import HumanMessage, AIMessage , SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

messages=[
    SystemMessage(content='You are helpful assistant'),
    HumanMessage(content='Tell me about Langchain')
]

result = llm.invoke(messages)

messages.append(AIMessage(content=result.text))

print(result.text)


