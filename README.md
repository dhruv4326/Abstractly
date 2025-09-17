# 🤖 Abstractly - Generative AI Research Paper Chatbot

A sophisticated RAG (Retrieval-Augmented Generation) chatbot built with Flask that allows users to interact with and ask questions about a Generative AI research paper. The system uses Google's Gemini AI for both embeddings and chat completion, with Pinecone as the vector database for efficient document retrieval.

## ✨ Features

- **Interactive Chat Interface**: Modern, responsive web UI with real-time messaging
- **Document Q&A**: Ask questions about the Generative AI research paper and get accurate, context-aware answers
- **RAG Architecture**: Combines document retrieval with generative AI for enhanced responses
- **Chat History**: Maintains conversation context for better follow-up questions
- **Real-time Indicators**: Shows typing indicators and handles errors gracefully
- **Responsive Design**: Works seamlessly on desktop and mobile devices


## 📁 Project Structure

```
RAG_CHATBOT/
├── data/
│   └── impact_of_generativeAI.pdf    # Research paper for RAG
├── templates/
│   └── index.html                    # Frontend chat interface
├── venv/                             # Virtual environment
├── .env                              # Environment variables
├── .gitignore                        # Git ignore file
├── app.py                            # Main Flask application
├── ingestion.py                      # Document processing script
├── profile                           # Project profile
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google AI API Key (for Gemini)
- Pinecone API Key
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd RAG_CHATBOT
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   INDEX_NAME=your_pinecone_index_name
   ```

5. **Initialize the vector database**
   Run the ingestion script to process and store the research paper:
   ```bash
   python ingestion.py
   ```

6. **Start the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   Navigate to `http://localhost:5000`

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google AI API key for Gemini models | Yes |
| `PINECONE_API_KEY` | Pinecone vector database API key | Yes |
| `INDEX_NAME` | Name of your Pinecone index | Yes |

### Model Configuration

The chatbot uses the following Google AI models:
- **Embeddings**: `models/gemini-embedding-001`
- **Chat**: `gemini-2.5-flash` (with temperature=0 for consistent responses)

## 📋 API Endpoints

### POST `/api/chat`
Main chat endpoint for user interactions.

**Request Body:**
```json
{
  "question": "What are the applications of generative AI?",
  "chat_history": [
    ["Previous question", "Previous answer"]
  ]
}
```

**Response:**
```json
{
  "answer": "AI generated response based on the research paper",
  "question": "What are the applications of generative AI?"
}
```

### GET `/`
Serves the main chat interface.

## 🔍 How It Works

1. **Document Ingestion** (`ingestion.py`):
   - Loads the PDF research paper using PyPDFLoader
   - Splits the document into 1000-character chunks with 100-character overlap
   - Creates embeddings using Google's Gemini embedding model
   - Stores embeddings in Pinecone vector database

2. **Query Processing** (`app.py`):
   - Receives user questions via the web interface
   - Uses ConversationalRetrievalChain to:
     - Retrieve relevant document chunks from Pinecone
     - Generate contextual responses using Gemini AI
     - Maintain conversation history for follow-up questions

3. **Frontend Interface**:
   - Modern, responsive chat UI built with vanilla HTML, CSS, and JavaScript
   - Real-time messaging with typing indicators
   - Error handling and user feedback
   - Mobile-responsive design

## 💻 Technologies Used

### Backend
- **Flask**: Web framework
- **LangChain**: RAG pipeline orchestration
- **Google Gemini AI**: Embeddings and chat completion
- **Pinecone**: Vector database for document storage
- **PyPDF**: PDF document processing

### Frontend
- **HTML5/CSS3**: Modern responsive design
- **JavaScript (Vanilla)**: Interactive chat functionality
- **Axios**: HTTP client for API communication

## 🎯 Usage Examples

### Sample Questions You Can Ask:

- "What is generative AI and how does it work?"
- "What are the main applications of generative AI mentioned in the paper?"
- "What are the challenges and limitations discussed?"
- "How does generative AI impact different industries?"
- "What future developments are predicted for generative AI?"

## 🛠️ Development

### Adding New Documents
1. Place your PDF in the `data/` directory
2. Update the file path in `ingestion.py`
3. Run `python ingestion.py` to reprocess and store embeddings

### Customizing the UI
- Modify `templates/index.html` for layout changes
- Update CSS styles within the HTML file
- Adjust JavaScript for additional functionality

### Changing AI Models
- Update the model names in `app.py`
- Ensure your API keys support the new models
- Test thoroughly after changes

## ⚠️ Troubleshooting

### Common Issues

1. **"Cannot connect to server"**
   - Ensure Flask app is running on port 5000
   - Check if firewall is blocking the connection

2. **"API Key Error"**
   - Verify your `.env` file contains correct API keys
   - Check if API keys have necessary permissions

3. **"Pinecone Index Not Found"**
   - Ensure you've run `ingestion.py` first
   - Verify the index name in your `.env` file

4. **"No documents found"**
   - Check if the PDF file exists in the `data/` directory
   - Ensure the file path in `ingestion.py` is correct

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Built with ❤️ using Flask, LangChain, Google Gemini AI, and Pinecone.