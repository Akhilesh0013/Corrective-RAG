import os
from typing import Optional, Any


from typing import List
from llama_index.core.schema import  NodeWithScore
from llama_index.core.workflow import (
    Event,
)

from llama_index.core.prompts import PromptTemplate 
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    step,
    Workflow,
    Context,
)
from llama_index.core.llms import LLM
from linkup import LinkupClient
from llama_index.tools.linkup_research import LinkupToolSpec








from dotenv import load_dotenv

load_dotenv()


class RetrieveEvent(Event) :

    retrieved_nodes : List[NodeWithScore]


class WebSearchEvent(Event):
    """Web search event."""

    relevant_text: str  


class QueryEvent(Event):
    """Query event. Queries given relevant text and search text."""

    relevant_text: str
    search_text: str



DEFAULT_RELEVANCY_PROMPT_TEMPLATE = PromptTemplate( 

template = """
As a grader, your task is to evaluate the relevance of a document retrieved in response to a user's question.

Retrieved Document:
-------------------
{context_str}


User Question:
--------------
{query_str}


Evaluation Criteria:

- Consider whether the document contains keywords or topics related to the user's question.
- The evaluation should not be overly stringent; the primary objective is to identify and filter out clearly irrelevant retrievals.


Decision:
- Assign a binary score to indicate the document's relevance.
- Use 'yes' if the document is relevant to the question, or 'no' if it is not.

Please provide your binary score ('yes' or 'no') below to indicate the document's relevance to the user question.

"""
) 



DEFAULT_TRANSFORM_QUERY_TEMPLATE = PromptTemplate(

template = """
Your task is to refine a query to ensure it is highly effective for retrieving relevant search results. \n
Analyze the given input to grasp the core semantic intent or meaning. \n

------- \n
{query_str}


\n ------- \n

Your goal is to rephrase or enhance this query to improve its search performance. Ensure the revised query is concise and directly aligned with the intended search objective. \n
Respond with the optimized query only: 


"""

)


class CorrectiveRAGWorkflow(Workflow):
    def __init__(self, index, linkup_api_key: str , llm: Optional[LLM] = None, **kwargs: Any ) -> None :

        super().__init__(**kwargs)
        self.index = index
        self.linkup_tool = LinkupToolSpec(api_key=linkup_api_key,
                                          depth="deep",
                                          output_type="searchResults", # or "sourcedAnswer" or "structured" 
                                        ) 
        self.llm = llm
    
    
        
       

                
                
                
                
                
    
        
        
        

        