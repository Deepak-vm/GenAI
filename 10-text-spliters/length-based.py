from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter


# loader
loader = PyPDFLoader('9-document-loaders/pdfs/file-sample_150kB.pdf')
docs = loader.load()


# splitter
splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents (docs)
print(result[0])