from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash'    
)

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}', 
    input_variables=['topic']
)

parser=StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'India'})

print(result)
