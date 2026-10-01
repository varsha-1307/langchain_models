from langchain_core.messages import SystemMessage , HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEndpoint ,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
model = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-120b",
        task="text-generation",
        max_new_tokens=500
    )
)
messages=[
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content='tell me about langchain ')
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)