from langchain_core.runnables import RunnableSequence
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt1 = PromptTemplate(
    template='Write a joke about {topic}', 
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the joke {joke}', 
    input_variables=['joke']
)


parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    joke= RunnablePassthrough(), 
    explaination= RunnableSequence(prompt2 , model , parser)
)

chain = RunnableSequence(joke_gen_chain , parallel_chain )

print(chain.invoke({'topic':'AI'}))