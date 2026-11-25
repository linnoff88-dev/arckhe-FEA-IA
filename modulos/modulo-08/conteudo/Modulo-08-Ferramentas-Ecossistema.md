# Módulo 8: Ferramentas e Ecossistema

## Dominando o Universo de Ferramentas para Agentes de IA

> "Um artesêo é têo bom quanto suas ferramentas. Um engenheiro de agentes é têo produtivo quanto seu conhecimento do ecossistema." - Princípio da Maestria em Ferramentas

---

## 📋 Índice

1. [Introduçêo ao Ecossistema](#81-introduçêo-ao-ecossistema)
2. [Ferramentas de Desenvolvimento](#82-ferramentas-de-desenvolvimento)
3. [Bibliotecas Essenciais](#83-bibliotecas-essenciais)
4. [Interfaces de Usuário](#84-interfaces-de-usuário)
5. [Integrações com APIs](#85-integrações-com-apis)
6. [Ferramentas de Debugging e Profiling](#86-ferramentas-de-debugging-e-profiling)
7. [Analytics e Business Intelligence](#87-analytics-e-business-intelligence)
8. [Ferramentas de Testes](#88-ferramentas-de-testes)
9. [Recursos da Comunidade](#89-recursos-da-comunidade)
10. [Projeto Prático: Painel de Controle Universal](#810-projeto-prático)
11. [Resumo e Próximos Passos](#811-resumo-e-próximos-passos)

---

## 8.1 Introduçêo ao Ecossistema

### 8.1.1 O Ecossistema de Agentes de IA

```
┌─────────────────────────────────────────────────────────────┐
│                  AI AGENTS ECOSYSTEM                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │               CORE FRAMEWORKS                        │  │
│  │  LangChain · Agno · CrewAI · AutoGen · Semantic K  │  │
│  └──────────────────────────────────────────────────────┘  │
│                            │                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │            PROTOCOLS & STANDARDS                     │  │
│  │         MCP · OpenAI Function Calling · Tools       │  │
│  └──────────────────────────────────────────────────────┘  │
│                            │                                │
│  ┌──────────────────────────┬──────────────────────────┐   │
│  │                          │                          │   │
│  ▼                          ▼                          ▼   │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐         │
│  │   UI     │      │ Utilities│      │Analytics │         │
│  │Streamlit │      │ Jupyter  │      │ LangSmith│         │
│  │ Gradio   │      │ Logging  │      │ Weights&B│         │
│  └──────────┘      └──────────┘      └──────────┘         │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              INFRASTRUCTURE                         │   │
│  │   Docker · Kubernetes · Redis · PostgreSQL         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 8.1.2 Categorias de Ferramentas

**1. Desenvolvimento**
- IDEs e editores (VS Code, Cursor, PyCharm)
- Notebooks (Jupyter, Google Colab)
- Version control (Git, GitHub)

**2. Frameworks e Bibliotecas**
- Agent frameworks (LangChain, Agno, CrewAI)
- LLM providers (Anthropic, OpenAI, Cohere)
- Vector databases (Pinecone, Weaviate, ChromaDB)

**3. UI e Visualizaçêo**
- Streamlit, Gradio, Chainlit
- Dash, Plotly
- Custom frontends (React, Vue)

**4. Observabilidade**
- LangSmith, Weights & Biases
- Prometheus, Grafana
- Sentry, DataDog

**5. Dados e Storage**
- PostgreSQL, MongoDB
- Redis, Memcached
- S3, MinIO

---

## 8.2 Ferramentas de Desenvolvimento

### 8.2.1 IDEs e Editores

**VS Code com Extensões Essenciais:**

```json
// .vscode/extensions.json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "github.copilot",
    "ms-azuretools.vscode-docker",
    "redhat.vscode-yaml",
    "tamasfe.even-better-toml",
    "charliermarsh.ruff"
  ]
}
```

**Configuraçêo recomendada:**

```json
// .vscode/settings.json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.ruffEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

**Cursor AI (IDE com IA integrada):**

```python
# Uso do Cursor para gerar código de agentes
# 1. Abra o Cursor
# 2. Ctrl+K para abrir o chat
# 3. Digite: "Create an Agno agent that analyzes customer feedback"
# 4. O Cursor gera o código diretamente no editor
```

### 8.2.2 Jupyter Notebooks

**Setup otimizado:**

```python
# Instalar kernel com ambiente virtual
python -m ipykernel install --user --name=agent-env --display-name="Python (Agent Env)"

# Magic commands úteis
%load_ext autoreload
%autoreload 2  # Auto-reload de módulos modificados

# Timing
%time result = agent.run("test")  # Tempo de uma célula
%timeit agent.run("test")  # Benchmark

# Profiling
%prun agent.run("long task")  # Profile detalhado

# Debug
%debug  # Ativar debugger após exception

# Plotting inline
%matplotlib inline
import matplotlib.pyplot as plt
```

**Template de notebook para agentes:**

```python
# =============================================================================
# CELL 1: Setup
# =============================================================================
import os
from dotenv import load_dotenv
from agno import Agent
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

# =============================================================================
# CELL 2: Configuraçêo do Agente
# =============================================================================
agent = Agent(
    name="Research Assistant",
    model="claude-3-7-sonnet-20250219",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    show_tool_calls=True
)

# =============================================================================
# CELL 3: Definir Ferramentas
# =============================================================================
def search_web(query: str) -> str:
    """Busca informações na web"""
    # Implementaçêo
    pass

agent.tools = [search_web]

# =============================================================================
# CELL 4: Testes Interativos
# =============================================================================
response = agent.run("What is the latest news on AI agents?")
print(response)

# =============================================================================
# CELL 5: Análise de Resultados
# =============================================================================
# Visualizar métricas, tokens usados, etc.
```

### 8.2.3 Ambiente de Desenvolvimento

**pyproject.toml (gerenciamento moderno de dependências):**

```toml
[project]
name = "my-agent-project"
version = "0.1.0"
description = "Production-ready AI agent system"
requires-python = ">=3.11"

dependencies = [
    "agno>=0.1.0",
    "anthropic>=0.18.0",
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "pydantic>=2.6.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "pytest-cov>=4.1.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.8.0",
]

ui = [
    "streamlit>=1.30.0",
    "gradio>=4.0.0",
]

monitoring = [
    "prometheus-client>=0.19.0",
    "opentelemetry-api>=1.22.0",
]

[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.black]
line-length = 100
target-version = ['py311']

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

**Makefile para automaçêo:**

```makefile
.PHONY: install dev test lint format clean docker-build run

install:
	pip install -e .

dev:
	pip install -e ".[dev,ui,monitoring]"

test:
	pytest tests/ -v --cov=app --cov-report=html

lint:
	ruff check app/ tests/
	mypy app/

format:
	black app/ tests/
	ruff check --fix app/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov

docker-build:
	docker build -t my-agent:latest .

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Uso:**

```bash
make dev      # Instalar dependências de desenvolvimento
make test     # Rodar testes
make format   # Formatar código
make run      # Iniciar aplicaçêo
```

---

## 8.3 Bibliotecas Essenciais

### 8.3.1 Processamento de Dados

**Pandas para análise de conversas:**

```python
import pandas as pd
from datetime import datetime

# Carregar histórico de conversas
conversations = [
    {"user_id": "u1", "message": "Hello", "response": "Hi!", "tokens": 10, "cost": 0.001, "timestamp": datetime(2025,1,1,10,0)},
    {"user_id": "u1", "message": "Help me", "response": "Sure!", "tokens": 15, "cost": 0.002, "timestamp": datetime(2025,1,1,10,5)},
    # ...
]

df = pd.DataFrame(conversations)

# Análises
print(df.groupby('user_id')['tokens'].sum())  # Tokens por usuário
print(df.groupby('user_id')['cost'].sum())    # Custo por usuário
print(df.resample('H', on='timestamp')['tokens'].sum())  # Tokens por hora

# Identificar usuários heavy
heavy_users = df.groupby('user_id').agg({
    'tokens': 'sum',
    'cost': 'sum',
    'message': 'count'
}).sort_values('cost', ascending=False).head(10)

print(heavy_users)
```

**NumPy para embeddings:**

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Embeddings de documentos
embeddings = np.array([
    [0.1, 0.2, 0.3, ...],  # doc1
    [0.15, 0.25, 0.35, ...],  # doc2
    # ...
])

# Encontrar documentos similares
query_embedding = np.array([0.12, 0.22, 0.32, ...])

similarities = cosine_similarity([query_embedding], embeddings)[0]
most_similar_idx = np.argsort(similarities)[::-1][:5]  # Top 5

print("Documentos mais similares:", most_similar_idx)
```

### 8.3.2 Validaçêo de Dados

**Pydantic para validaçêo robusta:**

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, Literal
from datetime import datetime

class AgentRequest(BaseModel):
    """Schema de requisiçêo para o agente"""

    message: str = Field(..., min_length=1, max_length=10000)
    user_id: str = Field(..., regex=r'^[a-zA-Z0-9_-]+$')
    context: Optional[dict] = None
    max_tokens: int = Field(default=1000, ge=100, le=4000)
    temperature: float = Field(default=0.7, ge=0.0, le=1.0)
    model: Literal["haiku", "sonnet", "opus"] = "sonnet"

    @validator('message')
    def sanitize_message(cls, v):
        """Remove caracteres de controle"""
        import re
        return re.sub(r'[\x00-\x1F\x7F]', '', v)

    @validator('context')
    def validate_context(cls, v):
        """Limita tamanho do contexto"""
        if v and len(str(v)) > 5000:
            raise ValueError("Context too large")
        return v

# Uso
try:
    request = AgentRequest(
        message="Hello, agent!",
        user_id="user123",
        temperature=0.8
    )
    print(request.dict())
except ValidationError as e:
    print(e.json())
```

### 8.3.3 Requisições HTTP

**httpx (async requests):**

```python
import httpx
import asyncio

async def fetch_multiple_apis():
    """Buscar dados de múltiplas APIs em paralelo"""

    async with httpx.AsyncClient(timeout=10.0) as client:
        # Fazer requisições em paralelo
        tasks = [
            client.get("https://api1.example.com/data"),
            client.get("https://api2.example.com/data"),
            client.get("https://api3.example.com/data"),
        ]

        responses = await asyncio.gather(*tasks, return_exceptions=True)

        results = []
        for response in responses:
            if isinstance(response, Exception):
                print(f"Error: {response}")
                continue

            if response.status_code == 200:
                results.append(response.json())

        return results

# Uso
results = asyncio.run(fetch_multiple_apis())
```

### 8.3.4 Cache e Performance

**cachetools para memoizaçêo:**

```python
from cachetools import cached, TTLCache, LRUCache
import time

# Cache com TTL (expira após X segundos)
@cached(cache=TTLCache(maxsize=1000, ttl=3600))
def get_embedding(text: str):
    """Cache de embeddings por 1 hora"""
    # Operaçêo cara
    time.sleep(0.5)
    return generate_embedding(text)

# Cache LRU (Least Recently Used)
@cached(cache=LRUCache(maxsize=500))
def get_user_profile(user_id: str):
    """Cache dos últimos 500 perfis acessados"""
    return db.query(User).filter(User.id == user_id).first()

# Cache personalizado com Redis
from redis import Redis
import json

redis_client = Redis(host='localhost', port=6379, decode_responses=True)

def redis_cache(ttl: int = 3600):
    """Decorator para cache com Redis"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Criar chave do cache
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"

            # Tentar buscar do cache
            cached_value = redis_client.get(cache_key)
            if cached_value:
                return json.loads(cached_value)

            # Nêo encontrado - executar funçêo
            result = func(*args, **kwargs)

            # Salvar no cache
            redis_client.setex(cache_key, ttl, json.dumps(result))

            return result
        return wrapper
    return decorator

@redis_cache(ttl=7200)
def expensive_computation(param: str):
    """Cacheado por 2 horas no Redis"""
    # Computaçêo cara
    pass
```

### 8.3.5 Utilitários Python

**python-dotenv para configuraçêo:**

```python
from dotenv import load_dotenv, find_dotenv
import os

# Carregar .env automaticamente
load_dotenv(find_dotenv())

# Acessar variáveis com fallback
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "default-key")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Validar que variáveis críticas estêo definidas
required_vars = ["ANTHROPIC_API_KEY", "DATABASE_URL"]
missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
```

**loguru para logging simplificado:**

```python
from loguru import logger
import sys

# Configuraçêo básica
logger.remove()  # Remover handler padrêo

# Console com cores
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

# Arquivo com rotaçêo
logger.add(
    "logs/app_{time:YYYY-MM-DD}.log",
    rotation="1 day",
    retention="7 days",
    compression="zip",
    level="DEBUG"
)

# Uso
logger.info("Agent started")
logger.debug("Processing message: {}", message)
logger.error("Failed to process: {}", error)

# Contexto adicional
logger.bind(user_id="u123", request_id="r456").info("Processing request")

# Decorators
@logger.catch  # Automatically log exceptions
def process_with_agent(message: str):
    # Se exception ocorrer, será logada automaticamente
    return agent.run(message)
```

---

## 8.4 Interfaces de Usuário

### 8.4.1 Streamlit

**App básico:**

```python
# app.py
import streamlit as st
from agno import Agent
import os

st.set_page_config(page_title="AI Agent Chat", page_icon="🤖", layout="wide")

# Título
st.title("🤖 AI Agent Assistant")

# Sidebar para configurações
with st.sidebar:
    st.header("⚙️ Settings")

    model = st.selectbox(
        "Model",
        ["claude-3-haiku-20240307", "claude-3-7-sonnet-20250219", "claude-3-opus-20240229"]
    )

    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)

    max_tokens = st.number_input("Max Tokens", 100, 4000, 1000, 100)

    st.divider()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Inicializar agente
if 'agent' not in st.session_state:
    st.session_state.agent = Agent(
        name="Assistant",
        model=model,
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        show_tool_calls=True
    )

# Histórico de mensagens
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Exibir histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Type your message..."):
    # Adicionar mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Processar com agente
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.run(prompt)
            st.markdown(response)

    # Adicionar resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": response})

# Métricas na sidebar
with st.sidebar:
    st.divider()
    st.header("📊 Stats")

    total_messages = len(st.session_state.messages)
    st.metric("Total Messages", total_messages)

    if hasattr(st.session_state.agent, 'total_tokens'):
        st.metric("Total Tokens", st.session_state.agent.total_tokens)
```

**Executar:**

```bash
streamlit run app.py
```

**Features avançadas do Streamlit:**

```python
# Tabs
tab1, tab2, tab3 = st.tabs(["Chat", "Analytics", "Settings"])

with tab1:
    # Chat interface
    pass

with tab2:
    # Analytics dashboard
    import pandas as pd
    import plotly.express as px

    # Gráfico de uso ao longo do tempo
    df = pd.DataFrame(conversation_history)
    fig = px.line(df, x='timestamp', y='tokens', title='Token Usage Over Time')
    st.plotly_chart(fig)

with tab3:
    # Advanced settings
    pass

# Expanders para organizaçêo
with st.expander("Advanced Options"):
    system_prompt = st.text_area("System Prompt", height=150)
    enable_memory = st.checkbox("Enable Conversation Memory")

# Progress bars
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)

# Status indicators
st.success("Agent ready!")
st.info("Processing your request...")
st.warning("High token usage detected")
st.error("API rate limit exceeded")

# File uploads
uploaded_file = st.file_uploader("Upload a document", type=['pdf', 'txt', 'docx'])
if uploaded_file:
    content = uploaded_file.read()
    # Process with agent
```

### 8.4.2 Gradio

**Interface básica:**

```python
# gradio_app.py
import gradio as gr
from agno import Agent
import os

agent = Agent(
    name="Assistant",
    model="claude-3-7-sonnet-20250219",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def chat(message, history):
    """Funçêo de chat"""
    # history é uma lista de tuplas (user_msg, bot_msg)
    response = agent.run(message)
    return response

# Interface Gradio
demo = gr.ChatInterface(
    fn=chat,
    title="🤖 AI Agent Chat",
    description="Chat with an intelligent AI agent powered by Claude",
    theme=gr.themes.Soft(),
    examples=[
        "What is the capital of France?",
        "Explain quantum computing in simple terms",
        "Write a Python function to calculate fibonacci numbers"
    ],
    cache_examples=False,
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
```

**Interface avançada com múltiplos componentes:**

```python
import gradio as gr

def analyze_document(file, analysis_type, temperature):
    """Analisa documento enviado"""
    # Ler arquivo
    content = file.read().decode('utf-8')

    # Processar com agente
    prompt = f"Analyze this document with focus on {analysis_type}:\n\n{content}"

    agent = Agent(
        model="claude-3-7-sonnet-20250219",
        temperature=temperature
    )

    response = agent.run(prompt)

    return response

with gr.Blocks(theme=gr.themes.Base()) as demo:
    gr.Markdown("# 📄 Document Analysis Agent")

    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="Upload Document", file_types=['.txt', '.md'])

            analysis_type = gr.Dropdown(
                choices=["Summary", "Key Points", "Sentiment", "Entities"],
                label="Analysis Type",
                value="Summary"
            )

            temperature = gr.Slider(
                minimum=0.0,
                maximum=1.0,
                value=0.7,
                step=0.1,
                label="Temperature"
            )

            submit_btn = gr.Button("Analyze", variant="primary")

        with gr.Column(scale=2):
            output = gr.Textbox(
                label="Analysis Result",
                lines=20,
                interactive=False
            )

    submit_btn.click(
        fn=analyze_document,
        inputs=[file_input, analysis_type, temperature],
        outputs=output
    )

    gr.Examples(
        examples=[
            ["example1.txt", "Summary", 0.7],
            ["example2.txt", "Key Points", 0.5],
        ],
        inputs=[file_input, analysis_type, temperature]
    )

demo.launch()
```

### 8.4.3 Chainlit

**Interface de chat conversacional:**

```python
# chainlit_app.py
import chainlit as cl
from agno import Agent

@cl.on_chat_start
async def start():
    """Inicializaçêo quando chat começa"""

    # Criar agente
    agent = Agent(
        name="Assistant",
        model="claude-3-7-sonnet-20250219"
    )

    # Salvar no contexto da sessêo
    cl.user_session.set("agent", agent)

    # Mensagem de boas-vindas
    await cl.Message(
        content="👋 Hello! I'm your AI assistant. How can I help you today?"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    """Processar mensagem do usuário"""

    # Recuperar agente
    agent = cl.user_session.get("agent")

    # Mostrar indicador de "typing"
    async with cl.Step(name="Thinking") as step:
        response = agent.run(message.content)
        step.output = response

    # Enviar resposta
    await cl.Message(content=response).send()

@cl.on_chat_end
async def end():
    """Cleanup quando chat termina"""
    print("Chat session ended")
```

**Executar:**

```bash
chainlit run chainlit_app.py -w
```

---

## 8.5 Integrações com APIs

### 8.5.1 APIs Populares

**1. GitHub API:**

```python
import requests
from typing import List, Dict

class GitHubTool:
    """Ferramenta para interagir com GitHub"""

    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def search_repositories(self, query: str, limit: int = 10) -> List[Dict]:
        """Busca repositórios"""
        response = requests.get(
            f"{self.base_url}/search/repositories",
            headers=self.headers,
            params={"q": query, "per_page": limit}
        )
        response.raise_for_status()

        repos = response.json()['items']
        return [{
            'name': repo['name'],
            'url': repo['html_url'],
            'stars': repo['stargazers_count'],
            'description': repo['description']
        } for repo in repos]

    def create_issue(self, owner: str, repo: str, title: str, body: str) -> Dict:
        """Cria uma issue"""
        response = requests.post(
            f"{self.base_url}/repos/{owner}/{repo}/issues",
            headers=self.headers,
            json={"title": title, "body": body}
        )
        response.raise_for_status()
        return response.json()

    def get_pull_requests(self, owner: str, repo: str, state: str = "open") -> List[Dict]:
        """Lista pull requests"""
        response = requests.get(
            f"{self.base_url}/repos/{owner}/{repo}/pulls",
            headers=self.headers,
            params={"state": state}
        )
        response.raise_for_status()
        return response.json()

# Uso com agente
from agno import Agent

github = GitHubTool(token=os.getenv("GITHUB_TOKEN"))

def search_repos(query: str) -> str:
    """Busca repositórios no GitHub"""
    repos = github.search_repositories(query, limit=5)
    result = f"Found {len(repos)} repositories:\n\n"
    for repo in repos:
        result += f"- {repo['name']} ({repo['stars']} ⭐)\n  {repo['url']}\n"
    return result

agent = Agent(
    name="GitHub Assistant",
    tools=[search_repos]
)

response = agent.run("Find popular Python AI agent frameworks on GitHub")
```

**2. Slack API:**

```python
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackTool:
    """Ferramenta para interagir com Slack"""

    def __init__(self, token: str):
        self.client = WebClient(token=token)

    def send_message(self, channel: str, text: str) -> str:
        """Envia mensagem para um canal"""
        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=text
            )
            return f"Message sent to {channel}"
        except SlackApiError as e:
            return f"Error: {e.response['error']}"

    def list_channels(self) -> List[str]:
        """Lista canais disponíveis"""
        try:
            response = self.client.conversations_list()
            channels = [ch['name'] for ch in response['channels']]
            return channels
        except SlackApiError as e:
            return []

    def get_channel_history(self, channel: str, limit: int = 10) -> List[Dict]:
        """Busca histórico de mensagens"""
        try:
            response = self.client.conversations_history(
                channel=channel,
                limit=limit
            )
            return response['messages']
        except SlackApiError as e:
            return []

# Integrar com agente
slack = SlackTool(token=os.getenv("SLACK_BOT_TOKEN"))

def notify_team(message: str) -> str:
    """Notifica o time via Slack"""
    return slack.send_message(channel="#general", text=message)

agent = Agent(
    name="Slack Assistant",
    tools=[notify_team]
)
```

**3. Google Calendar API:**

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

class GoogleCalendarTool:
    """Ferramenta para Google Calendar"""

    def __init__(self, credentials_path: str):
        creds = Credentials.from_authorized_user_file(credentials_path)
        self.service = build('calendar', 'v3', credentials=creds)

    def create_event(
        self,
        summary: str,
        start_time: datetime,
        duration_minutes: int = 60,
        description: str = ""
    ) -> str:
        """Cria um evento no calendário"""

        end_time = start_time + timedelta(minutes=duration_minutes)

        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': 'America/Sao_Paulo',
            },
        }

        event = self.service.events().insert(
            calendarId='primary',
            body=event
        ).execute()

        return f"Event created: {event.get('htmlLink')}"

    def list_upcoming_events(self, days: int = 7) -> List[Dict]:
        """Lista eventos próximos"""

        now = datetime.utcnow().isoformat() + 'Z'
        end = (datetime.utcnow() + timedelta(days=days)).isoformat() + 'Z'

        events_result = self.service.events().list(
            calendarId='primary',
            timeMin=now,
            timeMax=end,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])

        return [{
            'summary': event['summary'],
            'start': event['start'].get('dateTime', event['start'].get('date')),
            'end': event['end'].get('dateTime', event['end'].get('date'))
        } for event in events]
```

### 8.5.2 Wrappers de API Genéricos

**Cliente HTTP reutilizável:**

```python
import httpx
from typing import Optional, Dict, Any
import json

class APIClient:
    """Cliente genérico para APIs REST"""

    def __init__(
        self,
        base_url: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: float = 30.0
    ):
        self.base_url = base_url.rstrip('/')
        self.headers = headers or {}
        self.timeout = timeout

    async def request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        json_data: Optional[Dict] = None,
        data: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Faz uma requisiçêo HTTP"""

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.request(
                method=method,
                url=url,
                headers=self.headers,
                params=params,
                json=json_data,
                data=data
            )

            response.raise_for_status()

            return response.json()

    async def get(self, endpoint: str, params: Optional[Dict] = None):
        return await self.request("GET", endpoint, params=params)

    async def post(self, endpoint: str, json_data: Optional[Dict] = None):
        return await self.request("POST", endpoint, json_data=json_data)

    async def put(self, endpoint: str, json_data: Optional[Dict] = None):
        return await self.request("PUT", endpoint, json_data=json_data)

    async def delete(self, endpoint: str):
        return await self.request("DELETE", endpoint)

# Uso
api = APIClient(
    base_url="https://api.example.com",
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)

result = await api.get("/users", params={"limit": 10})
```

---

## 8.6 Ferramentas de Debugging e Profiling

### 8.6.1 Debugging com pdb

```python
import pdb

def complex_agent_logic(message: str):
    """Funçêo com lógica complexa"""

    # Ponto de breakpoint
    pdb.set_trace()  # Execuçêo pausa aqui

    # Comandos úteis no pdb:
    # n (next): próxima linha
    # s (step): entrar em funçêo
    # c (continue): continuar execuçêo
    # p variable: imprimir variável
    # l (list): mostrar código ao redor
    # q (quit): sair

    processed = preprocess(message)
    response = agent.run(processed)

    return response

# Alternativa moderna: breakpoint() (Python 3.7+)
def modern_debug():
    value = calculate_something()
    breakpoint()  # Pausa aqui
    return value
```

### 8.6.2 Profiling de Performance

**cProfile para identificar gargalos:**

```python
import cProfile
import pstats
from pstats import SortKey

def profile_agent():
    """Profile do agente"""

    profiler = cProfile.Profile()
    profiler.enable()

    # Código a ser profileado
    for i in range(100):
        agent.run(f"Test message {i}")

    profiler.disable()

    # Salvar resultados
    profiler.dump_stats('agent_profile.prof')

    # Imprimir estatísticas
    stats = pstats.Stats(profiler)
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(20)  # Top 20 funções mais lentas

# Alternativa: line_profiler para profiling linha por linha
from line_profiler import LineProfiler

def profile_function():
    lp = LineProfiler()
    lp.add_function(agent.run)

    lp_wrapper = lp(agent.run)
    lp_wrapper("Test message")

    lp.print_stats()
```

**memory_profiler para uso de memória:**

```python
from memory_profiler import profile

@profile
def memory_intensive_function():
    """Funçêo que usa muita memória"""

    # Carregar modelo grande
    large_data = load_large_model()

    # Processar
    results = process_data(large_data)

    return results

# Executar com: python -m memory_profiler script.py
```

### 8.6.3 LangSmith para Debugging de Agentes

```python
import os
from langsmith import Client
from langsmith.run_helpers import traceable

# Configurar LangSmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-api-key"
os.environ["LANGCHAIN_PROJECT"] = "my-agent-project"

client = Client()

@traceable(name="agent_run")
def run_agent_with_tracing(message: str):
    """Executa agente com tracing completo"""

    # Preprocessamento
    with traceable(name="preprocess"):
        processed = preprocess_message(message)

    # Executar agente
    with traceable(name="llm_call"):
        response = agent.run(processed)

    # Post-processing
    with traceable(name="postprocess"):
        final_response = postprocess_response(response)

    return final_response

# Visualizar traces em https://smith.langchain.com/
```

### 8.6.4 Sentry para Error Tracking

```python
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

# Inicializar Sentry
sentry_sdk.init(
    dsn="https://your-sentry-dsn@sentry.io/project-id",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    integrations=[
        LoggingIntegration(
            level=logging.INFO,
            event_level=logging.ERROR
        )
    ],
    environment="production"
)

# Capturar exceções automaticamente
def process_message(message: str):
    try:
        response = agent.run(message)
        return response
    except Exception as e:
        # Automaticamente enviado para Sentry
        sentry_sdk.capture_exception(e)
        raise

# Adicionar contexto
with sentry_sdk.configure_scope() as scope:
    scope.set_user({"id": "user123", "email": "user@example.com"})
    scope.set_tag("agent_version", "1.0.0")
    scope.set_context("request", {
        "message_length": len(message),
        "timestamp": datetime.now().isoformat()
    })

# Breadcrumbs para rastrear fluxo
sentry_sdk.add_breadcrumb(
    category='agent',
    message='Processing user message',
    level='info'
)
```

---

## 8.7 Analytics e Business Intelligence

### 8.7.1 Métricas de Negócio

```python
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List
import pandas as pd

@dataclass
class ConversationMetrics:
    """Métricas de uma conversa"""
    conversation_id: str
    user_id: str
    messages_count: int
    total_tokens: int
    total_cost_usd: float
    duration_seconds: float
    satisfaction_score: float  # 1-5
    goal_achieved: bool
    timestamp: datetime

class AgentAnalytics:
    """Analytics para sistema de agentes"""

    def __init__(self, db_connection):
        self.db = db_connection

    def get_daily_metrics(self, date: datetime) -> dict:
        """Métricas do dia"""

        metrics = self.db.query(ConversationMetrics).filter(
            ConversationMetrics.timestamp >= date,
            ConversationMetrics.timestamp < date + timedelta(days=1)
        ).all()

        df = pd.DataFrame([m.__dict__ for m in metrics])

        return {
            "total_conversations": len(df),
            "unique_users": df['user_id'].nunique(),
            "avg_messages_per_conversation": df['messages_count'].mean(),
            "total_tokens": df['total_tokens'].sum(),
            "total_cost_usd": df['total_cost_usd'].sum(),
            "avg_satisfaction": df['satisfaction_score'].mean(),
            "goal_achievement_rate": df['goal_achieved'].mean(),
            "avg_duration_seconds": df['duration_seconds'].mean()
        }

    def get_user_segments(self) -> pd.DataFrame:
        """Segmenta usuários por uso"""

        # Agregar por usuário
        user_stats = self.db.query(
            ConversationMetrics.user_id,
            func.count(ConversationMetrics.conversation_id).label('conversation_count'),
            func.sum(ConversationMetrics.total_tokens).label('total_tokens'),
            func.sum(ConversationMetrics.total_cost_usd).label('total_cost'),
            func.avg(ConversationMetrics.satisfaction_score).label('avg_satisfaction')
        ).group_by(ConversationMetrics.user_id).all()

        df = pd.DataFrame(user_stats)

        # Segmentar
        df['segment'] = pd.cut(
            df['conversation_count'],
            bins=[0, 5, 20, 100, float('inf')],
            labels=['Casual', 'Regular', 'Power', 'Super']
        )

        return df

    def cohort_analysis(self, start_date: datetime, periods: int = 12) -> pd.DataFrame:
        """Análise de coorte (retençêo)"""

        # Agrupar usuários por mês de primeira conversa
        # ... (implementaçêo de cohort analysis)
        pass

    def identify_churn_risk(self, threshold_days: int = 30) -> List[str]:
        """Identifica usuários em risco de churn"""

        cutoff_date = datetime.now() - timedelta(days=threshold_days)

        # Usuários que eram ativos mas pararam
        inactive_users = self.db.query(ConversationMetrics.user_id).filter(
            ConversationMetrics.timestamp < cutoff_date
        ).distinct().all()

        return [user[0] for user in inactive_users]
```

### 8.7.2 Dashboards com Plotly

```python
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def create_analytics_dashboard(metrics_df: pd.DataFrame):
    """Cria dashboard interativo"""

    # Layout com subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            'Conversations Over Time',
            'Token Usage by User Segment',
            'Satisfaction Score Distribution',
            'Cost Analysis'
        ),
        specs=[
            [{"type": "scatter"}, {"type": "bar"}],
            [{"type": "histogram"}, {"type": "pie"}]
        ]
    )

    # 1. Conversas ao longo do tempo
    daily_conv = metrics_df.groupby(metrics_df['timestamp'].dt.date).size()
    fig.add_trace(
        go.Scatter(x=daily_conv.index, y=daily_conv.values, mode='lines+markers', name='Conversations'),
        row=1, col=1
    )

    # 2. Uso de tokens por segmento
    segment_tokens = metrics_df.groupby('user_segment')['total_tokens'].sum()
    fig.add_trace(
        go.Bar(x=segment_tokens.index, y=segment_tokens.values, name='Tokens'),
        row=1, col=2
    )

    # 3. Distribuiçêo de satisfaçêo
    fig.add_trace(
        go.Histogram(x=metrics_df['satisfaction_score'], name='Satisfaction'),
        row=2, col=1
    )

    # 4. Breakdown de custos
    cost_by_model = metrics_df.groupby('model_used')['total_cost_usd'].sum()
    fig.add_trace(
        go.Pie(labels=cost_by_model.index, values=cost_by_model.values, name='Cost'),
        row=2, col=2
    )

    # Layout
    fig.update_layout(
        title_text="Agent Analytics Dashboard",
        showlegend=True,
        height=800
    )

    return fig

# Uso
fig = create_analytics_dashboard(metrics_df)
fig.write_html("dashboard.html")  # Salvar como HTML
fig.show()  # Mostrar no browser
```

### 8.7.3 A/B Testing

```python
from scipy import stats

class ABTest:
    """Framework para A/B testing de agentes"""

    def __init__(self, variant_a_name: str = "Control", variant_b_name: str = "Treatment"):
        self.variant_a = variant_a_name
        self.variant_b = variant_b_name
        self.results = {variant_a_name: [], variant_b_name: []}

    def assign_variant(self, user_id: str) -> str:
        """Atribui variante baseado em hash do user_id"""
        import hashlib
        hash_value = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
        return self.variant_a if hash_value % 2 == 0 else self.variant_b

    def record_metric(self, variant: str, value: float):
        """Registra métrica para uma variante"""
        self.results[variant].append(value)

    def analyze(self, metric_name: str = "conversion_rate") -> dict:
        """Analisa resultados do teste"""

        a_data = self.results[self.variant_a]
        b_data = self.results[self.variant_b]

        # T-test
        t_stat, p_value = stats.ttest_ind(a_data, b_data)

        # Médias
        a_mean = np.mean(a_data)
        b_mean = np.mean(b_data)

        # Lift
        lift = ((b_mean - a_mean) / a_mean) * 100 if a_mean > 0 else 0

        # Significância
        is_significant = p_value < 0.05

        return {
            "variant_a_mean": a_mean,
            "variant_b_mean": b_mean,
            "lift_percent": lift,
            "p_value": p_value,
            "is_significant": is_significant,
            "winner": self.variant_b if is_significant and b_mean > a_mean else self.variant_a,
            "sample_size_a": len(a_data),
            "sample_size_b": len(b_data)
        }

# Uso
ab_test = ABTest("GPT-4", "Claude-Sonnet")

# Atribuir variantes aos usuários
for user_id in user_ids:
    variant = ab_test.assign_variant(user_id)

    # Processar com agente da variante apropriada
    if variant == "GPT-4":
        response = gpt4_agent.run(message)
    else:
        response = claude_agent.run(message)

    # Registrar métrica (ex: satisfaçêo do usuário)
    satisfaction = get_user_satisfaction(user_id)
    ab_test.record_metric(variant, satisfaction)

# Analisar resultados
results = ab_test.analyze()
print(results)
# {
#   'variant_a_mean': 4.2,
#   'variant_b_mean': 4.5,
#   'lift_percent': 7.14,
#   'p_value': 0.023,
#   'is_significant': True,
#   'winner': 'Claude-Sonnet'
# }
```

---

## 8.8 Ferramentas de Testes

### 8.8.1 Pytest

```python
# tests/test_agent.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from app.agent import AgentService
from app.models import AgentRequest

@pytest.fixture
def agent_service():
    """Fixture do serviço de agente"""
    return AgentService(model="claude-3-haiku-20240307")

@pytest.fixture
def mock_anthropic_response():
    """Mock de resposta da API Anthropic"""
    mock = Mock()
    mock.content = [Mock(text="Mocked response")]
    mock.usage = Mock(input_tokens=10, output_tokens=20)
    return mock

class TestAgentService:
    """Suite de testes para AgentService"""

    def test_initialization(self, agent_service):
        """Testa inicializaçêo"""
        assert agent_service.model == "claude-3-haiku-20240307"
        assert agent_service.total_cost == 0.0

    def test_process_message(self, agent_service):
        """Testa processamento de mensagem"""
        response = agent_service.process("Hello")
        assert isinstance(response, str)
        assert len(response) > 0

    @pytest.mark.asyncio
    async def test_async_processing(self, agent_service):
        """Testa processamento assíncrono"""
        response = await agent_service.process_async("Test")
        assert response is not None

    def test_empty_message_raises_error(self, agent_service):
        """Testa que mensagem vazia gera erro"""
        with pytest.raises(ValueError, match="Message cannot be empty"):
            agent_service.process("")

    @patch('anthropic.Anthropic.messages.create')
    def test_with_mocked_api(self, mock_create, agent_service, mock_anthropic_response):
        """Testa com API mockada (sem custo real)"""
        mock_create.return_value = mock_anthropic_response

        response = agent_service.process("Test message")

        assert response == "Mocked response"
        mock_create.assert_called_once()

        # Verificar que custo foi calculado
        assert agent_service.total_cost > 0

    @pytest.mark.parametrize("message,expected_length", [
        ("Short", 5),
        ("Medium length message", 21),
        ("A" * 1000, 1000),
    ])
    def test_various_message_lengths(self, agent_service, message, expected_length):
        """Testa com diferentes tamanhos de mensagem"""
        assert len(message) == expected_length
        # Process and verify...

    def test_cost_tracking(self, agent_service):
        """Testa rastreamento de custos"""
        initial_cost = agent_service.get_total_cost()

        agent_service.process("Test message")

        final_cost = agent_service.get_total_cost()
        assert final_cost > initial_cost

    def test_concurrent_requests(self, agent_service):
        """Testa múltiplas requisições concorrentes"""
        import concurrent.futures

        messages = [f"Message {i}" for i in range(10)]

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(agent_service.process, msg) for msg in messages]
            results = [f.result() for f in futures]

        assert len(results) == 10
        assert all(isinstance(r, str) for r in results)
```

**Executar testes:**

```bash
# Todos os testes
pytest

# Com verbose
pytest -v

# Com coverage
pytest --cov=app --cov-report=html

# Testes específicos
pytest tests/test_agent.py::TestAgentService::test_initialization

# Apenas testes marcados
pytest -m "not slow"
```

### 8.8.2 Testes de Integraçêo

```python
# tests/test_integration.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAPIIntegration:
    """Testes de integraçêo da API"""

    def test_health_endpoint(self):
        """Testa endpoint de health"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_chat_endpoint_success(self):
        """Testa endpoint de chat com sucesso"""
        response = client.post(
            "/api/chat",
            json={"message": "Hello, agent!"},
            headers={"Authorization": "Bearer test-token"}
        )

        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert isinstance(data["response"], str)

    def test_chat_endpoint_unauthorized(self):
        """Testa que endpoint requer autenticaçêo"""
        response = client.post(
            "/api/chat",
            json={"message": "Hello"}
        )
        assert response.status_code == 401

    def test_rate_limiting(self):
        """Testa rate limiting"""
        # Fazer muitas requisições rapidamente
        for i in range(15):
            response = client.post(
                "/api/chat",
                json={"message": f"Test {i}"},
                headers={"Authorization": "Bearer test-token"}
            )

        # Última deve ser rate limited
        assert response.status_code == 429

    def test_invalid_input_validation(self):
        """Testa validaçêo de entrada"""
        response = client.post(
            "/api/chat",
            json={"message": ""},  # Mensagem vazia
            headers={"Authorization": "Bearer test-token"}
        )
        assert response.status_code == 422  # Validation error
```

### 8.8.3 Testes End-to-End

```python
# tests/test_e2e.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Fixture do browser para testes E2E"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

def test_complete_user_flow(browser):
    """Testa fluxo completo do usuário"""

    page = browser.new_page()

    # 1. Navegar para a aplicaçêo
    page.goto("http://localhost:8501")  # Streamlit app

    # 2. Digitar mensagem
    page.fill("input[type='text']", "Hello, agent!")

    # 3. Enviar
    page.click("button:has-text('Send')")

    # 4. Aguardar resposta
    page.wait_for_selector("text=Hi! How can I help", timeout=10000)

    # 5. Verificar que resposta apareceu
    content = page.text_content("body")
    assert "Hi! How can I help" in content

    page.close()
```

---

## 8.9 Recursos da Comunidade

### 8.9.1 Documentaçêo e Tutoriais

**Sites essenciais:**

- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction)
- [Anthropic Claude Docs](https://docs.anthropic.com/)
- [OpenAI Platform Docs](https://platform.openai.com/docs)
- [Agno Docs](https://docs.agno.dev/)
- [CrewAI Docs](https://docs.crewai.com/)

**Cursos recomendados:**

- DeepLearning.AI - LangChain courses
- Anthropic - Prompt Engineering Interactive Tutorial
- Fast.ai - Practical Deep Learning for Coders

### 8.9.2 Comunidades

**Discord Servers:**
- LangChain Discord
- Anthropic Developer Discord
- AI Engineer Discord

**Reddit:**
- r/MachineLearning
- r/LanguageTechnology
- r/LangChain

**GitHub:**
- Awesome LangChain
- Awesome LLM Apps
- Awesome AI Agents

### 8.9.3 Ferramentas Open Source

**Repositórios úteis:**

```bash
# LangChain templates
git clone https://github.com/langchain-ai/langchain-templates

# Agno examples
git clone https://github.com/agno-ai/examples

# CrewAI examples
git clone https://github.com/joaomdmoura/crewai-examples

# MCP servers collection
git clone https://github.com/anthropics/mcp-servers
```

---

## 8.10 Projeto Prático: Painel de Controle Universal

Vamos criar um painel de controle completo para gerenciar e monitorar múltiplos agentes.

### 8.10.1 Arquitetura do Projeto

```
agent-control-panel/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app
│   │   ├── agents.py            # Gerenciamento de agentes
│   │   ├── analytics.py         # Analytics
│   │   └── models.py            # Modelos Pydantic
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── streamlit_app.py         # Interface Streamlit
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

### 8.10.2 Backend (FastAPI)

**backend/app/main.py:**

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os

from .agents import AgentManager
from .analytics import Analytics
from .models import AgentConfig, ChatRequest, ChatResponse, AgentMetrics

app = FastAPI(title="Agent Control Panel API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar gerenciador de agentes
agent_manager = AgentManager()
analytics = Analytics()

# ============================================================================
# AGENT MANAGEMENT
# ============================================================================

@app.post("/api/agents", response_model=dict)
async def create_agent(config: AgentConfig):
    """Cria um novo agente"""
    agent_id = agent_manager.create_agent(
        name=config.name,
        model=config.model,
        temperature=config.temperature,
        tools=config.tools
    )
    return {"agent_id": agent_id, "status": "created"}

@app.get("/api/agents", response_model=List[dict])
async def list_agents():
    """Lista todos os agentes"""
    return agent_manager.list_agents()

@app.delete("/api/agents/{agent_id}")
async def delete_agent(agent_id: str):
    """Deleta um agente"""
    agent_manager.delete_agent(agent_id)
    return {"status": "deleted"}

# ============================================================================
# CHAT
# ============================================================================

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Envia mensagem para um agente"""

    agent = agent_manager.get_agent(request.agent_id)

    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    response = agent.run(request.message)

    # Registrar métricas
    analytics.record_conversation(
        agent_id=request.agent_id,
        user_id=request.user_id,
        message=request.message,
        response=response,
        tokens=agent.last_tokens,
        cost=agent.last_cost
    )

    return ChatResponse(
        response=response,
        tokens_used=agent.last_tokens,
        cost_usd=agent.last_cost
    )

# ============================================================================
# ANALYTICS
# ============================================================================

@app.get("/api/analytics/overview")
async def get_analytics_overview():
    """Visêo geral de analytics"""
    return analytics.get_overview()

@app.get("/api/analytics/agent/{agent_id}")
async def get_agent_analytics(agent_id: str):
    """Analytics de um agente específico"""
    return analytics.get_agent_metrics(agent_id)

@app.get("/api/analytics/costs")
async def get_cost_breakdown():
    """Breakdown de custos"""
    return analytics.get_cost_breakdown()
```

**backend/app/agents.py:**

```python
from agno import Agent
from typing import Dict, List, Optional
import uuid

class AgentManager:
    """Gerencia múltiplos agentes"""

    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.configs: Dict[str, dict] = {}

    def create_agent(
        self,
        name: str,
        model: str,
        temperature: float = 0.7,
        tools: Optional[List[str]] = None
    ) -> str:
        """Cria um novo agente"""

        agent_id = str(uuid.uuid4())

        agent = Agent(
            name=name,
            model=model,
            temperature=temperature
        )

        # Adicionar tools se especificadas
        if tools:
            # Carregar ferramentas baseado nos nomes
            agent.tools = self._load_tools(tools)

        self.agents[agent_id] = agent
        self.configs[agent_id] = {
            "id": agent_id,
            "name": name,
            "model": model,
            "temperature": temperature,
            "tools": tools or []
        }

        return agent_id

    def get_agent(self, agent_id: str) -> Optional[Agent]:
        """Retorna um agente"""
        return self.agents.get(agent_id)

    def list_agents(self) -> List[dict]:
        """Lista todos os agentes"""
        return list(self.configs.values())

    def delete_agent(self, agent_id: str):
        """Deleta um agente"""
        if agent_id in self.agents:
            del self.agents[agent_id]
            del self.configs[agent_id]

    def _load_tools(self, tool_names: List[str]) -> List:
        """Carrega ferramentas por nome"""
        # Implementar carregamento de ferramentas
        return []
```

### 8.10.3 Frontend (Streamlit)

**frontend/streamlit_app.py:**

```python
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Agent Control Panel",
    page_icon="🎛️",
    layout="wide"
)

st.title("🎛️ Agent Control Panel")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to", ["Agents", "Chat", "Analytics"])

# ============================================================================
# PAGE: AGENTS
# ============================================================================

if page == "Agents":
    st.header("🤖 Agent Management")

    # Criar novo agente
    with st.expander("➕ Create New Agent"):
        with st.form("create_agent"):
            name = st.text_input("Agent Name")
            model = st.selectbox("Model", [
                "claude-3-haiku-20240307",
                "claude-3-7-sonnet-20250219",
                "claude-3-opus-20240229"
            ])
            temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)

            if st.form_submit_button("Create"):
                response = requests.post(f"{API_URL}/api/agents", json={
                    "name": name,
                    "model": model,
                    "temperature": temperature,
                    "tools": []
                })

                if response.status_code == 200:
                    st.success(f"Agent created: {response.json()['agent_id']}")
                    st.rerun()

    # Listar agentes
    st.subheader("Active Agents")

    response = requests.get(f"{API_URL}/api/agents")
    if response.status_code == 200:
        agents = response.json()

        if agents:
            for agent in agents:
                col1, col2, col3, col4 = st.columns([3, 2, 2, 1])

                with col1:
                    st.write(f"**{agent['name']}**")

                with col2:
                    st.write(agent['model'])

                with col3:
                    st.write(f"Temp: {agent['temperature']}")

                with col4:
                    if st.button("Delete", key=agent['id']):
                        requests.delete(f"{API_URL}/api/agents/{agent['id']}")
                        st.rerun()
        else:
            st.info("No agents created yet")

# ============================================================================
# PAGE: CHAT
# ============================================================================

elif page == "Chat":
    st.header("💬 Chat with Agent")

    # Selecionar agente
    response = requests.get(f"{API_URL}/api/agents")
    agents = response.json()

    if not agents:
        st.warning("Please create an agent first")
    else:
        selected_agent = st.selectbox(
            "Select Agent",
            agents,
            format_func=lambda x: x['name']
        )

        # Histórico de chat
        if 'messages' not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Input do usuário
        if prompt := st.chat_input("Type your message..."):
            # Adicionar ao histórico
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("user"):
                st.markdown(prompt)

            # Chamar API
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = requests.post(f"{API_URL}/api/chat", json={
                        "agent_id": selected_agent['id'],
                        "user_id": "demo-user",
                        "message": prompt
                    })

                    if response.status_code == 200:
                        data = response.json()
                        st.markdown(data['response'])

                        # Mostrar métricas
                        col1, col2 = st.columns(2)
                        with col1:
                            st.caption(f"Tokens: {data['tokens_used']}")
                        with col2:
                            st.caption(f"Cost: ${data['cost_usd']:.4f}")

                        # Adicionar ao histórico
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": data['response']
                        })

# ============================================================================
# PAGE: ANALYTICS
# ============================================================================

elif page == "Analytics":
    st.header("📊 Analytics Dashboard")

    # Overview
    response = requests.get(f"{API_URL}/api/analytics/overview")
    if response.status_code == 200:
        overview = response.json()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Conversations", overview['total_conversations'])

        with col2:
            st.metric("Total Tokens", overview['total_tokens'])

        with col3:
            st.metric("Total Cost", f"${overview['total_cost']:.2f}")

        with col4:
            st.metric("Avg Satisfaction", f"{overview['avg_satisfaction']:.2f}/5")

    # Custos por agente
    st.subheader("Cost Breakdown by Agent")

    response = requests.get(f"{API_URL}/api/analytics/costs")
    if response.status_code == 200:
        costs = response.json()

        df = pd.DataFrame(costs)

        if not df.empty:
            fig = px.pie(df, values='cost', names='agent_name', title='Cost Distribution')
            st.plotly_chart(fig)

            # Tabela detalhada
            st.dataframe(df, use_container_width=True)
```

### 8.10.4 Deploy com Docker Compose

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    ports:
      - "8501:8501"
    depends_on:
      - backend
    volumes:
      - ./frontend:/app

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: agent
      POSTGRES_PASSWORD: password
      POSTGRES_DB: analytics
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

**Executar:**

```bash
docker-compose up -d
```

Acesse:
- API: http://localhost:8000
- Dashboard: http://localhost:8501

---

## 8.11 Resumo e Próximos Passos

### 8.11.1 O Que Aprendemos

Neste módulo final, você dominou:

✅ **Ecossistema de Ferramentas**: Panorama completo do universo de agentes
✅ **Ferramentas de Desenvolvimento**: IDEs, notebooks, ambientes
✅ **Bibliotecas Essenciais**: Pandas, Pydantic, httpx, caching
✅ **Interfaces de Usuário**: Streamlit, Gradio, Chainlit
✅ **Integrações**: GitHub, Slack, Google Calendar, APIs genéricas
✅ **Debugging**: pdb, profiling, LangSmith, Sentry
✅ **Analytics**: Métricas de negócio, dashboards, A/B testing
✅ **Testes**: pytest, testes de integraçêo, E2E
✅ **Comunidade**: Recursos, documentaçêo, open source
✅ **Projeto Prático**: Painel de controle completo

### 8.11.2 Você Completou o Curso!

**Parabéns! 🎉🎓**

Você completou todos os 8 módulos do curso **Engenharia de Agentes de IA 2.0**!

**Jornada percorrida:**

1. ✅ Fundamentos de IA Generativa
2. ✅ Engenharia de Prompts Avançada
3. ✅ LangChain para Agentes Inteligentes
4. ✅ Agno - Simplicidade e Poder
5. ✅ CrewAI - Sistemas Multi-Agente
6. ✅ Model Context Protocol (MCP)
7. ✅ Deploy e Produçêo
8. ✅ Ferramentas e Ecossistema

**Você agora é capaz de:**

- 🎯 Projetar e implementar agentes de IA complexos
- 🚀 Criar sistemas multi-agente orquestrados
- 🔧 Conectar agentes a dados e ferramentas reais via MCP
- ☁️ Fazer deploy de sistemas em produçêo
- 📊 Monitorar, otimizar e escalar aplicações
- 💰 Gerenciar custos e performance
- 🔒 Implementar segurança de nível enterprise
- 🛠️ Usar todo o ecossistema de ferramentas disponíveis

### 8.11.3 Próximos Passos

**1. Pratique!**

Construa projetos reais:
- Sistema de atendimento ao cliente
- Assistente de pesquisa científica
- Automaçêo de processos empresariais
- Agente de análise de dados
- Content creation pipeline

**2. Contribua para a Comunidade**

- Open source contributions
- Compartilhe seus projetos no GitHub
- Escreva artigos e tutoriais
- Ajude outros no Discord/Reddit

**3. Continue Aprendendo**

- Acompanhe novos modelos e frameworks
- Experimente com cutting-edge research
- Participe de hackathons e competições
- Faça cursos avançados

**4. Networking**

- Participe de conferências (AI Engineer Summit, etc.)
- Conecte-se com outros engenheiros de agentes
- Junte-se a comunidades profissionais

### 8.11.4 Recursos Finais

**Livros recomendados:**
- "Building LLM Apps" - Maxime Labonne
- "Hands-On Large Language Models" - Jay Alammar
- "AI Engineering" - Chip Huyen

**Newsletters:**
- The Batch (DeepLearning.AI)
- AI Engineer Digest
- Anthropic Developer Newsletter

**Podcasts:**
- Latent Space
- The AI Breakdown
- Practical AI

---

**Mensagem Final**

Você agora possui as habilidades e conhecimentos para criar sistemas de agentes de IA de nível profissional que resolvem problemas reais no mundo real.

A jornada nêo termina aqui - ela está apenas começando. O campo de agentes de IA está evoluindo rapidamente, e você agora está equipado para evoluir junto com ele.

**Continue construindo. Continue aprendendo. Continue inovando.**

🚀 **O futuro da IA é construído por engenheiros como você!**

---

*"A melhor maneira de prever o futuro é construí-lo." - Alan Kay*

**Obrigado por participar deste curso! 🙏**

---

**Certificado de Conclusêo**: Complete os exercícios e projetos práticos para receber seu certificado oficial de Engenheiro de Agentes de IA 2.0.

**Mantenha-se conectado**: Junte-se à nossa comunidade de alumni e continue sua jornada de aprendizado!
