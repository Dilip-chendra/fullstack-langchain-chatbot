from fastapi import FastAPI
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from secret_key import openrouter_api_key1

app = FastAPI()
backend_history = InMemoryChatMessageHistory()


model = ChatOpenRouter(
    model="openrouter/free", 
    openrouter_api_key=openrouter_api_key1
)

@app.get("/")
def hello():
    return {"Message": "Hello! Welcome To The Dilip Chat Bot backend infrastructure."}

@app.get("/ChatBot")
def backend(message: str):
    backend_history.add_user_message(message)
    try:
        response1 = model.invoke(backend_history.messages)
        ai_text = response1.content
        
        backend_history.add_message(AIMessage(content=ai_text))
        
        return {"result": ai_text}
    except Exception as e:
        return {"result": f"Execution pipeline error encountered: {str(e)}"}
