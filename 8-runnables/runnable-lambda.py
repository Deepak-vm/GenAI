from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableSequence
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


def word_counter(text):
    return len(text.split())



model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')


prompt= PromptTemplate(
    template='Write a joke about {topic}', 
    input_variables=['topic']
)


parser= StrOutputParser()

joke_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    joke = RunnablePassthrough(),
    word_count =  RunnableLambda(word_counter)
)

chain = RunnableSequence(joke_chain , parallel_chain)
print(chain.invoke({'topic':'AI'}))