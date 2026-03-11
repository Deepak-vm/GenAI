from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model1 = ChatGoogleGenerativeAI(model= 'gemini-3.5-flash')

llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.1-8B-Instruct', task="text-generation")

model2 = ChatHuggingFace(llm=llm)


prompt1 = PromptTemplate(
    template='Generate short and simple notes on the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question and anwers on the follwing text o \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n {notes} \n {quiz}',
    input_variables=['notes' , 'quiz']
)

parser= StrOutputParser()

parallel_chain=RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser 
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = "Langchain is a framework for developing applications powered by language models. It enables developers to build complex workflows by chaining together different components, such as prompts, models, and output parsers. LangChain supports various language models, including OpenAI's GPT series, Anthropic's Claude, and Google's Gemini. It also provides tools for working with data, such as vector stores and document loaders, as well as agents that can interact with external systems. LangChain is widely used for building chatbots, question-answering systems, and other AI-powered applications."

result = chain.invoke({'text':text})
print(result)