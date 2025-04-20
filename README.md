
## Repository Overview
### 🤖 AI Agents with LangChain & LangGraph
This repository contains multiple AI agent implementations leveraging the LangChain and LangGraph frameworks to demonstrate advanced LLM‑based workflows.

## Table of Contents

- [Technologies](#technologies)  
- [Project Structure](#project-structure)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

## 🌟Technologies

- **LangChain**: a framework for developing applications powered by LLMs, simplifying every stage of the LLM application lifecycle.  
- **LangGraph**: a low‑level orchestration framework for building controllable, stateful agent workflows with multi‑agent support.  
- **FastAPI**: for building high‑performance asynchronous APIs.  
- **Streamlit**: for creating interactive web UIs for experimentation and demos.  
- **ChatGoogleGenerativeAI (Gemini 2.0 Flash)**: Google’s generative AI model integrated via LangChain.  
- **Ollama LLM (llama3.2:1b)**: local Llama 3 model powered by Ollama.  
- **Pinecone**: vector database for retrieval‑augmented generation (RAG) pipelines.  
- **GroQ**: an end‑to‑end AI pipeline tool integrated in LangChain workflows.  
- **Hugging Face**: model hub integration for custom LLMs and embeddings.  
- **dotenv**: for managing environment variables.  
- **LangServe**: deploys LangChain pipelines as production‑ready APIs.  

## 📁Project Structure

- **`chain_yt/`**  
  Jupyter notebooks demonstrating LangChain‑based agents for YouTube video processing, covering Q&A, retrieval‑augmented generation (RAG), custom agent composition, function calling, GroQ pipeline integration, Hugging Face model usage, memory‑based retrieval, and Pinecone vector store indexing capabilities.

- **`graph_yt/`**  
  LangGraph workflows for structured YouTube data processing, including single‑agent and multi‑agent graph definitions, RAG graph pipelines, exam simulation flows, and custom bot implementations under the `Bots/` directory.

- **`project1/`**  
  A full‑stack AI chatbot application:  
  - **`api/`**  
    - `app.py`: FastAPI app exposing `/gemini`, `/essay`, and `/poem` routes via `add_routes`, wiring LangChain prompt templates to ChatGoogleGenerativeAI and OllamaLLM backends.  
    - `client.py`: Streamlit client for interacting with the `/gemini` endpoint.  

  - **`chatbot/`**  
    - `app.py`: Gemini‑powered Streamlit chatbot using LangChain prompt templates and output parsers.  
    - `localama.py`: Local Ollama Llama 3 Streamlit chatbot showcasing an entirely on‑device pipeline.  

The repository is organized to facilitate exploration and extension, with clear module boundaries and modular examples.

## 🚀Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/devagn611/AI-Agents.git
   cd AI-Agents
   ```

2. **Create a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Copy `.env.example` to `.env` and fill in your API keys for Google, LangChain, LangSmith, etc.

## 📚Usage

### Running the Jupyter Notebooks

Navigate to any folder under `chain_yt/` or `graph_yt/` and launch:
```bash
jupyter notebook
```

### Launching the API

```bash
cd project1/api
uvicorn app:app --reload
```
- Access `/gemini`, `/essay`, and `/poem` endpoints at `http://localhost:8000/`.

### Starting the Streamlit UIs

```bash
cd project1/api
streamlit run client.py

cd project1/chatbot
streamlit run app.py
# or
streamlit run localama.py
```

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and open a pull request. Ensure all new code is covered by appropriate documentation or tests.

## 📜License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📧Contact

For questions or feedback, please open an issue or reach out via email:  
devagnmaniya611@gmail.com
