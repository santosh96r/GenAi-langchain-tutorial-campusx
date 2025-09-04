from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint 

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm )

parser = JsonOutputParser()

template1 = PromptTemplate(
    # template="Give me the name , age and city of the fictional person \n {format_instruction}",
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables= {"format_instruction": parser.get_format_instructions()},
)

# prompt1 = template1.format(**{"topic": "black hole"})
prompt1 = template1.invoke({'topic':"black hole"})

# print(prompt1)

result = model.invoke(prompt1)

# print(result.content)
# print(type(result.content))
final_result = parser.parse(result.content)
print(final_result )
# print(type(final_result))
# print(final_result["name"])
# print(final_result.name)