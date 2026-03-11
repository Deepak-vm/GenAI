from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableBranch
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}', 
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write a short summary of the report {report}', 
    input_variables=['report']
)


model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1 , model ,  parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 100 , RunnableSequence(prompt2 , model , parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_gen_chain , branch_chain)

print(chain.invoke({'topic':'Russia vs Ukraine'}))
