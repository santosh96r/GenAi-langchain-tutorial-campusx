from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser 

from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    task= "text-generation"
)

model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name: str = Field(description="name of the person")
    age : int = Field(gt= 18 , description="age of the person")
    city : str = Field(description= "name of the city the person belongs to ")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template= "generate name , age and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.format(**{'place':'india'})

print(prompt)

result = model.invoke(prompt)
final_result = parser.parse(result.content)

# print(type(final_result))