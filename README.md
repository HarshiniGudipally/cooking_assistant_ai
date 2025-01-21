# Cooking Assistant AI

## Overview
Cooking Assistant AI is an intelligent chatbot designed to assist users with cooking-related queries. It provides recipes, cooking tips, and ingredient information using natural language processing and a comprehensive culinary knowledge base.

## Features
- Interactive chat interface for cooking queries
- Personalized responses based on user's cooking level and preferences
- Recipe suggestions and cooking techniques
- Ingredient substitutions and nutritional information
- Conversation history tracking

## Project Structure
```
cooking-assistant-ai/
│-- backend/
│   ├── app.py          # FastAPI backend
│   ├── database.py     # Database interactions
│   ├── openai_service.py  # OpenAI integration
│   ├── requirements.txt # Dependencies
│   ├── Dockerfile      # Docker deployment
│-- frontend/
│   ├── app.py          # Streamlit frontend
│   ├── Dockerfile      # Docker deployment
│-- tests/
│   ├── test_api.py     # Unit tests
│-- .env                # API keys (excluded from version control)
│-- README.md           # Project documentation
│-- docker-compose.yml  # Deployment config
```

## Prerequisites
- Python 3.9+
- Docker and Docker Compose (for containerized deployment)
- OpenAI API key

## Setup and Installation

### Clone the repository:
```sh
git clone https://github.com/HarshiniGudipally/cooking_assistant_ai.git
cd cooking_assistant_ai
```

### Set up a virtual environment:
```sh
python -m venv cooking-assistant-ai
source cooking-assistant-ai/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies:
```sh
pip install -r backend/requirements.txt
```

### Set up environment variables:
Create a `.env` file in the project root and add your OpenAI API key:
```sh
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

### Local Development
#### Start the backend:
```sh
uvicorn backend.app:app --reload
```

#### Start the frontend:
```sh
streamlit run frontend/app.py
```

Access the application at [http://localhost:8501](http://localhost:8501)

### Docker Deployment
#### Build and start the containers:
```sh
docker-compose up --build
```

Access the application at [http://localhost:8501](http://localhost:8501)

## Testing
Run the tests using pytest:
```sh
pytest tests
```

## API Endpoints

### POST `/chat`: Send a cooking query
**Request body:**
```json
{
  "session_id": "string",
  "content": "string"
}
```

**Response:**
```json
{
  "response": "string"
}
```

### GET `/history/{session_id}`: Retrieve conversation history
**Response:** List of conversation entries

## Acknowledgments
- OpenAI for providing the GPT model
- FastAPI and Streamlit for the web framework and UI
- SQLAlchemy for database operations
