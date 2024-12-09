from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.storage.agent.postgres import PgAgentStorage
from phi.vectordb.pgvector import PgVector, SearchType
from phi.playground import Playground, serve_playground_app


from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()



openai_api_key = os.getenv("gpt")


# 1. Traditional RAG -----------------------------------------------------------------



db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(
        table_name="recipes",
        db_url=db_url,
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(model="text-embedding-3-small", api_key=openai_api_key)
    ),
)

knowledge_base.load(upsert=True)

# agent = Agent(
#     model=OpenAIChat(id="gpt-4o-mini", api_key=openai_api_key),
#     knowledge=knowledge_base,
#     add_context=True,
#     search_knowledge=True,
#     markdown=True,
# )

# agent.print_response(
#     "Hi, i want to make a 3 course meal. Can you recommend some recipes. "
#     "I'd like to start with a soup, then im thinking a thai curry for the main course "
#     "and finish with a dessert",
#     stream=True
# )


# 1. Traditional RAG -----------------------------------------------------------------



# 2. Agentic RAG ******************************************************************


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini", api_key=openai_api_key),
    knowledge=knowledge_base,
    search_knowledge=True,
    show_tool_calls=True,
    markdown=True,
)
agent.print_response(
    "Hi, i want to make a 3 course meal. Can you recommend some recipes. "
    "I'd like to start with a soup, then im thinking a thai curry for the main course "
    "and finish with a dessert",
    stream=True
)


# 2. Agentic RAG ******************************************************************




# # 3. UI
# rag_agent = Agent(
#     name="RAG Agent",
#     agent_id="rag-agent",
#     model=OpenAIChat(id="gpt-4o-mini", api_key=openai_api_key),
#     knowledge=knowledge_base,
#     search_knowledge=True,
#     read_chat_history=True,
#     storage=PgAgentStorage(table_name="rag_agent_sessions", db_url=db_url),
#     instructions=[
#         "Always search your knowledge base first and use it if available.",
#         "Share the page number or source URL of the information you used in your response.",
#         "If health benefits are mentioned, include them in the response.",
#         "Important: Use tables where possible.",
#     ],
#     markdown=True,
# )
# app = Playground(agents=[rag_agent]).get_app()
# if __name__ == "__main__":
#     knowledge_base.load(upsert=True)
#     serve_playground_app(app)