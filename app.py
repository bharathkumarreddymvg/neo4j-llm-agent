import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chains import GraphCypherQAChain
from langchain_groq import ChatGroq

# Try importing Neo4jGraph from correct module
try:
    from langchain_community.graphs import Neo4jGraph
except ImportError:
    from langchain.graphs import Neo4jGraph

# Load environment variables
load_dotenv()

# Neo4j and Groq credentials
NEO4J_URI = os.getenv("NEO4J_URI") or "neo4j+s://<your-database-id>.databases.neo4j.io"
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME") or "neo4j"
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD") or "<your-password>"
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or "<your-groq-api-key>"

# Streamlit UI
st.set_page_config(page_title="Neo4j LangChain Chat", layout="centered")
st.title("Neo4j LangChain Groq Chatbot")
st.markdown("Ask natural-language questions about your Neo4j graph database and view the generated Cypher query.")

# Connect to Neo4j
try:
    graph = Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD
    )
    graph.refresh_schema()
    st.success("Connected to Neo4j successfully.")
except Exception as e:
    st.error(f"Error connecting to Neo4j: {e}")
    st.stop()

# Initialize Groq LLM
try:
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.1-8b-instant"
    )
    st.success("Groq LLM initialized.")
except Exception as e:
    st.error(f"Error initializing Groq LLM: {e}")
    st.stop()

# Create GraphCypherQAChain with intermediate steps enabled
chain = GraphCypherQAChain.from_llm(
    llm=llm,
    graph=graph,
    verbose=True,
    allow_dangerous_requests=True,
    return_intermediate_steps=True
)

# User Input
query = st.text_input("Enter your question about the graph data:")

# Button to Run
if st.button("Run Query"):
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Generating Cypher query and fetching results..."):
            try:
                result = chain.invoke({"query": query})

                # Extract Answer
                answer = result.get("result", "No response.")
                st.subheader("Answer")
                st.write(answer)

                # Extract and show Cypher Query
                cypher_query = None
                intermediate_steps = result.get("intermediate_steps", [])
                if intermediate_steps:
                    for step in intermediate_steps:
                        if isinstance(step, dict) and "query" in step:
                            cypher_query = step["query"]
                            break

                if cypher_query:
                    st.subheader("Generated Cypher Query")
                    st.code(cypher_query, language="cypher")
                else:
                    st.info("No Cypher query found in the response.")

            except Exception as e:
                st.error(f"Error: {e}")

# Show Graph Schema below
st.divider()
st.subheader("Graph Schema")
try:
    st.code(graph.schema)
except:
    st.info("Schema not available.")
