from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = ["Delhi is Capital of India", "Mumbai is Financial Capital of India"]

vector = embeddings.embed_documents(docs)
print(str(vector))