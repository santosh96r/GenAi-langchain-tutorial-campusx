from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    model= "mistralai/Mistral-7B-Instruct-v0.3", 
    task= "text-generation"
)

model = ChatHuggingFace(llm =llm)

# 1st prompt --> detailed report 
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt --> summary 
template2 = PromptTemplate(
    template="write a 5 line summary on the following text. \n {text}",
    input_variables=["text"]
)
# 
# prompt1 = template1.format({"topic" : "Black hole"}) ###########=========== we can use "invoke or format "
# result1 = model.invoke(prompt1)

# prompt2 = template2.invoke({"text" : result1.content})

# result2 = model.invoke(prompt2)

# print(type(result2.content))

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({'topic': "black hole "})

print(result )