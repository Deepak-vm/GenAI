from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage , SystemMessage
from dotenv import  load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash')



chat_history = [
    SystemMessage(content='You are helpful AI assistant'), 

]


while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input =='exit':
        break
    result= llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.text))
    print("AI: ", result.text)

    