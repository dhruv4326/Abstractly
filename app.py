from flask import Flask, request, jsonify ,render_template
from flask_cors import CORS
import os
import warnings
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from langchain_pinecone import PineconeVectorStore

warnings.filterwarnings("ignore")
load_dotenv()

app = Flask(__name__)
CORS(app)  # This allows your HTML to connect to the API

@app.route('/')
def home():
    return render_template("index.html")

# Initialize your RAG components
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", 
    google_api_key=os.environ["GEMINI_API_KEY"]
)
vectorstore = PineconeVectorStore(
    index_name=os.environ["INDEX_NAME"], 
    embedding=embeddings
)
chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   
    temperature=0,
    google_api_key=os.environ["GEMINI_API_KEY"],
    verbose=True
)
qa = ConversationalRetrievalChain.from_llm(
    llm=chat, 
    chain_type="stuff", 
    retriever=vectorstore.as_retriever()
)

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    try:
        data = request.json
        question = data.get('question')
        chat_history = data.get('chat_history', [])
        
        # Convert chat_history format if needed
        formatted_history = []
        for item in chat_history:
            if isinstance(item, list) and len(item) == 2:
                formatted_history.append((item[0], item[1]))
        
        result = qa({
            "question": question, 
            "chat_history": formatted_history
        })
        
        return jsonify({
            "answer": result["answer"],
            "question": result["question"]
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)
