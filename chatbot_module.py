from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

# --- Chatbot ---
def chatbot(query, system_context):   
    chat = ChatOpenAI(model='gpt-4')
    prompt_0 = "Hi there, climate chatbot! \n"
    prompt_1 = "Given the passages, Provide an answer citing the SOURCE AND PAGE. \n"
    prompt_2 = "If the answer is still not available, say you don't know. \n"
    prompt_3 = "Here are the passages. \n"
    context = prompt_0 + prompt_1 + prompt_2 + prompt_3 + system_context
    messages = [
        SystemMessage(content=context), 
        HumanMessage(content=query)
        ]
    return chat(messages).content