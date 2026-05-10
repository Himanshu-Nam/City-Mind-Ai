from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from rich import print
@tool
def length_text(text:str)->int:
    """Return the length of the character in the given text"""
    return len(text)

model = ChatOpenAI(model = "gpt-4o-mini",temperature=0)

#Tool binding

llm_with_tools = model.bind_tools([length_text])

messages= []
query = HumanMessage("Return the number of character in the given text : 'how are you himanshu'")
tool_dict ={
    "length_text":length_text
}
messages.append(query)
res = llm_with_tools.invoke(messages)
messages.append(res)
print(res)

if res.tool_calls:
    tool_name = res.tool_calls[0]['name']
    tool_message=tool_dict[tool_name].invoke(res.tool_calls[0])
    messages.append(tool_message)
   

res2= llm_with_tools.invoke(messages)

print(res2.content)



