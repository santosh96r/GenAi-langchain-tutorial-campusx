from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# used to control the inputs and expected op
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal , Annotated

from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda

load_dotenv()

model = ChatOpenAI()
parser  = StrOutputParser()

class Feedback(BaseModel):
    sentimate : Literal['positive', 'negative'] = Field(description="generate the sentimate of the following feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template= 'Classify the sentimate of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables= {'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# print(classifier_chain.invoke({'feedback': 'this is a terrible smartphone'}))


#-------------------------------------conditional chain ---------------------------------
# branch_chain = RunnableBranch(
#     (condition1 , chain ),
#     (condition2 , chain ),
#     default chain 
# )

prompt2 = PromptTemplate(
    template= " write an appropiate response to this positive feedback \n {feedback}",
    input_variables= ['feedback']
)
prompt3 = PromptTemplate(
    template='Write an appropiate response for this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x : x.sentimate == 'positive' , prompt2 | model | parser), 
    (lambda x : x.sentimate == 'negative',  prompt3 | model | parser), 
    RunnableLambda(lambda x : 'couldnot find any sentimate ') 
)

chain = classifier_chain | branch_chain 
result = chain.invoke({'feedback': 'This is a terrible phone '})

print(result)


