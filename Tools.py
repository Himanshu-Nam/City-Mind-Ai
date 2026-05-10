from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#Tools are also ruunble

search_tools = TavilySearchResults(max_result=5)

model = ChatOpenAI(model = "gpt-4o-mini",temperature=0)

prompt = ChatPromptTemplate.from_template(
    """
you are a very helpful assistant

summarize the following news into the new clear bullet point

{news}
"""
)
parser =StrOutputParser()

chains = prompt|model|parser

res = search_tools.run("Lates Ai news in May 2026")

result = chains.invoke({"news":res})

#print(result)
print(search_tools.name)
print(search_tools.description)
print(search_tools.args)