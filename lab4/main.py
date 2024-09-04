import os

from langchain_core.documents import Document
from langchain_community.graphs import Neo4jGraph
from langchain_community.chat_models import ChatOllama
from langchain_experimental.graph_transformers import LLMGraphTransformer

os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "password"

llm = ChatOllama(model="llama3.1:latest", temperature=0)
graph = Neo4jGraph()

def create_graph():
    text = """
    Ivan Petrenko owns a Toyota Corolla, which was manufactured in 2020. The car is blue color and has a 1.8-liter gasoline engine. Ivan lives in Kyiv, at 12 Shevchenko Street. Ivan's Toyota Corolla is equipped with 16-inch winter tires.
    """
    documents = [Document(page_content=text)]
    llm_transformer_filtered = LLMGraphTransformer(
        llm=llm,
        allowed_nodes=["Person", "Car", "Location", "Part"],
        allowed_relationships=["OWNS", "ENGINE", "COLOR", "TIRES", "LIVES_IN"],
    )
    graph_documents_filtered = llm_transformer_filtered.convert_to_graph_documents(documents)
    graph.add_graph_documents(graph_documents_filtered)


create_graph()
