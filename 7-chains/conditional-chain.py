from langchain_core.runnables import RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import Field
from pydantic import BaseModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

class Feedback(BaseModel):

    sentiment: Literal['positive' , 'negative'] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback into positive or negative  \n {feedback} \n {format_instruction}', 
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

parser = StrOutputParser()


classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write a appropriate response to the positive feedback  \n {feedback}', 
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write a appropriate response to the negative feedback  \n {feedback}', 
    input_variables=['feedback']
)

chain2 = prompt2 | model | parser
chain3 = prompt3 | model | parser

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', chain2),
    (lambda x: x.sentiment == 'negative', chain3),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'This is a great product!'})

print(result)