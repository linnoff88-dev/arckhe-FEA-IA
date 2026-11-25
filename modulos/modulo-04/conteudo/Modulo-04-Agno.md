# Módulo 4: Agentes Autônomos com Agno

**Duraçêo:** 5 horas | **Nível:** Intermediário

> **Frase-guia:** "Simplicidade é a sofisticaçêo máxima." - Leonardo da Vinci

---

![Capa do Módulo 4](../../../imagens-conceituais/modulo4_agno_agents.png)

## Ato 2: A Construçêo (Perspectiva Alternativa)

> "Você dominou a complexidade da orquestraçêo com LangChain. Agora, vamos explorar a elegância da simplicidade. Agno nos convida a pensar de forma diferente sobre a construçêo de agentes, focando em um design minimalista e em um fluxo de trabalho intuitivo. É a prova de que o poder nêo precisa vir da complexidade."

Depois de mergulhar na vastidêo de opções do LangChain, **Agno surge como um contraponto refrescante**. Criado com a filosofia de ser "**painfully simple**" (dolorosamente simples), este framework open-source foca em fazer uma coisa e fazê-la excepcionalmente bem: **criar agentes de IA autônomos**.

Neste módulo, vamos aprender:
- A filosofia e princípios de design do Agno
- Como criar agentes com código minimalista
- Padrões avançados (RAG, Memory, Multi-Agent)
- Quando escolher Agno vs LangChain
- Best practices para produçêo

---

## Capítulo 4.1: A Filosofia Agno

### O Problema da Complexidade

Após trabalhar com LangChain, você pode ter experimentado:

**Desafios Comuns:**
- 🤯 **Curva de aprendizado íngreme:** Dezenas de classes e abstrações
- 🍝 **"Spaghetti code":** Chains aninhadas difíceis de debugar
- 🐛 **Debugging complexo:** Rastrear erros através de múltiplas camadas
- 📚 **Documentaçêo fragmentada:** Muitas opções, pouca clareza
- ⏰ **Time to hello world:** Horas para entender o básico

**Exemplo de complexidade LangChain:**
```python
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.prompts import MessagesPlaceholder
from langchain.schema import SystemMessage

# Muitas importações, configurações...
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

llm = ChatOpenAI(temperature=0)

tools = [Tool(...), Tool(...)]  # Configuraçêo verbose

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    memory=memory,
    verbose=True,
    # ... mais configurações
)

# Finalmente executar!
agent.run("Pergunta")
```

### A Soluçêo Agno

Agno foi criado para resolver exatamente esses pontos de dor:

**Mesmo agente em Agno:**
```python
from agno import Agent

@tool
def my_tool(input: str) -> str:
    """Descriçêo da ferramenta"""
    return result

agent = Agent(tools=[my_tool])
agent.run("Pergunta")  # Pronto!
```

**3 linhas vs 30+ linhas.** 🎯

### Os 3 Pilares da Filosofia Agno

#### 1. Simplicidade Extrema

```
PRINCÍPIO: Se você precisa consultar a documentaçêo
para fazer algo básico, o design falhou.
```

**Manifesto:**
- Código linear e direto
- Zero abstrações desnecessárias
- API intuitiva e previsível
- Menos é mais

**Exemplo:**
```python
# LangChain: Configuraçêo de memoria
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="output"
)

# Agno: Apenas funciona
agent = Agent(memory=True)  # That's it!
```

#### 2. Foco no Agente

```
PRINCÍPIO: Agno faz UMA coisa excepcional bem:
Agentes autônomos com ferramentas.
```

**Nêo tenta ser:**
- ❌ Framework genérico de LLM
- ❌ Processador de documentos
- ❌ Pipeline de dados
- ❌ Canivete suíço

**Foca em:**
- ✅ Agentes que tomam decisões
- ✅ Agentes que usam ferramentas
- ✅ Agentes que colaboram
- ✅ Simplicidade de debugging

#### 3. Transparência Total

```
PRINCÍPIO: Você deve saber exatamente o que o agente
está pensando em cada etapa.
```

**Logging claro e automático:**
```
[Agent] Thinking: Preciso buscar informações sobre Python
[Agent] Action: search_web
[Agent] Action Input: "Python programming language"
[Agent] Observation: Python is a high-level...
[Agent] Thinking: Agora tenho a informaçêo
[Agent] Final Answer: Python is...
```

Sem mistérios. Sem caixas-pretas.

### Comparaçêo Direta: Agno vs LangChain

| Aspecto | LangChain | Agno |
|---------|-----------|------|
| **Filosofia** | Framework abrangente | Framework focado |
| **Curva de Aprendizado** | Íngreme (dias/semanas) | Suave (horas) |
| **Linhas de Código** | Muitas (~50-100 para agente) | Poucas (~10-20) |
| **Debugging** | Complexo, múltiplas camadas | Simples, linear |
| **Flexibilidade** | Muito alta | Moderada |
| **Casos de Uso** | Qualquer aplicaçêo LLM | Principalmente agentes |
| **Integrações** | 100+ | Essenciais |
| **Performance** | Boa | Excelente (menos overhead) |
| **Manutenibilidade** | Desafiadora | Fácil |

### Quando Usar Cada Um?

**Use LangChain quando:**
- Precisa de integrações com tudo
- Projeto complexo de processamento de dados
- Pipelines avançados de transformaçêo
- Time grande com tempo para aprender

**Use Agno quando:**
- Foco principal é agentes autônomos
- Protot ipagem rápida
- Clareza e manutenibilidade sêo prioridades
- Time pequeno ou solo developer
- Deadline apertado

**Use ambos quando:**
- Sistema híbrido (RAG com LangChain + Agentes com Agno)
- Migraçêo gradual
- Diferentes partes do sistema têm necessidades diferentes

---

## Capítulo 4.2: Setup e Primeiros Passos

### Instalaçêo

```bash
# Instalaçêo básica
pip install agno

# Com OpenAI
pip install "agno[openai]"

# Com Anthropic (Claude)
pip install "agno[anthropic]"

# Completo
pip install "agno[all]"
```

### Configuraçêo de API Keys

```python
import os

# Opçêo 1: Variável de ambiente
os.environ["OPENAI_API_KEY"] = "sk-..."

# Opçêo 2: .env file (recomendado)
# Criar arquivo .env:
# OPENAI_API_KEY=sk-...

from dotenv import load_dotenv
load_dotenv()

# Opçêo 3: Diretamente no código (nêo recomendado para produçêo)
from agno import Agent
agent = Agent(api_key="sk-...")
```

### Hello World: Seu Primeiro Agente

```python
from agno import Agent, tool

@tool
def get_weather(city: str) -> str:
    """
    Retorna informações sobre o clima de uma cidade.

    Args:
        city: Nome da cidade
    """
    # Simulaçêo (na prática, chamar API de clima)
    return f"O clima em {city} está ensolarado, 25°C"

# Criar agente
agent = Agent(
    name="Assistente de Clima",
    tools=[get_weather],
    model="gpt-4"
)

# Executar
result = agent.run("Como está o tempo em Sêo Paulo?")
print(result)
```

**Saída:**
```
[Agent] Thinking: Preciso verificar o clima em Sêo Paulo
[Agent] Action: get_weather
[Agent] Action Input: Sêo Paulo
[Agent] Observation: O clima em Sêo Paulo está ensolarado, 25°C
[Agent] Thinking: Tenho a informaçêo necessária
[Agent] Final Answer: O clima em Sêo Paulo está ensolarado com 25°C.
```

### Anatomia de um Tool

```python
@tool  # Decorator obrigatório
def nome_da_funcao(parametro: tipo) -> tipo:  # Type hints sêo importantes!
    """
    Descriçêo clara e concisa do que a ferramenta faz.

    O LLM usa esta descriçêo para decidir quando usar a tool.
    Seja específico e objetivo.

    Args:
        parametro: Descriçêo do parâmetro

    Returns:
        Descriçêo do retorno
    """
    # Implementaçêo
    return resultado
```

**Regras de Ouro:**
1. ✅ **Sempre use type hints** - Agno valida tipos
2. ✅ **Docstring detalhada** - É a "interface" para o LLM
3. ✅ **Nome descritivo** - `get_weather` > `tool1`
4. ✅ **Uma responsabilidade** - Cada tool faz UMA coisa
5. ✅ **Retorno sempre string** - LLMs entendem texto

---

## Capítulo 4.3: Tools - O Poder das Ferramentas

### Tools Básicas

#### 1. Tool de Cálculo

```python
@tool
def calculator(expression: str) -> str:
    """
    Calcula expressões matemáticas.

    Args:
        expression: Expressêo matemática (ex: "2 + 2", "10 * 5")
    """
    try:
        result = eval(expression)
        return f"Resultado: {result}"
    except Exception as e:
        return f"Erro ao calcular: {str(e)}"
```

#### 2. Tool de Busca Web (Mock)

```python
@tool
def search_web(query: str) -> str:
    """
    Busca informações na web.

    Args:
        query: Termo de busca
    """
    # Em produçêo, usar API real (SerpAPI, Google, etc.)
    mock_results = {
        "python": "Python é uma linguagem de programaçêo de alto nível...",
        "ia": "Inteligência Artificial é o campo da ciência da computaçêo..."
    }

    for keyword, content in mock_results.items():
        if keyword.lower() in query.lower():
            return content

    return "Nenhum resultado encontrado."
```

#### 3. Tool com API Externa

```python
import requests

@tool
def get_exchange_rate(from_currency: str, to_currency: str) -> str:
    """
    Retorna taxa de câmbio entre duas moedas.

    Args:
        from_currency: Moeda de origem (ex: USD, BRL, EUR)
        to_currency: Moeda de destino
    """
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        rate = data['rates'][to_currency]
        return f"1 {from_currency} = {rate} {to_currency}"

    except Exception as e:
        return f"Erro ao buscar taxa: {str(e)}"
```

### Tools Avançadas

#### 4. Tool com Estado (Database)

```python
# Simular banco de dados em memória
TASKS_DB = []

@tool
def add_task(task: str) -> str:
    """
    Adiciona uma nova tarefa à lista.

    Args:
        task: Descriçêo da tarefa a adicionar
    """
    TASKS_DB.append(task)
    return f"✓ Tarefa adicionada: '{task}'. Total: {len(TASKS_DB)} tarefas."

@tool
def list_tasks() -> str:
    """
    Lista todas as tarefas pendentes.
    """
    if not TASKS_DB:
        return "Nenhuma tarefa pendente."

    tasks_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(TASKS_DB)])
    return f"Tarefas pendentes:\n{tasks_list}"

@tool
def remove_task(task_number: int) -> str:
    """
    Remove uma tarefa da lista.

    Args:
        task_number: Número da tarefa (começando em 1)
    """
    try:
        task = TASKS_DB.pop(task_number - 1)
        return f"✓ Tarefa removida: '{task}'"
    except IndexError:
        return f"Erro: Tarefa #{task_number} nêo existe."
```

#### 5. Tool com Arquivos

```python
import json

@tool
def save_to_file(filename: str, content: str) -> str:
    """
    Salva conteúdo em um arquivo.

    Args:
        filename: Nome do arquivo
        content: Conteúdo a salvar
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✓ Conteúdo salvo em '{filename}'"
    except Exception as e:
        return f"Erro ao salvar: {str(e)}"

@tool
def read_from_file(filename: str) -> str:
    """
    Lê conteúdo de um arquivo.

    Args:
        filename: Nome do arquivo a ler
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"Arquivo '{filename}' nêo encontrado."
    except Exception as e:
        return f"Erro ao ler: {str(e)}"
```

### Agente com Múltiplas Tools

```python
from agno import Agent

# Criar agente assistente completo
assistant = Agent(
    name="Assistente Pessoal",
    description="Ajuda com cálculos, buscas, tarefas e arquivos",
    tools=[
        calculator,
        search_web,
        get_exchange_rate,
        add_task,
        list_tasks,
        remove_task,
        save_to_file,
        read_from_file
    ],
    model="gpt-4",
    show_tool_calls=True  # Mostrar raciocínio
)

# Testar capacidades
responses = [
    assistant.run("Qual é 25 * 17?"),
    assistant.run("Adicione 'Comprar leite' às minhas tarefas"),
    assistant.run("Quanto vale 1 dólar em reais?"),
    assistant.run("Liste minhas tarefas"),
]

for r in responses:
    print(f"\n{r}\n" + "="*60)
```

---

## Capítulo 4.4: Memory e Contexto Conversacional

### Memory Simples

```python
from agno import Agent

# Ativar memória com uma linha
agent = Agent(
    tools=[...],
    memory=True  # Isso é tudo!
)

# Conversa com contexto
agent.run("Meu nome é Joêo")
agent.run("Qual é meu nome?")  # Lembra: "Seu nome é Joêo"
agent.run("Adicione 'estudar Python' nas minhas tarefas")
agent.run("O que eu pedi para adicionar?")  # Lembra a tarefa
```

### Memory Configurada

```python
from agno import Agent
from agno.memory import ConversationMemory

# Memória customizada
memory = ConversationMemory(
    max_messages=10,  # Últimas 10 mensagens
    summary_threshold=20  # Resume após 20 mensagens
)

agent = Agent(
    tools=[...],
    memory=memory
)
```

### Memory Persistente (Storage)

```python
from agno import Agent
from agno.storage import FileStorage

# Salvar histórico em arquivo
storage = FileStorage(path="./agent_history.json")

agent = Agent(
    tools=[...],
    memory=True,
    storage=storage
)

# Histórico persiste entre execuções
agent.run("Meu email é joao@email.com")

# ... reiniciar programa ...

# Agente ainda lembra
agent.run("Qual é meu email?")  # "Seu email é joao@email.com"
```

### Memory com Database (SQLite)

```python
from agno import Agent
from agno.storage import SQLStorage

# Usar SQLite para persistência
storage = SQLStorage(
    connection_string="sqlite:///agent_memory.db",
    session_id="user_123"  # ID único por usuário
)

agent = Agent(
    tools=[...],
    memory=True,
    storage=storage
)

# Memória persistente e escalável
```

---

## Capítulo 4.5: RAG (Retrieval-Augmented Generation) com Agno

### Abordagem 1: RAG como Tool

A forma mais simples de fazer RAG em Agno é criar uma tool que consulta seu conhecimento base:

```python
from agno import Agent, tool
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Setup do vector store (uma vez)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Documentos de exemplo
documents = [
    "Python é uma linguagem de programaçêo de alto nível.",
    "JavaScript é usado para desenvolvimento web.",
    "SQL é usado para consultar bancos de dados.",
    "Docker facilita a containerizaçêo de aplicações."
]

# Criar embeddings
embeddings = model.encode(documents)
dimension = embeddings.shape[1]

# Criar índice FAISS
index = faiss.IndexFlatL2(dimension)
index.add(embeddings.astype('float32'))

@tool
def search_knowledge_base(query: str) -> str:
    """
    Busca informações na base de conhecimento da empresa.

    Args:
        query: Pergunta ou termo de busca
    """
    # Embedding da query
    query_embedding = model.encode([query]).astype('float32')

    # Buscar top 2 documentos mais relevantes
    k = 2
    distances, indices = index.search(query_embedding, k)

    # Retornar documentos encontrados
    results = [documents[i] for i in indices[0]]
    return "\n".join(results)

# Agente com RAG
rag_agent = Agent(
    name="Assistente Técnico",
    tools=[search_knowledge_base],
    model="gpt-4"
)

# Testar
response = rag_agent.run("O que você sabe sobre Docker?")
print(response)
```

**Saída:**
```
[Agent] Thinking: Preciso buscar informações sobre Docker
[Agent] Action: search_knowledge_base
[Agent] Action Input: Docker
[Agent] Observation: Docker facilita a containerizaçêo de aplicações.
[Agent] Final Answer: Docker é uma ferramenta que facilita a containerizaçêo de aplicações, permitindo que você empacote software em containers padronizados.
```

### Abordagem 2: RAG com Documentos Reais

```python
from agno import Agent, tool
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Carregar e processar PDFs (executar uma vez)
loader = PyPDFLoader("manual_produto.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(documents)

# Criar vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# Salvar para reutilizaçêo
vectorstore.save_local("vectorstore_agno")

# Agora criar a tool
@tool
def query_product_manual(question: str) -> str:
    """
    Consulta o manual do produto para responder perguntas.

    Args:
        question: Pergunta sobre o produto
    """
    # Carregar vectorstore
    vs = FAISS.load_local(
        "vectorstore_agno",
        OpenAIEmbeddings(),
        allow_dangerous_deserialization=True
    )

    # Buscar documentos relevantes
    docs = vs.similarity_search(question, k=3)

    # Combinar conteúdo
    context = "\n\n".join([doc.page_content for doc in docs])
    return context

# Agente especialista em produto
product_agent = Agent(
    name="Especialista em Produto",
    tools=[query_product_manual],
    model="gpt-4",
    instructions="""
    Você é um especialista no produto. Use a ferramenta query_product_manual
    para buscar informações precisas no manual antes de responder.
    Sempre cite a fonte quando usar informações do manual.
    """
)

# Usar
response = product_agent.run("Qual é o período de garantia?")
```

### RAG + Outros Tools

O poder real vem de combinar RAG com outras capacidades:

```python
@tool
def search_support_tickets(query: str) -> str:
    """Busca tickets de suporte similares"""
    # Implementaçêo...
    pass

@tool
def create_support_ticket(issue: str) -> str:
    """Cria novo ticket de suporte"""
    # Implementaçêo...
    pass

support_agent = Agent(
    name="Agente de Suporte",
    tools=[
        query_product_manual,  # RAG do manual
        search_support_tickets,  # Busca histórico
        create_support_ticket  # Açêo
    ],
    instructions="""
    1. Primeiro, busque no manual do produto
    2. Se nêo encontrar, busque tickets similares
    3. Se ainda precisar, crie um novo ticket
    4. Sempre seja prestativo e preciso
    """
)
```

---

## Capítulo 4.6: Sistemas Multi-Agentes

### Padrêo 1: Agente como Tool

A abordagem mais simples: um agente pode usar outro agente como tool.

```python
from agno import Agent, tool

# Agente Especialista 1: Pesquisador
researcher = Agent(
    name="Pesquisador",
    tools=[search_web, search_knowledge_base],
    model="gpt-4"
)

# Agente Especialista 2: Escritor
writer = Agent(
    name="Escritor",
    tools=[save_to_file],
    model="gpt-4"
)

# Transformar agentes em tools
@tool
def research(topic: str) -> str:
    """
    Pesquisa informações detalhadas sobre um tópico.

    Args:
        topic: Tópico a pesquisar
    """
    return researcher.run(f"Pesquise sobre: {topic}")

@tool
def write_article(topic: str, research_data: str) -> str:
    """
    Escreve um artigo baseado em dados de pesquisa.

    Args:
        topic: Título do artigo
        research_data: Dados da pesquisa
    """
    prompt = f"Escreva um artigo sobre '{topic}' usando estes dados:\n{research_data}"
    return writer.run(prompt)

# Agente Gerente
manager = Agent(
    name="Gerente de Conteúdo",
    tools=[research, write_article],
    model="gpt-4",
    instructions="""
    Você coordena a criaçêo de conteúdo:
    1. Use 'research' para coletar informações
    2. Use 'write_article' para criar o artigo
    3. Sempre siga essa ordem
    """
)

# Executar workflow completo
result = manager.run("Crie um artigo sobre Inteligência Artificial")
```

### Padrêo 2: Pipeline de Agentes

```python
class AgentPipeline:
    """Pipeline sequencial de agentes"""

    def __init__(self, agents: list):
        self.agents = agents

    def run(self, initial_input: str) -> str:
        current_input = initial_input

        for i, agent in enumerate(self.agents):
            print(f"\n{'='*60}")
            print(f"Etapa {i+1}: {agent.name}")
            print(f"{'='*60}")

            current_input = agent.run(current_input)

        return current_input

# Criar pipeline
pipeline = AgentPipeline([
    Agent(
        name="Planejador",
        instructions="Crie um plano detalhado para a tarefa",
        model="gpt-4"
    ),
    Agent(
        name="Executor",
        tools=[search_web, calculator],
        instructions="Execute o plano usando as ferramentas disponíveis",
        model="gpt-4"
    ),
    Agent(
        name="Revisor",
        instructions="Revise o resultado e melhore se necessário",
        model="gpt-4"
    )
])

# Executar
final_result = pipeline.run("Pesquise sobre IA e calcule quantos artigos foram publicados em 2023")
```

### Padrêo 3: Collaborative Agents

```python
class CollaborativeAgents:
    """Múltiplos agentes colaborando em paralelo"""

    def __init__(self, agents: dict):
        self.agents = agents

    def run(self, task: str) -> dict:
        results = {}

        for name, agent in self.agents.items():
            print(f"\n{name} trabalhando...")
            results[name] = agent.run(task)

        return results

    def synthesize(self, results: dict) -> str:
        """Sintetiza resultados de todos os agentes"""
        synthesizer = Agent(
            name="Sintetizador",
            instructions="""
            Analise os resultados de diferentes agentes e
            crie uma resposta consolidada e coerente.
            """
        )

        combined = "\n\n".join([
            f"**{name}:**\n{result}"
            for name, result in results.items()
        ])

        return synthesizer.run(f"Sintetize estes resultados:\n\n{combined}")

# Criar time colaborativo
team = CollaborativeAgents({
    "Analista Técnico": Agent(
        name="Analista Técnico",
        tools=[search_knowledge_base],
        instructions="Analise aspectos técnicos"
    ),
    "Analista de Mercado": Agent(
        name="Analista de Mercado",
        tools=[search_web],
        instructions="Analise perspectiva de mercado"
    ),
    "Analista Financeiro": Agent(
        name="Analista Financeiro",
        tools=[calculator, get_exchange_rate],
        instructions="Analise aspectos financeiros"
    )
})

# Executar análise colaborativa
task = "Avalie a viabilidade de lançar um produto de IA no Brasil"
results = team.run(task)
final_analysis = team.synthesize(results)

print(f"\n{'='*60}")
print("ANÁLISE FINAL:")
print(f"{'='*60}\n")
print(final_analysis)
```

---

## Capítulo 4.7: Configurações e Customizaçêo

### Configurando o Agente

```python
from agno import Agent

agent = Agent(
    # Identidade
    name="Assistente Executivo",
    description="Especialista em produtividade e gestêo",

    # Comportamento
    instructions="""
    Você é um assistente executivo altamente organizado.

    Suas prioridades:
    1. Precisêo sobre velocidade
    2. Proatividade
    3. Comunicaçêo clara e profissional

    Sempre:
    - Confirme entendimento antes de agir
    - Forneça resumos executivos
    - Sugira próximos passos
    """,

    # Modelo e parâmetros
    model="gpt-4",
    temperature=0.3,  # Mais determinístico

    # Tools
    tools=[...],

    # Memory
    memory=True,
    max_memory_messages=20,

    # Debugging
    show_tool_calls=True,
    debug_mode=False,

    # Limites de segurança
    max_iterations=10,
    timeout=60,  # segundos
)
```

### System Prompts Avançados

```python
agent = Agent(
    instructions="""
    # IDENTIDADE
    Você é Alex, um assistente de pesquisa acadêmica especializado
    em Ciência da Computaçêo e Inteligência Artificial.

    # CAPACIDADES
    - Buscar papers científicos
    - Resumir artigos técnicos
    - Explicar conceitos complexos de forma acessível
    - Citar fontes adequadamente

    # PROCESSO DE TRABALHO
    1. Entenda completamente a pergunta
    2. Se ambígua, peça esclarecimentos
    3. Use ferramentas para buscar informações atualizadas
    4. Sintetize findings de múltiplas fontes
    5. Forneça resposta estruturada com citações

    # RESTRIÇÕES
    - NUNCA invente citações ou referências
    - SEMPRE indique quando informaçêo é incerta
    - Admita limitações quando apropriado
    - Priorize qualidade sobre quantidade

    # TOM E ESTILO
    - Acadêmico mas acessível
    - Preciso e objetivo
    - Entusiasta mas profissional
    """,
    tools=[...],
    model="gpt-4"
)
```

### Callbacks e Hooks

```python
from agno import Agent
from agno.callbacks import CallbackHandler

class CustomCallback(CallbackHandler):
    """Callback customizado para logging avançado"""

    def on_agent_start(self, agent, input_text):
        print(f"🚀 Agente {agent.name} iniciado")
        print(f"📝 Input: {input_text}")

    def on_tool_start(self, tool_name, tool_input):
        print(f"🔧 Usando tool: {tool_name}")
        print(f"📥 Input: {tool_input}")

    def on_tool_end(self, tool_name, tool_output):
        print(f"✓ Tool {tool_name} completada")
        print(f"📤 Output: {tool_output[:100]}...")

    def on_agent_end(self, agent, output):
        print(f"✅ Agente {agent.name} finalizado")
        print(f"🎯 Resultado: {output}")

    def on_error(self, error):
        print(f"❌ Erro: {error}")

# Usar callback
agent = Agent(
    tools=[...],
    callbacks=[CustomCallback()]
)
```

---

## Capítulo 4.8: Best Practices e Padrões

### 1. Estrutura de Projeto

```
meu-projeto/
├── agents/
│   ├── __init__.py
│   ├── researcher_agent.py
│   ├── writer_agent.py
│   └── manager_agent.py
├── tools/
│   ├── __init__.py
│   ├── web_tools.py
│   ├── database_tools.py
│   └── file_tools.py
├── config/
│   ├── settings.py
│   └── prompts.py
├── storage/
│   └── agent_memory.db
├── main.py
├── requirements.txt
└── .env
```

### 2. Gerenciamento de Configurações

```python
# config/settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    # API Keys
    openai_api_key: str
    anthropic_api_key: str = None

    # Agente
    default_model: str = "gpt-4"
    default_temperature: float = 0.7
    max_iterations: int = 10

    # Storage
    storage_path: str = "./storage"
    database_url: str = "sqlite:///agent_memory.db"

    # Logging
    log_level: str = "INFO"
    show_tool_calls: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
```

### 3. Factory Pattern para Agentes

```python
# agents/__init__.py
from agno import Agent
from tools import web_tools, database_tools
from config.settings import settings

def create_researcher_agent():
    """Factory para criar agente pesquisador"""
    return Agent(
        name="Researcher",
        tools=[
            web_tools.search_web,
            web_tools.fetch_url,
            database_tools.query_knowledge_base
        ],
        model=settings.default_model,
        temperature=0.3,
        memory=True,
        show_tool_calls=settings.show_tool_calls
    )

def create_writer_agent():
    """Factory para criar agente escritor"""
    return Agent(
        name="Writer",
        tools=[
            database_tools.save_article,
            web_tools.check_plagiarism
        ],
        model=settings.default_model,
        temperature=0.7,
        memory=True
    )

def create_manager_agent():
    """Factory para criar agente gerente"""
    from .researcher_agent import create_researcher_agent
    from .writer_agent import create_writer_agent

    # Agentes como tools
    researcher = create_researcher_agent()
    writer = create_writer_agent()

    return Agent(
        name="Manager",
        tools=[
            researcher.as_tool(),
            writer.as_tool()
        ],
        model="gpt-4",
        memory=True
    )
```

### 4. Error Handling

```python
from agno import Agent, AgentError
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def run_agent_with_retry(agent, input_text):
    """Executa agente com retry automático"""
    try:
        return agent.run(input_text)
    except AgentError as e:
        print(f"⚠️ Erro do agente: {e}")
        raise
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        raise

# Uso
try:
    result = run_agent_with_retry(agent, "Pesquise sobre IA")
    print(result)
except Exception:
    print("Falha após 3 tentativas")
```

### 5. Testing

```python
import pytest
from agents import create_researcher_agent

@pytest.fixture
def researcher():
    """Fixture para agente pesquisador"""
    return create_researcher_agent()

def test_researcher_basic_query(researcher):
    """Testa consulta básica"""
    result = researcher.run("O que é Python?")
    assert "Python" in result
    assert len(result) > 100

def test_researcher_uses_tools(researcher, mocker):
    """Testa se agente usa ferramentas"""
    mock_search = mocker.patch('tools.web_tools.search_web')
    mock_search.return_value = "Python é uma linguagem..."

    result = researcher.run("Pesquise sobre Python")

    mock_search.assert_called_once()
    assert "Python" in result

def test_researcher_memory(researcher):
    """Testa memória do agente"""
    researcher.run("Meu nome é Joêo")
    result = researcher.run("Qual é meu nome?")
    assert "Joêo" in result
```

---

## 📝 Resumo Gráfico do Módulo 4

### Conceitos-Chave

**Filosofia Agno:**
- Simplicidade > Complexidade
- Foco > Generalizaçêo
- Transparência > Caixa-preta

**Componentes:**
```
Agent = Tools + Memory + Instructions + Model
```

**Patterns:**
1. Single Agent (1 agente, N tools)
2. Agent as Tool (agente usando agente)
3. Pipeline (sequência de agentes)
4. Collaborative (agentes em paralelo)

**Quando Usar:**
- ✅ Protótipos rápidos
- ✅ Agentes autônomos
- ✅ Código limpo e manutenível
- ✅ Time pequeno

---

## 🚀 Projeto Prático do Módulo 4

### Desafio: Assistente Pessoal Completo

**Objetivo:** Criar um assistente pessoal com múltiplas capacidades usando Agno.

#### Especificações

**Funcionalidades:**
1. Gerenciamento de tarefas (CRUD)
2. Lembretes e agenda
3. Notas e anotações
4. Busca de informações
5. Cálculos e conversões
6. Memory persistente

**Arquivo: `personal_assistant.py`**

```python
from agno import Agent, tool
from datetime import datetime, timedelta
import json
import os

# ============== STORAGE ==============

STORAGE_FILE = "assistant_data.json"

def load_data():
    """Carrega dados do arquivo"""
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"tasks": [], "notes": [], "reminders": []}

def save_data(data):
    """Salva dados no arquivo"""
    with open(STORAGE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ============== TASKS TOOLS ==============

@tool
def add_task(task: str, priority: str = "medium") -> str:
    """
    Adiciona uma nova tarefa.

    Args:
        task: Descriçêo da tarefa
        priority: Prioridade (low, medium, high)
    """
    data = load_data()
    task_obj = {
        "id": len(data["tasks"]) + 1,
        "description": task,
        "priority": priority,
        "created_at": datetime.now().isoformat(),
        "completed": False
    }
    data["tasks"].append(task_obj)
    save_data(data)
    return f"✓ Tarefa #{task_obj['id']} adicionada: '{task}' (prioridade: {priority})"

@tool
def list_tasks(filter_by: str = "all") -> str:
    """
    Lista tarefas.

    Args:
        filter_by: 'all', 'pending', 'completed', 'high', 'medium', 'low'
    """
    data = load_data()
    tasks = data["tasks"]

    if filter_by == "pending":
        tasks = [t for t in tasks if not t["completed"]]
    elif filter_by == "completed":
        tasks = [t for t in tasks if t["completed"]]
    elif filter_by in ["low", "medium", "high"]:
        tasks = [t for t in tasks if t["priority"] == filter_by]

    if not tasks:
        return "Nenhuma tarefa encontrada."

    result = f"Tarefas ({filter_by}):\n\n"
    for t in tasks:
        status = "✓" if t["completed"] else "○"
        result += f"{status} #{t['id']} [{t['priority']}] {t['description']}\n"

    return result

@tool
def complete_task(task_id: int) -> str:
    """
    Marca tarefa como concluída.

    Args:
        task_id: ID da tarefa
    """
    data = load_data()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["completed"] = True
            task["completed_at"] = datetime.now().isoformat()
            save_data(data)
            return f"✓ Tarefa #{task_id} concluída: '{task['description']}'"
    return f"Tarefa #{task_id} nêo encontrada."

@tool
def delete_task(task_id: int) -> str:
    """
    Remove uma tarefa.

    Args:
        task_id: ID da tarefa a remover
    """
    data = load_data()
    original_count = len(data["tasks"])
    data["tasks"] = [t for t in data["tasks"] if t["id"] != task_id]

    if len(data["tasks"]) < original_count:
        save_data(data)
        return f"✓ Tarefa #{task_id} removida."
    return f"Tarefa #{task_id} nêo encontrada."

# ============== NOTES TOOLS ==============

@tool
def create_note(title: str, content: str) -> str:
    """
    Cria uma nova nota.

    Args:
        title: Título da nota
        content: Conteúdo da nota
    """
    data = load_data()
    note = {
        "id": len(data["notes"]) + 1,
        "title": title,
        "content": content,
        "created_at": datetime.now().isoformat()
    }
    data["notes"].append(note)
    save_data(data)
    return f"✓ Nota '{title}' criada (ID: {note['id']})"

@tool
def list_notes() -> str:
    """Lista todas as notas."""
    data = load_data()
    notes = data["notes"]

    if not notes:
        return "Nenhuma nota encontrada."

    result = "Notas:\n\n"
    for n in notes:
        result += f"#{n['id']} - {n['title']}\n"
        result += f"   {n['content'][:100]}...\n\n"

    return result

@tool
def read_note(note_id: int) -> str:
    """
    Lê conteúdo completo de uma nota.

    Args:
        note_id: ID da nota
    """
    data = load_data()
    for note in data["notes"]:
        if note["id"] == note_id:
            return f"**{note['title']}**\n\n{note['content']}"
    return f"Nota #{note_id} nêo encontrada."

# ============== REMINDER TOOLS ==============

@tool
def set_reminder(message: str, when: str) -> str:
    """
    Define um lembrete.

    Args:
        message: Mensagem do lembrete
        when: Quando lembrar (ex: 'tomorrow 9am', 'in 2 hours')
    """
    data = load_data()
    # Simplificado: apenas armazenar
    reminder = {
        "id": len(data["reminders"]) + 1,
        "message": message,
        "when": when,
        "created_at": datetime.now().isoformat()
    }
    data["reminders"].append(reminder)
    save_data(data)
    return f"✓ Lembrete definido: '{message}' para {when}"

@tool
def list_reminders() -> str:
    """Lista todos os lembretes."""
    data = load_data()
    reminders = data["reminders"]

    if not reminders:
        return "Nenhum lembrete definido."

    result = "Lembretes:\n\n"
    for r in reminders:
        result += f"#{r['id']} - {r['message']} ({r['when']})\n"

    return result

# ============== UTILITY TOOLS ==============

@tool
def calculator(expression: str) -> str:
    """
    Calcula expressões matemáticas.

    Args:
        expression: Expressêo matemática
    """
    try:
        result = eval(expression)
        return f"Resultado: {result}"
    except Exception as e:
        return f"Erro: {str(e)}"

@tool
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """
    Converte moedas (simplificado).

    Args:
        amount: Valor a converter
        from_currency: Moeda de origem (USD, EUR, BRL)
        to_currency: Moeda de destino
    """
    # Taxas simplificadas (usar API real em produçêo)
    rates = {
        ("USD", "BRL"): 5.0,
        ("USD", "EUR"): 0.9,
        ("EUR", "BRL"): 5.5,
        ("EUR", "USD"): 1.1,
        ("BRL", "USD"): 0.2,
        ("BRL", "EUR"): 0.18
    }

    key = (from_currency.upper(), to_currency.upper())
    if key in rates:
        result = amount * rates[key]
        return f"{amount} {from_currency} = {result:.2f} {to_currency}"

    return f"Conversêo {from_currency} → {to_currency} nêo disponível."

# ============== CREATE AGENT ==============

assistant = Agent(
    name="Assistente Pessoal",
    description="Ajuda com tarefas, notas, lembretes e utilidades",

    instructions="""
    Você é um assistente pessoal eficiente e organizado.

    SUAS CAPACIDADES:
    - Gerenciar tarefas (criar, listar, completar, remover)
    - Criar e organizar notas
    - Definir lembretes
    - Fazer cálculos
    - Converter moedas

    COMPORTAMENTO:
    - Seja proativo: sugira organizaçêo e priorizaçêo
    - Confirme ações antes de executar (ex: "Vou adicionar a tarefa X, ok?")
    - Forneça resumos quando listar itens
    - Use emojis para tornar respostas mais amigáveis

    EXEMPLOS:
    - "Adicione 'comprar leite' às tarefas" → use add_task
    - "O que tenho que fazer hoje?" → use list_tasks(filter_by="pending")
    - "Marque a tarefa 3 como feita" → use complete_task(3)
    - "Lembre-me de ligar para Joêo amanhê" → use set_reminder
    """,

    tools=[
        # Tasks
        add_task,
        list_tasks,
        complete_task,
        delete_task,

        # Notes
        create_note,
        list_notes,
        read_note,

        # Reminders
        set_reminder,
        list_reminders,

        # Utilities
        calculator,
        convert_currency
    ],

    model="gpt-4",
    temperature=0.7,
    memory=True,
    show_tool_calls=True
)

# ============== MAIN ==============

if __name__ == "__main__":
    print("="*60)
    print("🤖 ASSISTENTE PESSOAL AGNO")
    print("="*60)
    print("\nDiga 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ").strip()

        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("\n👋 Até logo!")
            break

        if not user_input:
            continue

        try:
            response = assistant.run(user_input)
            print(f"\n🤖 Assistente: {response}\n")
            print("-"*60)

        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            break

        except Exception as e:
            print(f"\n❌ Erro: {e}\n")
```

#### Como Executar

```bash
# 1. Instalar dependências
pip install agno python-dotenv

# 2. Configurar .env
echo "OPENAI_API_KEY=sk-..." > .env

# 3. Executar
python personal_assistant.py
```

#### Exemplos de Uso

```
Você: Adicione "estudar Python" às minhas tarefas com alta prioridade

🤖 Assistente: ✓ Tarefa #1 adicionada: 'estudar Python' (prioridade: high)

---

Você: Liste minhas tarefas pendentes

🤖 Assistente: Tarefas (pending):

○ #1 [high] estudar Python

---

Você: Quanto é 25 * 17?

🤖 Assistente: Resultado: 425

---

Você: Converta 100 dólares para reais

🤖 Assistente: 100 USD = 500.00 BRL

---

Você: Crie uma nota chamada "Ideias" com o conteúdo "Criar app de produtividade"

🤖 Assistente: ✓ Nota 'Ideias' criada (ID: 1)

---

Você: Lembre-me de fazer exercícios amanhê às 7h

🤖 Assistente: ✓ Lembrete definido: 'fazer exercícios' para tomorrow 7am
```

---

## 💡 Conclusões e Próximos Passos

### O que você aprendeu:

✓ Filosofia de simplicidade do Agno
✓ Criar agentes com código minimalista
✓ Desenvolver tools customizadas
✓ Implementar memory e storage
✓ RAG simplificado
✓ Sistemas multi-agentes
✓ Best practices e patterns
✓ Projeto completo production-ready

### Agno vs LangChain: Veredito

**Use Agno quando:**
- Velocidade de desenvolvimento é crítica
- Foco em agentes autônomos
- Clareza > Flexibilidade
- Equipe pequena

**Use LangChain quando:**
- Necessita ecossistema completo
- Pipelines complexos de dados
- Múltiplas integrações especializadas
- Recursos avançados específicos

**Use ambos quando:**
- Melhor ferramenta para cada job
- Sistema híbrido

---

**No Módulo 5**, vamos explorar **CrewAI**, o framework especializado em orquestrar **equipes de agentes** que colaboram como uma tripulaçêo profissional, cada um com papel e expertise específicos, trabalhando juntos para resolver problemas complexos de forma coordenada.

---

**Continue para o Módulo 5: Sistemas Multi-Agentes com CrewAI** →
