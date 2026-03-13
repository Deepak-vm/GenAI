from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


# loader
loader = PyPDFLoader('9-document-loaders/pdfs/file-sample_150kB.pdf')
docs = loader.load()


# splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0,
    separators=['\n\n', '\n', ' ']
)

result = splitter.split_documents (docs)
print(len(result))
print(result)