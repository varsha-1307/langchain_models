from langchain_core.prompts import ChatPromptTemplate


chat_template=ChatPromptTemplate.from_messages([
    ('system','you are a helpful {domain} expert'),
    ('human','explain in smpile terms,what is the {topic}')
])
prompt=chat_template.invoke({'domain':'cricket','topic':'dusra'})
print(prompt)
