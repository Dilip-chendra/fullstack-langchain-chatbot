# Full-Stack LangChain Chatbot (Flat Local Setup)

A decoupled full-stack AI chatbot architecture built with FastAPI, Streamlit, and LangChain. This repository implements stateful chat memory across network boundaries and leverages dynamic model orchestration.

## Architecture Overview
- **Backend (FastAPI + LangChain):** Manages conversational state tracking using `InMemoryChatMessageHistory` inside `gpt3.py` to bypass LLM statelessness. It translates incoming user strings into structured message payloads and communicates with OpenRouter API nodes.
- **Frontend (Streamlit):** Serves as an interactive interface inside `Chatbot.py`. It communicates asynchronously with the backend API over HTTP `requests` and handles visualization persistence across page refreshes via `st.session_state`.

## Current Project Structure
```text
FASTAPI/
│
├── __pycache__/
├── myvenv/                # Your Python virtual environment
├── Chatbot.py             # Streamlit chat user interface (Frontend)
├── gpt3.py                # FastAPI & LangChain orchestration logic (Backend)
├── secret_key.py          # Local OpenRouter API key credentials file
└── README.md              # Project documentation
```

## Setup and Installation

### Running Globally (Local Without Docker)

1. Clone the repository and navigate into the project directory:
   ```bash
   git clone https://github.com
   cd FASTAPI
   ```

2. Activate your existing virtual environment (`myvenv`):
   ```bash
   # On Windows (PowerShell):
   .\myvenv\Scripts\Activate.ps1
   
   # On Windows (Command Prompt):
   .\myvenv\Scripts\activate.bat
   ```

3. Install the required dependency libraries if you haven't already:
   ```bash
   pip install fastapi uvicorn langchain-openrouter langchain-core streamlit requests
   ```

4. Verify your `secret_key.py` contains your token:
   ```python
   openrouter_api_key1 = "your_actual_openrouter_api_key_here"
   ```

5. Run your FastAPI backend server using your local environment python runner:
   ```bash
   .\myvenv\Scripts\uvicorn gpt3:app --reload
   ```

6. Open a separate terminal split window, ensure your virtual environment is active, and launch the Streamlit frontend client app:
   ```bash
   .\myvenv\Scripts\streamlit run Chatbot.py
   ```

- **Frontend UI Workspace:** Open `http://localhost:8501` inside your web browser.
- **Backend API Endpoints:** Open `http://localhost:8000/docs` to view the interactive FastAPI Swagger documentation.

## System Workflow
1. The user types a query into the Streamlit interactive chat box (`Chatbot.py`).
2. The user interface logs the message locally into `st.session_state` and fires an HTTP GET network request containing the prompt string to the local address `http://127.0.0`.
3. The FastAPI endpoint inside `gpt3.py` captures the string parameter, wraps it into a `HumanMessage` schema object, and saves it into `InMemoryChatMessageHistory`.
4. The historical conversation log list is bundled and pushed to OpenRouter via the universal model router `openrouter/free` to maintain conversational context.
5. The API parses the text answer, updates the backend memory map with an `AIMessage` data object, and returns a JSON dictionary back across the network to render the text bubble visually in Streamlit.
