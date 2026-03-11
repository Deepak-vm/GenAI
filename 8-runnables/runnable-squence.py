from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


# model
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# prompt 
prompt1 = PromptTemplate(
    template='Write a  joke about {topic}', 
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the joke about {joke}', 
    input_variables=['joke']
)

# parser
parser = StrOutputParser()

chain = RunnableSequence(prompt1 , llm , parser , prompt2 , llm , parser)

print(chain.invoke({'topic':'AI'}))
