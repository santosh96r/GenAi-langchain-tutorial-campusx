from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# schema 

# class Review(TypedDict):
#     key_themes : Annotated[list[str] , "Writedown all the key themes discussed in the review in our list "]
#     summary: Annotated[str, "A breif summary of the review"]
#     # sentimate : Annotated[str, "return sentimate of the review either negative , positive or neutral"]
#     sentimate : Annotated[Literal["pos", "neg"], "return sentimate of the review either negative , positive or neutral"]
#     pros : Annotated[Optional[list[str]], "write down all the pros inside a list "]
#     name : Annotated[Optional[str], "write the name of the reviewer "]

class Review(BaseModel):
    key_thems : list[str] = Field(description="Writedown all the key themes discussed in the review in our list ")
    summary : str = Field(description="A breif summary of the review")
    sentimate : Literal["pos", "neg"] = Field(description="return sentimate of the review either negative , positive or neutral")
    pros : Optional[list[str]] = Field(default=None, description="write down all the pros inside a list ")
    name : Optional[str] = Field(description="write the name of the reviewer ")

structured_model = model.with_structured_output(Review)

# result = model.invoke("""The hardware is great , but the software feels bloated , There are too many pre-installed apps that I can't remove . 
#                       Alos , the UI looks outdated compare to other brands. 
#                       Hoping for a software updated to fix this """)

# result = structured_model.invoke("""The hardware is great , but the software feels bloated , There are too many pre-installed apps that I can't remove . 
#                       Alos , the UI looks outdated compare to other brands. 
#                       Hoping for a software updated to fix this """)


result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh""")



# print(result["name"])
# print(result["analy"])
# print(result["sentimate"])

# print(result)
print(dict(result)['key_themes'])

