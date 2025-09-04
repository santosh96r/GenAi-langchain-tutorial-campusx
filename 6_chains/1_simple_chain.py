# # from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# prompt = PromptTemplate(
#     template="generate 5 interesting facts about {topic}",
#     input_variables=["topic"]
# )

# model = ChatOpenAI()

# parser = StrOutputParser()
# chain = prompt | model | parser

# result = chain.invoke({"topic":"cricket"})
# print(result)



from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prmopt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables= ["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()



chain = prmopt | model | parser

result = chain.invoke({'topic': " cricket"})
print(result)

# template = PromptTemplate(
#     template="write 5 interesting fact about {topic}",
#     input_variables= ['topic']
# )

# prompt = template.format(**{'topic': 'cricket'})
# model = ChatOpenAI()
# result = model.invoke(prompt)
# parser = StrOutputParser()
# final_result = parser.parse(result)
# print(final_result.content)