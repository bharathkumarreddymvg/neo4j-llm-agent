# 🧠 Neo4j LangChain Groq Chatbot

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.x-orange)](https://www.langchain.com/)
[![Neo4j](https://img.shields.io/badge/Database-Neo4j-008CC1.svg)](https://neo4j.com/)
[![Groq](https://img.shields.io/badge/LLM-Groq-black)](https://groq.com/)

---

## 📘 Overview

This project demonstrates an **AI-powered chatbot** built using **LangChain**, **Groq LLM**, and a **Neo4j Graph Database**.  
It allows users to ask **natural-language questions**, automatically generates **Cypher queries**, executes them on Neo4j, and displays both the **query** and **answer** in a sleek Streamlit interface.

> 🟢 **Live Demo:** [neo4j-llm-agent.streamlit.app](https://neo4j-llm-agent-0.streamlit.app/)

---

## 🎯 Objective

- Seamlessly integrate **Neo4j** with **LangChain** and **Groq LLM**
- Convert user queries into **Cypher** dynamically  
- Retrieve and visualize results directly from Neo4j  
- Serve as a foundation for **graph-driven conversational AI**

---

## 🧩 Key Features

✅ Natural language → Cypher query conversion  
✅ Real-time graph database interaction  
✅ Interactive Streamlit interface  
✅ Clean modular architecture  
✅ Simple environment configuration  

---

## 🗂️ Project Structure

├── app.py # Streamlit web application
├── experiment.ipynb # Data storage & retrieval in Neo4j
├── promptstrategies.ipynb # Query and prompt optimization
├── requirements.txt # Dependencies list
├── .env.example # Template for environment variables
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/neo4j-llm-agent.git
cd neo4j-llm-agent
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file in your project root:

bash
Copy code
NEO4J_URI=neo4j+s://<your-database-id>.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=<your-password>
GROQ_API_KEY=<your-groq-api-key>
5️⃣ Run the Application
bash
Copy code
streamlit run app.py
Then open your browser:
👉 http://localhost:8501
```
---

🔄 Workflow
1️⃣ Data Preparation
Use experiment.ipynb to create/import graph data into Neo4j and define nodes, relationships, and properties.

2️⃣ Query Optimization
promptstrategies.ipynb helps refine Cypher query generation and LLM prompt tuning.

3️⃣ Application Logic
app.py:

Connects to Neo4j

Initializes Groq LLM with LangChain

Builds a GraphCypherQAChain

Displays results in Streamlit

4️⃣ Execution Flow
User inputs a natural-language question.

LangChain + Groq generate the Cypher query.

Query executes on Neo4j.

Streamlit displays both query and answer.

🧠 Tech Stack
Component	Technology
Language	Python
Frontend Framework	Streamlit
Graph Database	Neo4j
LLM Provider	Groq
Framework	LangChain
Env Management	python-dotenv
Data Libraries	pandas, numpy

🌐 Deployment (Streamlit Cloud)
Push your project to GitHub.

Go to Streamlit Cloud.

Create a new app and select your repo.

Add credentials in App Settings → Secrets:

toml
Copy code
NEO4J_URI="neo4j+s://<your-database-id>.databases.neo4j.io"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="<your-password>"
GROQ_API_KEY="<your-groq-api-key>"
Deploy 🚀 — Streamlit will build and host automatically.

✅ Deployed App: https://neo4j-llm-agent-0.streamlit.app/

📸 Demo Screenshot
(Optional: Add a UI screenshot for better presentation)

scss
Copy code
![Chatbot Demo](assets/demo.png)
🧑‍💻 Author
Bharath Kumar Reddy
📍 India
💼 Data Science & AI Enthusiast
🔗 GitHub

🤝 Contribution Guidelines
Contributions, issues, and feature requests are welcome!

Fork the repository

Create a feature branch:

bash
Copy code
git checkout -b feature/your-feature
Commit your changes:

bash
Copy code
git commit -m 'Add new feature'
Push to your branch and open a Pull Request

📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it for personal or educational purposes.
