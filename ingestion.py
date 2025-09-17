import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore


load_dotenv()

# loading document for ingestion
loader=PyPDFLoader("data/impact_of_generativeAI.pdf")
document=loader.load()

# splitting documents into the chunks 

text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=100);
texts=text_splitter.split_documents(document)
print(f"created{len(texts)} chunks")

# creating emebeddings and storing into pinecone vector store

#embeddings=OpenAIEmbeddings(openai_api_type=os.environ.get("OPENAI_API_KEY"))
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",   # Gemini embedding model
    google_api_key=os.environ.get("GEMINI_API_KEY")
)
PineconeVectorStore.from_documents(texts,embeddings,index_name=os.environ.get("INDEX_NAME"))
