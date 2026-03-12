from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate   
from langchain_core.runnables import RunnableSequence

from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt = PromptTemplate(
    template='Summarize this document : {document}',
    input_variables=['document']
)

parser = StrOutputParser()

loader = TextLoader('/home/deepak/Desktop/langchain-models/9-document-loaders/demo.txt')

docs = loader.load()

document = (docs[0].page_content)

chain = prompt |model |parser
print(chain.invoke(document))
