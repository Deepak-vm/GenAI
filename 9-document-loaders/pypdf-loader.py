from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt = PromptTemplate(
    template='Summarize this document : {document}',
    input_variables=['document']
)

parser = StrOutputParser()

chain = prompt | model| parser

# PDFLoader
loader = PyPDFLoader('/home/deepak/Desktop/langchain-models/9-document-loaders/file-sample_150kB.pdf')
docs = loader.load()
document = (docs[0].page_content)

#invoke
print(chain.invoke(document))