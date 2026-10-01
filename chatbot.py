from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-120b",
        task="text-generation",
        max_new_tokens=500
    )
)
chat_history=[
    SystemMessage(content='you are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(user_input)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)