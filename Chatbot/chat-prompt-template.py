
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    ('system' , 'You are helpful {domain} expert'), 
    ('user' , 'Explain in simple terms, what is {topic}')
)

prompt = chat_template.invoke({'domain' : 'AI' , 'topic' : 'Machine Learning'})

print(prompt)