from langchain_text_splitters import RecursiveCharacterTextSplitter

code = """
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review in a list"
    )
    summary: str = Field(
        description="A brief summary of the review"
    )
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language="python", #yaha bohut sari language ka support he jese java , cpp , markdown et 
    chunk_size=100,
    chunk_overlap=0
)

result = splitter.split_text(code)

print(len(result))
print(result)