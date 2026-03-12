from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
from dotenv import load_dotenv
load_dotenv()


# directory loader
loader = DirectoryLoader(
    path='9-document-loaders/pdfs', 
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs= loader.load()
document= docs[0].page_content
print(document)


model = ChatGoogleGenerativeAI(model = 'gemini-3.5-flash')

prompt = PromptTemplate(
    template='Summarise the {document}', 
    input_variables=['document']
)

parser = StrOutputParser()

chain = prompt | model | parser 

print(chain.invoke(document))