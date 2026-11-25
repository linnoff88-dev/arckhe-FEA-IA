# Módulo 6: Model Context Protocol (MCP)

## Conectando Agentes ao Mundo Real

> "A verdadeira inteligência nêo vem apenas do modelo, mas das conexões que ele pode fazer com o mundo." - Princípio fundamental do MCP

---

## 📋 Índice

1. [Introduçêo ao MCP](#61-introduçêo-ao-mcp)
2. [Arquitetura do MCP](#62-arquitetura-do-mcp)
3. [Criando Servidores MCP](#63-criando-servidores-mcp)
4. [Criando Clientes MCP](#64-criando-clientes-mcp)
5. [Recursos e Prompts](#65-recursos-e-prompts)
6. [Tools no MCP](#66-tools-no-mcp)
7. [Integraçêo com Agentes](#67-integraçêo-com-agentes)
8. [Segurança e Autenticaçêo](#68-segurança-e-autenticaçêo)
9. [Projeto Prático: Sistema de Gestêo de Projetos com MCP](#69-projeto-prático)
10. [Resumo e Próximos Passos](#610-resumo-e-próximos-passos)

---

## 6.1 Introduçêo ao MCP

### 6.1.1 O Que É o Model Context Protocol?

O **Model Context Protocol (MCP)** é um protocolo aberto desenvolvido pela Anthropic que define uma maneira padronizada para que aplicações de IA se conectem a fontes de dados e ferramentas externas.

**Analogia:** Se os LLMs sêo "cérebros", o MCP é o "sistema nervoso" que conecta esse cérebro aos "órgêos sensoriais" e "membros" - permitindo que o agente veja (dados) e aja (ferramentas) no mundo real.

### 6.1.2 Por Que MCP É Importante?

**Problema antes do MCP:**

```python
# Cada ferramenta tinha sua própria integraçêo
chatbot.add_tool(custom_database_connector())
chatbot.add_tool(custom_api_wrapper())
chatbot.add_tool(custom_file_reader())
# Resultado: código fragmentado, difícil de manter
```

**Soluçêo com MCP:**

```python
# Protocolo unificado
mcp_client.connect_to_server("sqlite://local.db")
mcp_client.connect_to_server("api://github.com")
mcp_client.connect_to_server("file://~/documents")
# Resultado: interface consistente e reutilizável
```

### 6.1.3 Casos de Uso Principais

1. **Acesso a Dados Empresariais**
   - Conectar agentes a bancos de dados corporativos
   - Acessar sistemas CRM, ERP
   - Integraçêo com data warehouses

2. **Automaçêo de Ferramentas**
   - Executar comandos no sistema operacional
   - Gerenciar serviços em nuvem
   - Controlar APIs de terceiros

3. **Sistemas de Conhecimento**
   - RAG com fontes de dados dinâmicas
   - Acesso a documentaçêo técnica atualizada
   - Bases de conhecimento corporativas

4. **Agentes Autônomos**
   - Agentes que operam em ambientes reais
   - Robôs de atendimento com acesso a sistemas
   - Assistentes pessoais conectados

### 6.1.4 Componentes Principais

```
┌─────────────────────────────────────────────────────────────┐
│                        MCP ECOSYSTEM                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐         MCP Protocol        ┌──────────┐ │
│  │              │  ◄─────────────────────────► │          │ │
│  │  MCP Client  │                              │   MCP    │ │
│  │  (seu app)   │  ◄─────────────────────────► │  Server  │ │
│  │              │    Resources, Tools,         │          │ │
│  └──────────────┘    Prompts                   └──────────┘ │
│        │                                             │      │
│        │                                             │      │
│        ▼                                             ▼      │
│  ┌──────────┐                              ┌──────────────┐│
│  │   LLM    │                              │ Data Sources ││
│  │ (Claude) │                              │  & Tools     ││
│  └──────────┘                              └──────────────┘│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.1.5 Principais Vantagens

✅ **Padronizaçêo**: Uma interface única para todos os tipos de integrações
✅ **Reutilizaçêo**: Servidores MCP podem ser usados por múltiplas aplicações
✅ **Segurança**: Controle granular de permissões e autenticaçêo
✅ **Escalabilidade**: Fácil adicionar novas fontes de dados
✅ **Manutenibilidade**: Separaçêo clara entre cliente e servidor

---

## 6.2 Arquitetura do MCP

### 6.2.1 Visêo Geral da Arquitetura

O MCP segue uma arquitetura **cliente-servidor** baseada em **JSON-RPC 2.0**.

```
┌────────────────────────────────────────────────────────────────┐
│                     MCP ARCHITECTURE                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   CLIENT SIDE                 │           SERVER SIDE          │
│                               │                                │
│  ┌─────────────────┐          │        ┌─────────────────┐    │
│  │  Application    │          │        │  MCP Server     │    │
│  │  (Claude, etc)  │          │        │                 │    │
│  └────────┬────────┘          │        └────────┬────────┘    │
│           │                   │                 │             │
│  ┌────────▼────────┐          │        ┌────────▼────────┐    │
│  │  MCP Client     │  JSON-RPC│        │  Protocol       │    │
│  │  Implementation │◄─────────┼────────►│  Handler        │    │
│  └─────────────────┘          │        └────────┬────────┘    │
│                               │                 │             │
│                               │        ┌────────▼────────┐    │
│                               │        │  Resources      │    │
│                               │        │  Tools          │    │
│                               │        │  Prompts        │    │
│                               │        └────────┬────────┘    │
│                               │                 │             │
│                               │        ┌────────▼────────┐    │
│                               │        │  Data Sources   │    │
│                               │        │  (DB, API, FS)  │    │
│                               │        └─────────────────┘    │
│                               │                                │
└────────────────────────────────────────────────────────────────┘
```

### 6.2.2 Conceitos Fundamentais

#### Resources (Recursos)

Resources sêo **dados** que o servidor expõe ao cliente.

```python
# Exemplo conceitual de um resource
{
  "uri": "project://tasks/12345",
  "name": "Task #12345",
  "mimeType": "application/json",
  "description": "Detalhes da tarefa de desenvolvimento"
}
```

**Características:**
- Representam dados que podem ser lidos
- Identificados por URIs únicas
- Podem ter diferentes formatos (JSON, texto, binário)
- Suportam versionamento

#### Tools (Ferramentas)

Tools sêo **ações** que o servidor pode executar.

```python
# Exemplo conceitual de uma tool
{
  "name": "create_task",
  "description": "Cria uma nova tarefa no sistema",
  "inputSchema": {
    "type": "object",
    "properties": {
      "title": {"type": "string"},
      "priority": {"type": "string", "enum": ["low", "medium", "high"]}
    },
    "required": ["title"]
  }
}
```

**Características:**
- Representam operações que modificam estado
- Podem receber parâmetros
- Retornam resultados estruturados
- Podem ter efeitos colaterais

#### Prompts (Prompts Pré-configurados)

Prompts sêo **templates** reutilizáveis que o servidor oferece.

```python
# Exemplo conceitual de um prompt
{
  "name": "analyze_project_status",
  "description": "Analisa o status atual do projeto",
  "arguments": [
    {"name": "project_id", "required": true}
  ]
}
```

**Características:**
- Templates de prompts otimizados
- Podem incluir contexto específico
- Reutilizáveis entre aplicações
- Podem ter parâmetros dinâmicos

### 6.2.3 Protocolo de Comunicaçêo

O MCP usa **JSON-RPC 2.0** sobre transporte **stdio** ou **HTTP/SSE**.

**Exemplo de mensagem de requisiçêo:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_task",
    "arguments": {
      "title": "Implementar autenticaçêo",
      "priority": "high"
    }
  }
}
```

**Exemplo de mensagem de resposta:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "✓ Tarefa criada com sucesso! ID: #12348"
      }
    ]
  }
}
```

### 6.2.4 Ciclo de Vida de uma Conexêo

```
1. INITIALIZE
   Client ──────► Server
   (Handshake, troca de capacidades)

2. INITIALIZED
   Server ──────► Client
   (Confirmaçêo, recursos disponíveis)

3. OPERATION PHASE
   Client ◄────► Server
   (Resources/Tools/Prompts)

4. SHUTDOWN
   Client ──────► Server
   (Encerramento gracioso)
```

### 6.2.5 Tipos de Transporte

**1. STDIO (Standard Input/Output)**

```python
# Servidor roda como subprocess
# Cliente comunica via stdin/stdout
import subprocess
server_process = subprocess.Popen(
    ["python", "mcp_server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE
)
```

**Vantagens:**
- Simples de implementar
- Baixa latência
- Ideal para processos locais

**Desvantagens:**
- Nêo funciona através de rede
- Um cliente por servidor

**2. HTTP + Server-Sent Events (SSE)**

```python
# Servidor HTTP que envia eventos
# Cliente conecta via HTTP
import requests
response = requests.post(
    "http://localhost:8000/mcp",
    json=rpc_request,
    stream=True
)
```

**Vantagens:**
- Funciona através de rede
- Múltiplos clientes
- Compatível com infraestrutura web

**Desvantagens:**
- Maior overhead
- Mais complexo de configurar

---

## 6.3 Criando Servidores MCP

### 6.3.1 Setup Inicial

Vamos criar um servidor MCP do zero usando Python.

**Instalaçêo:**

```bash
pip install mcp anthropic-mcp
```

**Estrutura de diretórios:**

```
my_mcp_server/
├── server.py           # Código principal do servidor
├── tools.py            # Definições de tools
├── resources.py        # Definições de resources
├── prompts.py          # Definições de prompts
└── requirements.txt
```

### 6.3.2 Servidor Básico

**server.py:**

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    Resource,
    Prompt,
    TextContent,
    ImageContent,
    EmbeddedResource
)
import asyncio
import json

# Criar instância do servidor
app = Server("my-project-manager")

# ============================================================================
# TOOLS
# ============================================================================

@app.list_tools()
async def list_tools() -> list[Tool]:
    """Lista todas as tools disponíveis"""
    return [
        Tool(
            name="create_task",
            description="Cria uma nova tarefa no sistema de gestêo de projetos",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Título da tarefa"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descriçêo detalhada da tarefa"
                    },
                    "priority": {
                        "type": "string",
                        "enum": ["low", "medium", "high", "urgent"],
                        "description": "Prioridade da tarefa"
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Pessoa responsável pela tarefa"
                    }
                },
                "required": ["title", "priority"]
            }
        ),
        Tool(
            name="list_tasks",
            description="Lista todas as tarefas, com filtros opcionais",
            inputSchema={
                "type": "object",
                "properties": {
                    "status": {
                        "type": "string",
                        "enum": ["pending", "in_progress", "completed", "blocked"],
                        "description": "Filtrar por status"
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Filtrar por responsável"
                    }
                }
            }
        ),
        Tool(
            name="update_task",
            description="Atualiza uma tarefa existente",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "ID da tarefa"
                    },
                    "status": {
                        "type": "string",
                        "enum": ["pending", "in_progress", "completed", "blocked"]
                    },
                    "notes": {
                        "type": "string",
                        "description": "Notas sobre a atualizaçêo"
                    }
                },
                "required": ["task_id"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Executa uma tool"""

    if name == "create_task":
        # Lógica para criar tarefa
        task_id = generate_task_id()
        task = {
            "id": task_id,
            "title": arguments["title"],
            "description": arguments.get("description", ""),
            "priority": arguments["priority"],
            "assignee": arguments.get("assignee"),
            "status": "pending",
            "created_at": datetime.now().isoformat()
        }

        # Salvar no banco de dados (simulado aqui)
        save_task(task)

        return [
            TextContent(
                type="text",
                text=f"✓ Tarefa criada com sucesso!\n\n"
                     f"ID: {task_id}\n"
                     f"Título: {task['title']}\n"
                     f"Prioridade: {task['priority']}\n"
                     f"Status: {task['status']}"
            )
        ]

    elif name == "list_tasks":
        # Lógica para listar tarefas
        tasks = get_tasks(
            status=arguments.get("status"),
            assignee=arguments.get("assignee")
        )

        if not tasks:
            return [TextContent(type="text", text="Nenhuma tarefa encontrada.")]

        # Formatar lista de tarefas
        task_list = []
        for task in tasks:
            task_list.append(
                f"[{task['id']}] {task['title']}\n"
                f"  Status: {task['status']} | Prioridade: {task['priority']}\n"
                f"  Responsável: {task.get('assignee', 'Nêo atribuído')}"
            )

        return [
            TextContent(
                type="text",
                text=f"📋 **Tarefas encontradas: {len(tasks)}**\n\n" + "\n\n".join(task_list)
            )
        ]

    elif name == "update_task":
        # Lógica para atualizar tarefa
        task_id = arguments["task_id"]
        task = get_task_by_id(task_id)

        if not task:
            return [TextContent(type="text", text=f"❌ Tarefa {task_id} nêo encontrada.")]

        # Atualizar campos
        if "status" in arguments:
            task["status"] = arguments["status"]
        if "notes" in arguments:
            task["notes"] = arguments["notes"]

        update_task(task)

        return [
            TextContent(
                type="text",
                text=f"✓ Tarefa {task_id} atualizada com sucesso!\n"
                     f"Novo status: {task['status']}"
            )
        ]

    else:
        raise ValueError(f"Tool desconhecida: {name}")

# ============================================================================
# RESOURCES
# ============================================================================

@app.list_resources()
async def list_resources() -> list[Resource]:
    """Lista todos os resources disponíveis"""
    return [
        Resource(
            uri="project://dashboard",
            name="Project Dashboard",
            mimeType="application/json",
            description="Visêo geral do projeto com estatísticas"
        ),
        Resource(
            uri="project://tasks/all",
            name="All Tasks",
            mimeType="application/json",
            description="Lista completa de todas as tarefas"
        ),
        Resource(
            uri="project://team",
            name="Team Members",
            mimeType="application/json",
            description="Lista de membros da equipe"
        )
    ]

@app.read_resource()
async def read_resource(uri: str) -> str:
    """Lê um resource específico"""

    if uri == "project://dashboard":
        tasks = get_all_tasks()
        stats = {
            "total_tasks": len(tasks),
            "pending": len([t for t in tasks if t["status"] == "pending"]),
            "in_progress": len([t for t in tasks if t["status"] == "in_progress"]),
            "completed": len([t for t in tasks if t["status"] == "completed"]),
            "blocked": len([t for t in tasks if t["status"] == "blocked"])
        }
        return json.dumps(stats, indent=2)

    elif uri == "project://tasks/all":
        tasks = get_all_tasks()
        return json.dumps(tasks, indent=2)

    elif uri == "project://team":
        team = get_team_members()
        return json.dumps(team, indent=2)

    else:
        raise ValueError(f"Resource nêo encontrado: {uri}")

# ============================================================================
# PROMPTS
# ============================================================================

@app.list_prompts()
async def list_prompts() -> list[Prompt]:
    """Lista todos os prompts disponíveis"""
    return [
        Prompt(
            name="daily_standup",
            description="Gera um relatório de standup diário",
            arguments=[
                {
                    "name": "team_member",
                    "description": "Nome do membro da equipe (opcional)",
                    "required": False
                }
            ]
        ),
        Prompt(
            name="sprint_planning",
            description="Ajuda no planejamento de sprint",
            arguments=[
                {
                    "name": "sprint_number",
                    "description": "Número do sprint",
                    "required": True
                }
            ]
        )
    ]

@app.get_prompt()
async def get_prompt(name: str, arguments: dict) -> str:
    """Retorna um prompt específico"""

    if name == "daily_standup":
        team_member = arguments.get("team_member")

        if team_member:
            tasks = get_tasks(assignee=team_member)
        else:
            tasks = get_all_tasks()

        prompt = f"""# Daily Standup Report

**Data:** {datetime.now().strftime("%d/%m/%Y")}

## Tarefas em Progresso
"""
        in_progress = [t for t in tasks if t["status"] == "in_progress"]
        for task in in_progress:
            prompt += f"\n- [{task['id']}] {task['title']} ({task.get('assignee', 'Nêo atribuído')})"

        prompt += "\n\n## Tarefas Completadas Recentemente\n"
        completed = [t for t in tasks if t["status"] == "completed"][:5]
        for task in completed:
            prompt += f"\n- [{task['id']}] {task['title']}"

        prompt += "\n\n## Bloqueios\n"
        blocked = [t for t in tasks if t["status"] == "blocked"]
        if blocked:
            for task in blocked:
                prompt += f"\n- [{task['id']}] {task['title']} - {task.get('block_reason', 'Motivo nêo especificado')}"
        else:
            prompt += "\nNenhum bloqueio identificado."

        prompt += "\n\nPor favor, analise este relatório e forneça insights sobre o progresso da equipe."

        return prompt

    elif name == "sprint_planning":
        sprint_number = arguments["sprint_number"]

        # Buscar dados relevantes
        pending_tasks = get_tasks(status="pending")
        team_capacity = calculate_team_capacity()

        prompt = f"""# Sprint Planning - Sprint {sprint_number}

## Capacidade da Equipe
{json.dumps(team_capacity, indent=2)}

## Tarefas Disponíveis ({len(pending_tasks)})
"""
        for task in pending_tasks[:10]:  # Top 10
            prompt += f"\n- [{task['priority']}] {task['title']}"

        prompt += "\n\nCom base nestas informações, sugira quais tarefas devem ser incluídas no próximo sprint, considerando prioridades e capacidade da equipe."

        return prompt

    else:
        raise ValueError(f"Prompt nêo encontrado: {name}")

# ============================================================================
# FUNÇÕES AUXILIARES (Simulaçêo de Banco de Dados)
# ============================================================================

# Banco de dados em memória (em produçêo, use um DB real)
TASKS_DB = []
TEAM_DB = [
    {"name": "Alice", "role": "Developer", "capacity_hours": 40},
    {"name": "Bob", "role": "Designer", "capacity_hours": 40},
    {"name": "Carol", "role": "Developer", "capacity_hours": 32}
]

import uuid
from datetime import datetime

def generate_task_id():
    return str(uuid.uuid4())[:8]

def save_task(task):
    TASKS_DB.append(task)

def get_all_tasks():
    return TASKS_DB

def get_tasks(status=None, assignee=None):
    tasks = TASKS_DB

    if status:
        tasks = [t for t in tasks if t["status"] == status]

    if assignee:
        tasks = [t for t in tasks if t.get("assignee") == assignee]

    return tasks

def get_task_by_id(task_id):
    for task in TASKS_DB:
        if task["id"] == task_id:
            return task
    return None

def update_task(updated_task):
    for i, task in enumerate(TASKS_DB):
        if task["id"] == updated_task["id"]:
            TASKS_DB[i] = updated_task
            return True
    return False

def get_team_members():
    return TEAM_DB

def calculate_team_capacity():
    total_hours = sum(member["capacity_hours"] for member in TEAM_DB)
    return {
        "total_hours": total_hours,
        "members": TEAM_DB
    }

# ============================================================================
# MAIN
# ============================================================================

async def main():
    """Inicia o servidor MCP via stdio"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### 6.3.3 Testando o Servidor

**1. Teste manual via stdio:**

```bash
# Terminal 1: Rodar o servidor
python server.py
```

**2. Criar um cliente de teste:**

```python
# test_client.py
import subprocess
import json

def send_request(process, request):
    """Envia requisiçêo JSON-RPC para o servidor"""
    request_json = json.dumps(request) + "\n"
    process.stdin.write(request_json.encode())
    process.stdin.flush()

    # Ler resposta
    response_line = process.stdout.readline()
    return json.loads(response_line)

# Iniciar servidor como subprocess
server = subprocess.Popen(
    ["python", "server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# 1. Initialize
init_request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {
            "name": "test-client",
            "version": "1.0.0"
        }
    }
}

response = send_request(server, init_request)
print("Initialize:", json.dumps(response, indent=2))

# 2. Listar tools
tools_request = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list",
    "params": {}
}

response = send_request(server, tools_request)
print("\nTools:", json.dumps(response, indent=2))

# 3. Chamar uma tool
call_request = {
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "create_task",
        "arguments": {
            "title": "Implementar autenticaçêo OAuth",
            "priority": "high",
            "assignee": "Alice"
        }
    }
}

response = send_request(server, call_request)
print("\nCall Tool:", json.dumps(response, indent=2))

# Encerrar
server.terminate()
```

### 6.3.4 Boas Práticas para Servidores

**1. Validaçêo de Entrada**

```python
def validate_task_input(arguments: dict):
    """Valida entrada de create_task"""
    if not arguments.get("title"):
        raise ValueError("Título é obrigatório")

    if len(arguments["title"]) < 3:
        raise ValueError("Título deve ter pelo menos 3 caracteres")

    valid_priorities = ["low", "medium", "high", "urgent"]
    if arguments["priority"] not in valid_priorities:
        raise ValueError(f"Prioridade inválida. Use: {', '.join(valid_priorities)}")

    return True
```

**2. Tratamento de Erros**

```python
@app.call_tool()
async def call_tool(name: str, arguments: dict):
    try:
        if name == "create_task":
            validate_task_input(arguments)
            # ... resto da lógica

    except ValueError as e:
        return [
            TextContent(
                type="text",
                text=f"❌ Erro de validaçêo: {str(e)}"
            )
        ]
    except Exception as e:
        # Log do erro
        logger.error(f"Erro ao executar tool {name}: {e}")
        return [
            TextContent(
                type="text",
                text=f"❌ Erro interno ao executar a operaçêo. Tente novamente."
            )
        ]
```

**3. Logging e Observabilidade**

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    logger.info(f"Tool chamada: {name} com argumentos: {arguments}")

    start_time = time.time()
    result = # ... execuçêo
    duration = time.time() - start_time

    logger.info(f"Tool {name} executada em {duration:.2f}s")
    return result
```

**4. Rate Limiting**

```python
from collections import defaultdict
import time

# Limitar a 10 requisições por minuto por tool
rate_limits = defaultdict(list)

def check_rate_limit(tool_name: str, max_calls=10, window_seconds=60):
    now = time.time()

    # Remover chamadas antigas
    rate_limits[tool_name] = [
        timestamp for timestamp in rate_limits[tool_name]
        if now - timestamp < window_seconds
    ]

    if len(rate_limits[tool_name]) >= max_calls:
        raise Exception(f"Rate limit excedido para {tool_name}")

    rate_limits[tool_name].append(now)
```

---

## 6.4 Criando Clientes MCP

### 6.4.1 Cliente Python Básico

```python
# mcp_client.py
from mcp.client import Client
from mcp.client.stdio import stdio_client
import asyncio

async def main():
    # Conectar ao servidor MCP via stdio
    async with stdio_client("python", ["server.py"]) as (read, write):
        async with Client(read, write) as client:

            # 1. Inicializar
            await client.initialize()

            # 2. Listar tools disponíveis
            tools = await client.list_tools()
            print("Tools disponíveis:")
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")

            # 3. Chamar uma tool
            result = await client.call_tool(
                "create_task",
                arguments={
                    "title": "Implementar login social",
                    "priority": "medium",
                    "assignee": "Bob"
                }
            )

            print("\nResultado:")
            for content in result.content:
                print(content.text)

            # 4. Ler um resource
            dashboard = await client.read_resource("project://dashboard")
            print("\nDashboard:")
            print(dashboard)

            # 5. Obter um prompt
            standup_prompt = await client.get_prompt(
                "daily_standup",
                arguments={"team_member": "Alice"}
            )
            print("\nPrompt de Standup:")
            print(standup_prompt)

if __name__ == "__main__":
    asyncio.run(main())
```

### 6.4.2 Integraçêo com Claude Desktop

O Claude Desktop pode se conectar a servidores MCP através de configuraçêo.

**Arquivo de configuraçêo (claude_desktop_config.json):**

```json
{
  "mcpServers": {
    "project-manager": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {
        "DATABASE_URL": "sqlite:///projects.db"
      }
    },
    "github-integration": {
      "command": "node",
      "args": ["/path/to/github-mcp-server.js"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxxxxxxxxxxxx"
      }
    }
  }
}
```

**Como usar no Claude Desktop:**

1. Abra o Claude Desktop
2. Configure o arquivo acima em `~/.config/claude-desktop/config.json`
3. Reinicie o Claude Desktop
4. Agora você pode usar as tools do servidor MCP diretamente:

```
Usuário: "Crie uma tarefa de alta prioridade para implementar autenticaçêo"

Claude: [Usa automaticamente a tool create_task do MCP server]
✓ Tarefa criada com sucesso!
ID: a3f2b8c1
Título: Implementar autenticaçêo
Prioridade: high
Status: pending
```

### 6.4.3 Cliente Web com SSE

Para servidores HTTP com SSE:

```python
# web_client.py
import requests
import json
import sseclient

class MCPWebClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.request_id = 0

    def _next_id(self):
        self.request_id += 1
        return self.request_id

    def call_tool(self, tool_name, arguments):
        """Chama uma tool via HTTP"""
        request = {
            "jsonrpc": "2.0",
            "id": self._next_id(),
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            }
        }

        response = requests.post(
            f"{self.server_url}/mcp",
            json=request,
            headers={"Content-Type": "application/json"}
        )

        return response.json()

    def subscribe_to_events(self):
        """Inscreve-se para receber eventos via SSE"""
        response = requests.get(
            f"{self.server_url}/events",
            stream=True,
            headers={"Accept": "text/event-stream"}
        )

        client = sseclient.SSEClient(response)

        for event in client.events():
            print(f"Event: {event.event}")
            print(f"Data: {event.data}")
            yield json.loads(event.data)

# Uso
client = MCPWebClient("http://localhost:8000")

result = client.call_tool("create_task", {
    "title": "Tarefa de exemplo",
    "priority": "low"
})

print(result)
```

### 6.4.4 Cliente com Retry e Circuit Breaker

Para produçêo, implemente resiliência:

```python
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

class ResilientMCPClient:
    def __init__(self, server_command, server_args):
        self.server_command = server_command
        self.server_args = server_args
        self.circuit_breaker_failures = 0
        self.circuit_breaker_threshold = 5
        self.circuit_open = False

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10)
    )
    async def call_tool_with_retry(self, client, tool_name, arguments):
        """Chama tool com retry automático"""
        if self.circuit_open:
            raise Exception("Circuit breaker está aberto")

        try:
            result = await client.call_tool(tool_name, arguments)

            # Reset em caso de sucesso
            self.circuit_breaker_failures = 0

            return result

        except Exception as e:
            self.circuit_breaker_failures += 1

            if self.circuit_breaker_failures >= self.circuit_breaker_threshold:
                self.circuit_open = True
                print("⚠️ Circuit breaker ABERTO - muitas falhas consecutivas")

            raise e

    async def reset_circuit_breaker(self):
        """Tenta fechar o circuit breaker após um tempo"""
        await asyncio.sleep(30)  # Espera 30s
        self.circuit_open = False
        self.circuit_breaker_failures = 0
        print("✓ Circuit breaker FECHADO - pronto para novas tentativas")
```

---

## 6.5 Recursos e Prompts

### 6.5.1 Design de Resources Eficazes

**Princípios:**

1. **URIs Descritivas e Hierárquicas**

```python
# ✅ BOM
"project://tasks/12345"
"project://sprints/sprint-23/burndown"
"project://team/alice/workload"

# ❌ RUIM
"resource1"
"data"
"info"
```

2. **Versionamento de Resources**

```python
@app.read_resource()
async def read_resource(uri: str) -> str:
    # Suportar versionamento na URI
    if uri.startswith("project://tasks/v2/"):
        return get_tasks_v2(uri)
    elif uri.startswith("project://tasks/"):
        return get_tasks_v1(uri)  # Legacy
    else:
        raise ValueError(f"URI nêo reconhecida: {uri}")
```

3. **Metadados Ricos**

```python
Resource(
    uri="project://sprint/23",
    name="Sprint 23 - Q4 2024",
    mimeType="application/json",
    description="Dados completos do sprint 23, incluindo tarefas, métricas e retrospectiva",
    metadata={
        "start_date": "2024-10-01",
        "end_date": "2024-10-14",
        "status": "completed",
        "team_size": 5
    }
)
```

### 6.5.2 Templates de Resources Comuns

**1. Dashboard/Analytics Resource**

```python
@app.read_resource()
async def read_resource(uri: str) -> str:
    if uri == "project://analytics/weekly":
        data = {
            "period": "2024-W42",
            "metrics": {
                "velocity": 32,
                "completed_stories": 12,
                "bugs_fixed": 8,
                "code_reviews": 24
            },
            "trends": {
                "velocity_change": "+12%",
                "quality_score": 94
            },
            "top_contributors": [
                {"name": "Alice", "commits": 47},
                {"name": "Bob", "commits": 38}
            ]
        }
        return json.dumps(data, indent=2)
```

**2. Configuration Resource**

```python
@app.read_resource()
async def read_resource(uri: str) -> str:
    if uri == "project://config":
        config = {
            "project_name": "E-commerce Platform",
            "sprint_duration_days": 14,
            "default_priority": "medium",
            "allowed_labels": ["bug", "feature", "improvement", "tech-debt"],
            "notification_channels": {
                "slack": "#dev-team",
                "email": "team@company.com"
            }
        }
        return json.dumps(config, indent=2)
```

**3. Documentation Resource**

```python
@app.read_resource()
async def read_resource(uri: str) -> str:
    if uri.startswith("project://docs/"):
        doc_name = uri.replace("project://docs/", "")

        docs = {
            "api": "# API Documentation\n\n...",
            "setup": "# Setup Guide\n\n1. Install dependencies...",
            "contributing": "# Contributing\n\n## Code Style..."
        }

        return docs.get(doc_name, "Documentation not found")
```

### 6.5.3 Prompts Dinâmicos

**1. Prompt com Contexto Rico**

```python
@app.get_prompt()
async def get_prompt(name: str, arguments: dict) -> str:
    if name == "code_review_assistant":
        pr_number = arguments["pr_number"]

        # Buscar dados do PR
        pr_data = get_pull_request(pr_number)
        changed_files = get_changed_files(pr_number)

        prompt = f"""# Code Review Assistant - PR #{pr_number}

## Pull Request Information
- **Title:** {pr_data['title']}
- **Author:** {pr_data['author']}
- **Target Branch:** {pr_data['target_branch']}
- **Files Changed:** {len(changed_files)}

## Changed Files
"""
        for file in changed_files:
            prompt += f"\n- {file['path']} (+{file['additions']} -{file['deletions']})"

        prompt += """

## Review Guidelines
Please review this PR considering:

1. **Code Quality**
   - Follows project coding standards?
   - Proper error handling?
   - No code smells?

2. **Testing**
   - Adequate test coverage?
   - Edge cases considered?

3. **Performance**
   - No obvious performance issues?
   - Efficient algorithms?

4. **Security**
   - No security vulnerabilities?
   - Proper input validation?

5. **Documentation**
   - Code comments where needed?
   - README updated if necessary?

Provide a detailed review with specific suggestions for improvement.
"""
        return prompt
```

**2. Prompt de Planejamento**

```python
@app.get_prompt()
async def get_prompt(name: str, arguments: dict) -> str:
    if name == "feature_planning":
        feature_description = arguments["feature_description"]

        # Buscar contexto relevante
        similar_features = find_similar_features(feature_description)
        tech_stack = get_project_tech_stack()
        team_capacity = calculate_team_capacity()

        prompt = f"""# Feature Planning Assistant

## Requested Feature
{feature_description}

## Similar Features (for reference)
"""
        for feature in similar_features:
            prompt += f"\n- {feature['name']} (completed in {feature['duration_days']} days)"

        prompt += f"""

## Current Tech Stack
{json.dumps(tech_stack, indent=2)}

## Team Capacity
{json.dumps(team_capacity, indent=2)}

## Tasks

Please help plan this feature by:

1. Breaking it down into concrete tasks
2. Estimating effort for each task
3. Identifying potential risks or challenges
4. Suggesting an implementation order
5. Recommending which team members should work on each part

Provide a detailed implementation plan.
"""
        return prompt
```

### 6.5.4 Prompts com Parâmetros Opcionais

```python
@app.get_prompt()
async def get_prompt(name: str, arguments: dict) -> str:
    if name == "bug_triage":
        bug_id = arguments["bug_id"]
        include_history = arguments.get("include_history", False)
        include_similar = arguments.get("include_similar", True)

        bug = get_bug(bug_id)

        prompt = f"""# Bug Triage Assistant - Bug #{bug_id}

## Bug Details
- **Title:** {bug['title']}
- **Reporter:** {bug['reporter']}
- **Severity:** {bug['severity']}
- **Component:** {bug['component']}

## Description
{bug['description']}
"""

        if include_history:
            history = get_bug_history(bug_id)
            prompt += "\n## History\n"
            for entry in history:
                prompt += f"\n- {entry['date']}: {entry['action']} by {entry['user']}"

        if include_similar:
            similar = find_similar_bugs(bug_id)
            prompt += "\n\n## Similar Bugs\n"
            for similar_bug in similar[:5]:
                prompt += f"\n- #{similar_bug['id']}: {similar_bug['title']} (resolved as {similar_bug['resolution']})"

        prompt += """

## Triage Tasks

Please help triage this bug by:

1. Assessing the actual severity (confirm or suggest change)
2. Identifying the root cause if possible
3. Suggesting potential assignees based on expertise
4. Estimating effort to fix
5. Recommending priority

Provide a detailed triage report.
"""
        return prompt
```

---

## 6.6 Tools no MCP

### 6.6.1 Design de Tools Eficazes

**Princípios SOLID para Tools:**

1. **Single Responsibility**: Cada tool faz uma coisa bem feita

```python
# ✅ BOM - Responsabilidade única
Tool(name="create_task", ...)
Tool(name="update_task", ...)
Tool(name="delete_task", ...)

# ❌ RUIM - Faz muitas coisas
Tool(name="manage_task", ...)  # Cria, atualiza, deleta tudo em uma
```

2. **Idempotência**: Chamar múltiplas vezes com mesmos parâmetros = mesmo resultado

```python
@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "create_task":
        # Verificar se já existe antes de criar
        existing = find_task_by_title(arguments["title"])
        if existing:
            return [TextContent(
                type="text",
                text=f"Tarefa já existe: {existing['id']}"
            )]

        # Criar apenas se nêo existir
        return create_new_task(arguments)
```

3. **Validaçêo Rigorosa**

```python
def validate_email(email: str):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError(f"Email inválido: {email}")

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "invite_user":
        validate_email(arguments["email"])
        # ...
```

### 6.6.2 Tools Compostas

Às vezes você quer oferecer tools de alto nível que internamente usam outras tools:

```python
@app.call_tool()
async def call_tool(name: str, arguments: dict):

    if name == "complete_sprint":
        """Tool composta que fecha um sprint e prepara o próximo"""

        sprint_id = arguments["sprint_id"]

        # 1. Marcar todas as tarefas nêo concluídas como "rollover"
        incomplete_tasks = get_tasks(sprint=sprint_id, status="in_progress")
        for task in incomplete_tasks:
            update_task_status(task["id"], "rollover")

        # 2. Gerar relatório do sprint
        report = generate_sprint_report(sprint_id)

        # 3. Criar próximo sprint
        next_sprint = create_next_sprint(sprint_id)

        # 4. Mover tarefas rollover para próximo sprint
        for task in incomplete_tasks:
            assign_task_to_sprint(task["id"], next_sprint["id"])

        return [
            TextContent(
                type="text",
                text=f"""✓ Sprint {sprint_id} finalizado com sucesso!

📊 Relatório:
- Tarefas completadas: {report['completed']}
- Tarefas rollover: {len(incomplete_tasks)}
- Velocity: {report['velocity']}

🚀 Próximo Sprint: {next_sprint['id']}
- {len(incomplete_tasks)} tarefas já adicionadas
"""
            )
        ]
```

### 6.6.3 Tools com Confirmaçêo

Para operações destrutivas, implemente confirmaçêo:

```python
# Primeira chamada: solicitar confirmaçêo
Tool(
    name="delete_project",
    description="[DESTRUTIVO] Deleta um projeto permanentemente",
    inputSchema={
        "type": "object",
        "properties": {
            "project_id": {"type": "string"},
            "confirm": {
                "type": "boolean",
                "description": "Deve ser true para confirmar a deleçêo"
            }
        },
        "required": ["project_id", "confirm"]
    }
)

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "delete_project":
        project_id = arguments["project_id"]
        confirm = arguments.get("confirm", False)

        if not confirm:
            project = get_project(project_id)
            return [
                TextContent(
                    type="text",
                    text=f"""⚠️ ATENÇêO: Você está prestes a deletar o projeto:

📁 {project['name']}
- {project['task_count']} tarefas
- {project['member_count']} membros
- Criado em: {project['created_at']}

Esta açêo é IRREVERSÍVEL!

Para confirmar, chame novamente com confirm=true
"""
                )
            ]

        # Confirmado - executar deleçêo
        delete_project_permanently(project_id)

        return [
            TextContent(
                type="text",
                text=f"✓ Projeto {project_id} deletado permanentemente."
            )
        ]
```

### 6.6.4 Tools com Progresso

Para operações longas, retorne progresso:

```python
import asyncio

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "bulk_import_tasks":
        file_path = arguments["file_path"]

        tasks_to_import = parse_csv(file_path)
        total = len(tasks_to_import)

        imported = []
        failed = []

        for i, task_data in enumerate(tasks_to_import):
            try:
                task = create_task(task_data)
                imported.append(task)

                # Simular progresso (em produçêo, use websocket ou SSE)
                if (i + 1) % 10 == 0:
                    print(f"Progress: {i+1}/{total}", file=sys.stderr)

            except Exception as e:
                failed.append({"data": task_data, "error": str(e)})

        result_text = f"""✓ Importaçêo concluída!

📊 Resultados:
- Total: {total}
- Sucesso: {len(imported)}
- Falhas: {len(failed)}
"""

        if failed:
            result_text += "\n⚠️ Tarefas que falharam:\n"
            for item in failed[:5]:  # Mostrar só as primeiras 5
                result_text += f"\n- {item['data']['title']}: {item['error']}"

        return [TextContent(type="text", text=result_text)]
```

### 6.6.5 Tools com Side Effects Visíveis

```python
@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "deploy_to_production":
        environment = "production"
        version = arguments["version"]

        # 1. Executar deploy
        deploy_result = execute_deployment(version, environment)

        # 2. Criar registro de auditoria
        create_audit_log({
            "action": "deployment",
            "version": version,
            "environment": environment,
            "user": "mcp-server",
            "timestamp": datetime.now().isoformat()
        })

        # 3. Notificar equipe
        send_slack_notification(
            channel="#deployments",
            message=f"🚀 v{version} deployed to {environment}"
        )

        # 4. Agendar health check
        schedule_health_check(delay_seconds=60)

        return [
            TextContent(
                type="text",
                text=f"""✓ Deploy concluído!

📦 Versêo: {version}
🌍 Ambiente: {environment}
⏰ Timestamp: {deploy_result['timestamp']}

Side effects executados:
- Audit log criado
- Equipe notificada via Slack
- Health check agendado para daqui a 60s
"""
            )
        ]
```

---

## 6.7 Integraçêo com Agentes

### 6.7.1 Agno + MCP

```python
from agno import Agent
from mcp.client import Client
from mcp.client.stdio import stdio_client

async def create_agno_agent_with_mcp():
    """Cria um agente Agno conectado a um servidor MCP"""

    # Conectar ao servidor MCP
    async with stdio_client("python", ["server.py"]) as (read, write):
        async with Client(read, write) as mcp_client:

            await mcp_client.initialize()

            # Listar tools disponíveis do MCP
            mcp_tools = await mcp_client.list_tools()

            # Criar ferramentas Agno que chamam tools MCP
            async def create_task_via_mcp(title: str, priority: str = "medium") -> str:
                """Cria uma tarefa usando o servidor MCP"""
                result = await mcp_client.call_tool(
                    "create_task",
                    arguments={"title": title, "priority": priority}
                )
                return result.content[0].text

            async def list_tasks_via_mcp(status: str = None) -> str:
                """Lista tarefas usando o servidor MCP"""
                args = {"status": status} if status else {}
                result = await mcp_client.call_tool("list_tasks", arguments=args)
                return result.content[0].text

            # Criar agente Agno com as ferramentas MCP
            assistant = Agent(
                name="Project Manager Assistant",
                role="Assistente de Gestêo de Projetos",
                model="claude-3-7-sonnet-20250219",
                tools=[create_task_via_mcp, list_tasks_via_mcp],
                instructions="""
                Você é um assistente especializado em gestêo de projetos.
                Use as ferramentas disponíveis para ajudar o usuário a gerenciar tarefas.
                Sempre confirme as ações antes de executá-las.
                """,
                show_tool_calls=True
            )

            # Usar o agente
            response = await assistant.async_run(
                "Crie uma tarefa de alta prioridade para implementar autenticaçêo OAuth"
            )

            print(response)

# Executar
import asyncio
asyncio.run(create_agno_agent_with_mcp())
```

### 6.7.2 LangChain + MCP

```python
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_anthropic import ChatAnthropic
from mcp.client import Client
from mcp.client.stdio import stdio_client

async def create_langchain_agent_with_mcp():
    """Cria um agente LangChain conectado a MCP"""

    # Conectar ao servidor MCP
    async with stdio_client("python", ["server.py"]) as (read, write):
        async with Client(read, write) as mcp_client:

            await mcp_client.initialize()

            # Converter tools MCP em ferramentas LangChain
            mcp_tools_list = await mcp_client.list_tools()

            langchain_tools = []

            for mcp_tool in mcp_tools_list:
                # Criar uma funçêo wrapper para cada tool MCP
                async def tool_wrapper(tool_name=mcp_tool.name):
                    async def func(**kwargs):
                        result = await mcp_client.call_tool(
                            tool_name,
                            arguments=kwargs
                        )
                        return result.content[0].text
                    return func

                wrapper_func = await tool_wrapper()

                lc_tool = Tool(
                    name=mcp_tool.name,
                    description=mcp_tool.description,
                    func=wrapper_func
                )

                langchain_tools.append(lc_tool)

            # Criar agente LangChain
            llm = ChatAnthropic(model="claude-3-7-sonnet-20250219")

            agent = initialize_agent(
                tools=langchain_tools,
                llm=llm,
                agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True
            )

            # Usar o agente
            result = agent.run(
                "Liste todas as tarefas em progresso e crie uma nova tarefa "
                "de alta prioridade para revisar o código do módulo de autenticaçêo"
            )

            print(result)

asyncio.run(create_langchain_agent_with_mcp())
```

### 6.7.3 CrewAI + MCP

```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import BaseTool
from mcp.client import Client
from mcp.client.stdio import stdio_client

class MCPTool(BaseTool):
    """Wrapper que converte tools MCP em CrewAI tools"""

    name: str
    description: str
    mcp_client: Client
    tool_name: str

    async def _run(self, **kwargs):
        """Executa a tool MCP"""
        result = await self.mcp_client.call_tool(
            self.tool_name,
            arguments=kwargs
        )
        return result.content[0].text

async def create_crewai_with_mcp():
    """Cria um crew CrewAI conectado a MCP"""

    async with stdio_client("python", ["server.py"]) as (read, write):
        async with Client(read, write) as mcp_client:

            await mcp_client.initialize()

            # Criar ferramentas CrewAI a partir das tools MCP
            mcp_tools_list = await mcp_client.list_tools()

            crewai_tools = []
            for mcp_tool in mcp_tools_list:
                tool = MCPTool(
                    name=mcp_tool.name,
                    description=mcp_tool.description,
                    mcp_client=mcp_client,
                    tool_name=mcp_tool.name
                )
                crewai_tools.append(tool)

            # Criar agentes especializados
            project_manager = Agent(
                role="Gerente de Projetos",
                goal="Organizar e priorizar tarefas do projeto",
                backstory="""Você é um gerente de projetos experiente com 10 anos
                de experiência em metodologias ágeis.""",
                tools=crewai_tools,
                verbose=True
            )

            developer = Agent(
                role="Desenvolvedor Sênior",
                goal="Estimar esforço e complexidade técnica das tarefas",
                backstory="""Você é um desenvolvedor sênior com ampla experiência
                em arquitetura de software.""",
                tools=crewai_tools,
                verbose=True
            )

            # Criar tarefas
            task1 = Task(
                description="""Analise todas as tarefas pendentes e crie um plano
                de sprint priorizando as tarefas de alta prioridade""",
                agent=project_manager,
                expected_output="Plano de sprint detalhado com tarefas priorizadas"
            )

            task2 = Task(
                description="""Para cada tarefa de alta prioridade, forneça uma
                estimativa de esforço em pontos de história""",
                agent=developer,
                expected_output="Lista de tarefas com estimativas"
            )

            # Criar o crew
            crew = Crew(
                agents=[project_manager, developer],
                tasks=[task1, task2],
                process=Process.sequential,
                verbose=True
            )

            # Executar
            result = crew.kickoff()

            print("\n" + "="*60)
            print("RESULTADO FINAL")
            print("="*60)
            print(result)

asyncio.run(create_crewai_with_mcp())
```

### 6.7.4 Padrêo: MCP como Camada de Abstraçêo

```
┌───────────────────────────────────────────────────────────┐
│                     APPLICATION LAYER                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │   Agno   │  │LangChain │  │ CrewAI   │  │  Custom  │ │
│  │  Agent   │  │  Agent   │  │   Crew   │  │   App    │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘ │
├───────┼─────────────┼──────────────┼──────────────┼───────┤
│       │             │              │              │       │
│       └─────────────┴──────────────┴──────────────┘       │
│                          │                                │
│                  ┌───────▼────────┐                       │
│                  │   MCP CLIENT   │                       │
│                  └───────┬────────┘                       │
├──────────────────────────┼────────────────────────────────┤
│                  MCP PROTOCOL (JSON-RPC)                  │
├──────────────────────────┼────────────────────────────────┤
│                  ┌───────▼────────┐                       │
│                  │   MCP SERVER   │                       │
│                  └───────┬────────┘                       │
│                          │                                │
│       ┌──────────────────┼──────────────────┐            │
│       │                  │                  │            │
│  ┌────▼────┐      ┌──────▼──────┐    ┌─────▼──────┐     │
│  │Database │      │   APIs      │    │File System │     │
│  └─────────┘      └─────────────┘    └────────────┘     │
│                                                           │
│                     DATA/TOOLS LAYER                      │
└───────────────────────────────────────────────────────────┘
```

**Vantagens deste padrêo:**

✅ **Desacoplamento**: Agentes nêo dependem de implementações específicas
✅ **Reutilizaçêo**: Mesmo servidor MCP serve múltiplos agentes
✅ **Manutenibilidade**: Mudanças em fontes de dados ficam isoladas
✅ **Testabilidade**: Fácil mockar o servidor MCP para testes

---

## 6.8 Segurança e Autenticaçêo

### 6.8.1 Princípios de Segurança

**1. Princípio do Menor Privilégio**

```python
# Definir níveis de permissêo
PERMISSION_LEVELS = {
    "read_only": ["list_tasks", "read_resource"],
    "developer": ["list_tasks", "read_resource", "create_task", "update_task"],
    "admin": ["*"]  # Todas as tools
}

def check_permission(user_role: str, tool_name: str) -> bool:
    """Verifica se o usuário tem permissêo para usar a tool"""
    allowed_tools = PERMISSION_LEVELS.get(user_role, [])

    if "*" in allowed_tools:
        return True

    return tool_name in allowed_tools

@app.call_tool()
async def call_tool(name: str, arguments: dict, context: dict):
    # Extrair papel do usuário do contexto
    user_role = context.get("user_role", "read_only")

    if not check_permission(user_role, name):
        raise PermissionError(
            f"Usuário com papel '{user_role}' nêo tem permissêo para usar '{name}'"
        )

    # Executar tool...
```

**2. Validaçêo de Entrada**

```python
import re

def sanitize_input(value: str) -> str:
    """Remove caracteres potencialmente perigosos"""
    # Remove SQL injection attempts
    dangerous_patterns = [
        r"(--)",
        r"(;)",
        r"(\bDROP\b)",
        r"(\bDELETE\b)",
        r"(\bINSERT\b)",
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, value, re.IGNORECASE):
            raise ValueError(f"Entrada contém padrêo suspeito: {pattern}")

    return value.strip()

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "create_task":
        # Sanitizar todas as entradas
        title = sanitize_input(arguments["title"])
        description = sanitize_input(arguments.get("description", ""))

        # Proceder com segurança...
```

**3. Rate Limiting por Usuário**

```python
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self):
        self.calls = defaultdict(list)

    def check_limit(self, user_id: str, max_calls: int = 100, window: int = 3600):
        """Verifica se usuário excedeu o rate limit (padrêo: 100 calls/hora)"""
        now = time.time()

        # Remover chamadas antigas
        self.calls[user_id] = [
            timestamp for timestamp in self.calls[user_id]
            if now - timestamp < window
        ]

        if len(self.calls[user_id]) >= max_calls:
            return False

        self.calls[user_id].append(now)
        return True

rate_limiter = RateLimiter()

@app.call_tool()
async def call_tool(name: str, arguments: dict, context: dict):
    user_id = context.get("user_id", "anonymous")

    if not rate_limiter.check_limit(user_id):
        raise Exception(
            "Rate limit excedido. Tente novamente em alguns minutos."
        )

    # Executar tool...
```

### 6.8.2 Autenticaçêo com Tokens

**server.py com autenticaçêo:**

```python
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-here"  # Em produçêo, use variável de ambiente

def create_token(user_id: str, role: str) -> str:
    """Cria um JWT token"""
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token: str) -> dict:
    """Verifica e decodifica um JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token expirado")
    except jwt.InvalidTokenError:
        raise Exception("Token inválido")

# Adicionar middleware de autenticaçêo
@app.before_request()
async def authenticate_request(request):
    """Verifica token antes de processar requisiçêo"""
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise Exception("Token de autenticaçêo nêo fornecido")

    token = auth_header.replace("Bearer ", "")

    try:
        payload = verify_token(token)
        request.context["user_id"] = payload["user_id"]
        request.context["user_role"] = payload["role"]
    except Exception as e:
        raise Exception(f"Autenticaçêo falhou: {e}")
```

**Cliente com autenticaçêo:**

```python
# Cliente envia token em cada requisiçêo
class AuthenticatedMCPClient:
    def __init__(self, server_url, token):
        self.server_url = server_url
        self.token = token

    def call_tool(self, tool_name, arguments):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            f"{self.server_url}/mcp",
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "tools/call",
                "params": {
                    "name": tool_name,
                    "arguments": arguments
                }
            },
            headers=headers
        )

        return response.json()

# Uso
token = create_token("user123", "developer")
client = AuthenticatedMCPClient("http://localhost:8000", token)

result = client.call_tool("create_task", {
    "title": "Nova tarefa",
    "priority": "high"
})
```

### 6.8.3 Auditoria e Logging

```python
import logging
from datetime import datetime

# Configurar logging estruturado
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AuditLogger:
    """Logger de auditoria para ações críticas"""

    def __init__(self, db_connection):
        self.db = db_connection

    def log_action(self, user_id: str, action: str, resource: str, details: dict):
        """Registra uma açêo no log de auditoria"""
        audit_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "action": action,
            "resource": resource,
            "details": details
        }

        # Salvar no banco de dados
        self.db.audit_logs.insert_one(audit_entry)

        # Também logar no sistema
        logger.info(f"AUDIT: {user_id} {action} {resource}")

audit_logger = AuditLogger(db_connection)

@app.call_tool()
async def call_tool(name: str, arguments: dict, context: dict):
    user_id = context.get("user_id", "anonymous")

    if name == "delete_task":
        # Açêo crítica - auditar
        task_id = arguments["task_id"]
        task = get_task(task_id)

        audit_logger.log_action(
            user_id=user_id,
            action="delete_task",
            resource=f"task:{task_id}",
            details={
                "task_title": task["title"],
                "task_status": task["status"]
            }
        )

        # Executar deleçêo
        delete_task(task_id)

        return [TextContent(type="text", text=f"Tarefa {task_id} deletada")]
```

### 6.8.4 Proteçêo contra Injeções

**SQL Injection Protection:**

```python
# ❌ VULNERÁVEL
def get_tasks_unsafe(status: str):
    query = f"SELECT * FROM tasks WHERE status = '{status}'"
    return db.execute(query)

# ✅ SEGURO - Use queries parametrizadas
def get_tasks_safe(status: str):
    query = "SELECT * FROM tasks WHERE status = ?"
    return db.execute(query, (status,))
```

**Command Injection Protection:**

```python
import shlex

# ❌ VULNERÁVEL
def run_command_unsafe(filename: str):
    os.system(f"cat {filename}")

# ✅ SEGURO
def run_command_safe(filename: str):
    # Validar que o filename nêo contém caracteres perigosos
    if not filename.replace("_", "").replace("-", "").replace(".", "").isalnum():
        raise ValueError("Filename inválido")

    # Usar subprocess com lista de argumentos (nêo string)
    import subprocess
    subprocess.run(["cat", filename], check=True)
```

**Path Traversal Protection:**

```python
import os
from pathlib import Path

ALLOWED_BASE_PATH = "/var/mcp/data"

def read_file_safe(filepath: str) -> str:
    """Lê arquivo com proteçêo contra path traversal"""
    # Resolver path absoluto
    requested_path = Path(filepath).resolve()
    base_path = Path(ALLOWED_BASE_PATH).resolve()

    # Verificar que o path está dentro do diretório permitido
    try:
        requested_path.relative_to(base_path)
    except ValueError:
        raise PermissionError(
            "Acesso negado: path fora do diretório permitido"
        )

    # Verificar que o arquivo existe
    if not requested_path.exists():
        raise FileNotFoundError(f"Arquivo nêo encontrado: {filepath}")

    # Ler arquivo com segurança
    with open(requested_path, 'r') as f:
        return f.read()
```

---

## 6.9 Projeto Prático: Sistema de Gestêo de Projetos com MCP

### 6.9.1 Visêo Geral do Projeto

Vamos construir um **sistema completo de gestêo de projetos** usando MCP, integrando:

- Servidor MCP com tools, resources e prompts
- Cliente Agno que usa o servidor
- Banco de dados SQLite para persistência
- Interface de linha de comando (CLI)
- Autenticaçêo e autorizaçêo
- Logging e auditoria

**Arquitetura:**

```
┌──────────────────────────────────────────────────────────┐
│                    CLI Application                       │
│              (project_manager_cli.py)                    │
└────────────────────┬─────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────┐
│                  Agno Agent                              │
│              (agent_config.py)                           │
└────────────────────┬─────────────────────────────────────┘
                     │
                     ▼ (MCP Protocol)
┌──────────────────────────────────────────────────────────┐
│                  MCP Server                              │
│              (mcp_server.py)                             │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐        │
│  │ Tools  │  │Resource│  │ Prompts│  │  Auth  │        │
│  └───┬────┘  └───┬────┘  └───┬────┘  └───┬────┘        │
└──────┼───────────┼───────────┼───────────┼──────────────┘
       │           │           │           │
       └───────────┴───────────┴───────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────┐
│              SQLite Database                             │
│         (projects.db)                                    │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐        │
│  │ users  │  │projects│  │ tasks  │  │ audit  │        │
│  └────────┘  └────────┘  └────────┘  └────────┘        │
└──────────────────────────────────────────────────────────┘
```

### 6.9.2 Estrutura de Arquivos

```
project_manager_mcp/
├── mcp_server.py           # Servidor MCP principal
├── database.py             # Gerenciamento do banco de dados
├── models.py               # Modelos de dados (User, Project, Task)
├── auth.py                 # Autenticaçêo e autorizaçêo
├── tools_impl.py           # Implementaçêo das tools
├── resources_impl.py       # Implementaçêo dos resources
├── prompts_impl.py         # Implementaçêo dos prompts
├── agent_config.py         # Configuraçêo do agente Agno
├── project_manager_cli.py  # Interface CLI
├── config.py               # Configurações gerais
├── requirements.txt
└── README.md
```

### 6.9.3 Implementaçêo Completa

**requirements.txt:**

```
mcp>=0.9.0
agno>=0.1.0
anthropic
sqlite3
pydantic
python-dotenv
rich
typer
```

**config.py:**

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE_PATH = os.getenv("DATABASE_PATH", "./projects.db")

# Auth
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24

# MCP Server
MCP_SERVER_NAME = "project-manager"
MCP_SERVER_VERSION = "1.0.0"

# Anthropic
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
```

**models.py:**

```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    DEVELOPER = "developer"
    READ_ONLY = "read_only"

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class User(BaseModel):
    id: str
    username: str
    email: str
    role: UserRole
    created_at: datetime

class Project(BaseModel):
    id: str
    name: str
    description: str
    owner_id: str
    created_at: datetime
    updated_at: datetime

class Task(BaseModel):
    id: str
    project_id: str
    title: str
    description: Optional[str] = None
    status: TaskStatus
    priority: TaskPriority
    assignee_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None

class AuditLog(BaseModel):
    id: str
    user_id: str
    action: str
    resource_type: str
    resource_id: str
    details: dict
    timestamp: datetime
```

**database.py:**

```python
import sqlite3
from typing import List, Optional
import uuid
from datetime import datetime
from models import User, Project, Task, AuditLog, UserRole, TaskStatus, TaskPriority
import config

class Database:
    def __init__(self, db_path: str = config.DATABASE_PATH):
        self.db_path = db_path
        self.init_database()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_database(self):
        """Inicializa o schema do banco de dados"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Tabela de usuários
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """)

        # Tabela de projetos
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            owner_id TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY (owner_id) REFERENCES users(id)
        )
        """)

        # Tabela de tarefas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            project_id TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            priority TEXT NOT NULL,
            assignee_id TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            completed_at TEXT,
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (assignee_id) REFERENCES users(id)
        )
        """)

        # Tabela de auditoria
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            action TEXT NOT NULL,
            resource_type TEXT NOT NULL,
            resource_id TEXT NOT NULL,
            details TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)

        conn.commit()
        conn.close()

        # Criar usuários padrêo se nêo existirem
        self._create_default_users()

    def _create_default_users(self):
        """Cria usuários padrêo para teste"""
        default_users = [
            User(
                id=str(uuid.uuid4()),
                username="admin",
                email="admin@projectmanager.com",
                role=UserRole.ADMIN,
                created_at=datetime.utcnow()
            ),
            User(
                id=str(uuid.uuid4()),
                username="alice",
                email="alice@projectmanager.com",
                role=UserRole.DEVELOPER,
                created_at=datetime.utcnow()
            ),
            User(
                id=str(uuid.uuid4()),
                username="bob",
                email="bob@projectmanager.com",
                role=UserRole.DEVELOPER,
                created_at=datetime.utcnow()
            )
        ]

        conn = self.get_connection()
        cursor = conn.cursor()

        for user in default_users:
            # Verificar se já existe
            cursor.execute("SELECT id FROM users WHERE username = ?", (user.username,))
            if cursor.fetchone() is None:
                cursor.execute(
                    """INSERT INTO users (id, username, email, role, created_at)
                       VALUES (?, ?, ?, ?, ?)""",
                    (user.id, user.username, user.email, user.role.value,
                     user.created_at.isoformat())
                )

        conn.commit()
        conn.close()

    # ========== USER OPERATIONS ==========

    def get_user(self, user_id: str) -> Optional[User]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return User(
                id=row["id"],
                username=row["username"],
                email=row["email"],
                role=UserRole(row["role"]),
                created_at=datetime.fromisoformat(row["created_at"])
            )
        return None

    def get_user_by_username(self, username: str) -> Optional[User]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return User(
                id=row["id"],
                username=row["username"],
                email=row["email"],
                role=UserRole(row["role"]),
                created_at=datetime.fromisoformat(row["created_at"])
            )
        return None

    # ========== PROJECT OPERATIONS ==========

    def create_project(self, project: Project) -> Project:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO projects (id, name, description, owner_id, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (project.id, project.name, project.description, project.owner_id,
             project.created_at.isoformat(), project.updated_at.isoformat())
        )
        conn.commit()
        conn.close()
        return project

    def get_projects(self, owner_id: Optional[str] = None) -> List[Project]:
        conn = self.get_connection()
        cursor = conn.cursor()

        if owner_id:
            cursor.execute("SELECT * FROM projects WHERE owner_id = ?", (owner_id,))
        else:
            cursor.execute("SELECT * FROM projects")

        rows = cursor.fetchall()
        conn.close()

        projects = []
        for row in rows:
            projects.append(Project(
                id=row["id"],
                name=row["name"],
                description=row["description"],
                owner_id=row["owner_id"],
                created_at=datetime.fromisoformat(row["created_at"]),
                updated_at=datetime.fromisoformat(row["updated_at"])
            ))

        return projects

    # ========== TASK OPERATIONS ==========

    def create_task(self, task: Task) -> Task:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO tasks
               (id, project_id, title, description, status, priority, assignee_id,
                created_at, updated_at, completed_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (task.id, task.project_id, task.title, task.description,
             task.status.value, task.priority.value, task.assignee_id,
             task.created_at.isoformat(), task.updated_at.isoformat(),
             task.completed_at.isoformat() if task.completed_at else None)
        )
        conn.commit()
        conn.close()
        return task

    def get_tasks(
        self,
        project_id: Optional[str] = None,
        status: Optional[TaskStatus] = None,
        assignee_id: Optional[str] = None
    ) -> List[Task]:
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM tasks WHERE 1=1"
        params = []

        if project_id:
            query += " AND project_id = ?"
            params.append(project_id)

        if status:
            query += " AND status = ?"
            params.append(status.value)

        if assignee_id:
            query += " AND assignee_id = ?"
            params.append(assignee_id)

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()

        tasks = []
        for row in rows:
            tasks.append(Task(
                id=row["id"],
                project_id=row["project_id"],
                title=row["title"],
                description=row["description"],
                status=TaskStatus(row["status"]),
                priority=TaskPriority(row["priority"]),
                assignee_id=row["assignee_id"],
                created_at=datetime.fromisoformat(row["created_at"]),
                updated_at=datetime.fromisoformat(row["updated_at"]),
                completed_at=datetime.fromisoformat(row["completed_at"]) if row["completed_at"] else None
            ))

        return tasks

    def update_task(self, task: Task) -> Task:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE tasks
               SET title = ?, description = ?, status = ?, priority = ?,
                   assignee_id = ?, updated_at = ?, completed_at = ?
               WHERE id = ?""",
            (task.title, task.description, task.status.value, task.priority.value,
             task.assignee_id, task.updated_at.isoformat(),
             task.completed_at.isoformat() if task.completed_at else None,
             task.id)
        )
        conn.commit()
        conn.close()
        return task

    # ========== AUDIT LOG OPERATIONS ==========

    def create_audit_log(self, audit_log: AuditLog):
        import json
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO audit_logs
               (id, user_id, action, resource_type, resource_id, details, timestamp)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (audit_log.id, audit_log.user_id, audit_log.action,
             audit_log.resource_type, audit_log.resource_id,
             json.dumps(audit_log.details), audit_log.timestamp.isoformat())
        )
        conn.commit()
        conn.close()

# Instância global do banco de dados
db = Database()
```

**auth.py:**

```python
import jwt
from datetime import datetime, timedelta
from typing import Optional
import config
from models import User

def create_access_token(user: User) -> str:
    """Cria um JWT token para o usuário"""
    payload = {
        "user_id": user.id,
        "username": user.username,
        "role": user.role.value,
        "exp": datetime.utcnow() + timedelta(hours=config.JWT_EXPIRATION_HOURS)
    }
    return jwt.encode(payload, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)

def verify_access_token(token: str) -> dict:
    """Verifica e decodifica um JWT token"""
    try:
        payload = jwt.decode(
            token,
            config.JWT_SECRET_KEY,
            algorithms=[config.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expirado")
    except jwt.InvalidTokenError:
        raise ValueError("Token inválido")

def check_permission(user_role: str, required_permission: str) -> bool:
    """Verifica se o usuário tem a permissêo necessária"""
    permissions = {
        "admin": ["*"],
        "developer": [
            "create_project", "create_task", "update_task",
            "list_projects", "list_tasks", "read_resource"
        ],
        "read_only": ["list_projects", "list_tasks", "read_resource"]
    }

    user_permissions = permissions.get(user_role, [])

    if "*" in user_permissions:
        return True

    return required_permission in user_permissions
```

**tools_impl.py:**

```python
from typing import List
import uuid
from datetime import datetime
from models import Project, Task, TaskStatus, TaskPriority, AuditLog
from database import db
from mcp.types import TextContent

def create_project_tool(name: str, description: str, user_id: str) -> List[TextContent]:
    """Cria um novo projeto"""
    project = Project(
        id=str(uuid.uuid4()),
        name=name,
        description=description,
        owner_id=user_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.create_project(project)

    # Audit log
    db.create_audit_log(AuditLog(
        id=str(uuid.uuid4()),
        user_id=user_id,
        action="create_project",
        resource_type="project",
        resource_id=project.id,
        details={"name": name},
        timestamp=datetime.utcnow()
    ))

    return [TextContent(
        type="text",
        text=f"""✓ Projeto criado com sucesso!

📁 **{project.name}**
ID: {project.id}
Descriçêo: {project.description}
"""
    )]

def create_task_tool(
    project_id: str,
    title: str,
    priority: str,
    description: str = "",
    assignee_username: str = None,
    user_id: str = None
) -> List[TextContent]:
    """Cria uma nova tarefa"""

    # Resolver assignee
    assignee_id = None
    if assignee_username:
        assignee = db.get_user_by_username(assignee_username)
        if assignee:
            assignee_id = assignee.id

    task = Task(
        id=str(uuid.uuid4()),
        project_id=project_id,
        title=title,
        description=description,
        status=TaskStatus.PENDING,
        priority=TaskPriority(priority),
        assignee_id=assignee_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.create_task(task)

    # Audit log
    db.create_audit_log(AuditLog(
        id=str(uuid.uuid4()),
        user_id=user_id,
        action="create_task",
        resource_type="task",
        resource_id=task.id,
        details={"title": title, "priority": priority},
        timestamp=datetime.utcnow()
    ))

    assignee_text = f"Responsável: {assignee_username}" if assignee_username else "Nêo atribuída"

    return [TextContent(
        type="text",
        text=f"""✓ Tarefa criada com sucesso!

📝 **{task.title}**
ID: {task.id}
Prioridade: {task.priority.value}
Status: {task.status.value}
{assignee_text}
"""
    )]

def list_tasks_tool(
    project_id: str = None,
    status: str = None,
    assignee_username: str = None
) -> List[TextContent]:
    """Lista tarefas com filtros opcionais"""

    # Resolver assignee
    assignee_id = None
    if assignee_username:
        assignee = db.get_user_by_username(assignee_username)
        if assignee:
            assignee_id = assignee.id

    # Buscar tarefas
    tasks = db.get_tasks(
        project_id=project_id,
        status=TaskStatus(status) if status else None,
        assignee_id=assignee_id
    )

    if not tasks:
        return [TextContent(type="text", text="Nenhuma tarefa encontrada.")]

    # Formatar lista
    task_list = []
    for task in tasks:
        assignee = ""
        if task.assignee_id:
            user = db.get_user(task.assignee_id)
            assignee = f" | {user.username}" if user else ""

        task_list.append(
            f"[{task.id[:8]}] **{task.title}**\n"
            f"  {task.priority.value.upper()} | {task.status.value}{assignee}"
        )

    return [TextContent(
        type="text",
        text=f"📋 **{len(tasks)} tarefa(s) encontrada(s)**\n\n" + "\n\n".join(task_list)
    )]

def update_task_tool(
    task_id: str,
    status: str = None,
    priority: str = None,
    assignee_username: str = None,
    user_id: str = None
) -> List[TextContent]:
    """Atualiza uma tarefa existente"""

    # Buscar tarefa
    tasks = db.get_tasks()
    task = next((t for t in tasks if t.id == task_id), None)

    if not task:
        return [TextContent(
            type="text",
            text=f"❌ Tarefa {task_id} nêo encontrada."
        )]

    # Atualizar campos
    if status:
        task.status = TaskStatus(status)
        if status == "completed":
            task.completed_at = datetime.utcnow()

    if priority:
        task.priority = TaskPriority(priority)

    if assignee_username:
        assignee = db.get_user_by_username(assignee_username)
        if assignee:
            task.assignee_id = assignee.id

    task.updated_at = datetime.utcnow()

    db.update_task(task)

    # Audit log
    db.create_audit_log(AuditLog(
        id=str(uuid.uuid4()),
        user_id=user_id,
        action="update_task",
        resource_type="task",
        resource_id=task.id,
        details={"status": status, "priority": priority},
        timestamp=datetime.utcnow()
    ))

    return [TextContent(
        type="text",
        text=f"""✓ Tarefa atualizada com sucesso!

📝 **{task.title}**
Status: {task.status.value}
Prioridade: {task.priority.value}
"""
    )]
```

**(Continuaçêo do código no próximo bloco...)**

**mcp_server.py** (servidor MCP principal):

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, Resource, Prompt, TextContent
import asyncio
import json
from database import db
from auth import verify_access_token, check_permission
from tools_impl import (
    create_project_tool,
    create_task_tool,
    list_tasks_tool,
    update_task_tool
)
import config

# Criar instância do servidor
app = Server(config.MCP_SERVER_NAME)

# ============================================================================
# MIDDLEWARE DE AUTENTICAÇêO
# ============================================================================

# Armazenar contexto da requisiçêo atual
current_context = {}

# ============================================================================
# TOOLS
# ============================================================================

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="create_project",
            description="Cria um novo projeto",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Nome do projeto"},
                    "description": {"type": "string", "description": "Descriçêo do projeto"}
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="create_task",
            description="Cria uma nova tarefa em um projeto",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_id": {"type": "string"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "priority": {
                        "type": "string",
                        "enum": ["low", "medium", "high", "urgent"]
                    },
                    "assignee_username": {"type": "string"}
                },
                "required": ["project_id", "title", "priority"]
            }
        ),
        Tool(
            name="list_tasks",
            description="Lista tarefas com filtros opcionais",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_id": {"type": "string"},
                    "status": {
                        "type": "string",
                        "enum": ["pending", "in_progress", "completed", "blocked"]
                    },
                    "assignee_username": {"type": "string"}
                }
            }
        ),
        Tool(
            name="update_task",
            description="Atualiza uma tarefa existente",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {"type": "string"},
                    "status": {
                        "type": "string",
                        "enum": ["pending", "in_progress", "completed", "blocked"]
                    },
                    "priority": {
                        "type": "string",
                        "enum": ["low", "medium", "high", "urgent"]
                    },
                    "assignee_username": {"type": "string"}
                },
                "required": ["task_id"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    # Obter user_id do contexto (em produçêo, viria do token JWT)
    user_id = current_context.get("user_id", "admin")  # Default para teste

    # Verificar permissêo
    user_role = current_context.get("user_role", "admin")
    if not check_permission(user_role, name):
        return [TextContent(
            type="text",
            text=f"❌ Você nêo tem permissêo para executar '{name}'"
        )]

    # Executar tool
    try:
        if name == "create_project":
            return create_project_tool(
                name=arguments["name"],
                description=arguments.get("description", ""),
                user_id=user_id
            )

        elif name == "create_task":
            return create_task_tool(
                project_id=arguments["project_id"],
                title=arguments["title"],
                priority=arguments["priority"],
                description=arguments.get("description", ""),
                assignee_username=arguments.get("assignee_username"),
                user_id=user_id
            )

        elif name == "list_tasks":
            return list_tasks_tool(
                project_id=arguments.get("project_id"),
                status=arguments.get("status"),
                assignee_username=arguments.get("assignee_username")
            )

        elif name == "update_task":
            return update_task_tool(
                task_id=arguments["task_id"],
                status=arguments.get("status"),
                priority=arguments.get("priority"),
                assignee_username=arguments.get("assignee_username"),
                user_id=user_id
            )

        else:
            return [TextContent(type="text", text=f"❌ Tool desconhecida: {name}")]

    except Exception as e:
        return [TextContent(type="text", text=f"❌ Erro: {str(e)}")]

# ============================================================================
# RESOURCES
# ============================================================================

@app.list_resources()
async def list_resources() -> list[Resource]:
    return [
        Resource(
            uri="project://dashboard",
            name="Dashboard",
            mimeType="application/json",
            description="Visêo geral de todos os projetos e tarefas"
        ),
        Resource(
            uri="project://projects",
            name="All Projects",
            mimeType="application/json",
            description="Lista de todos os projetos"
        )
    ]

@app.read_resource()
async def read_resource(uri: str) -> str:
    if uri == "project://dashboard":
        projects = db.get_projects()
        tasks = db.get_tasks()

        dashboard = {
            "projects": {
                "total": len(projects),
                "list": [{"id": p.id, "name": p.name} for p in projects]
            },
            "tasks": {
                "total": len(tasks),
                "pending": len([t for t in tasks if t.status.value == "pending"]),
                "in_progress": len([t for t in tasks if t.status.value == "in_progress"]),
                "completed": len([t for t in tasks if t.status.value == "completed"])
            }
        }

        return json.dumps(dashboard, indent=2)

    elif uri == "project://projects":
        projects = db.get_projects()
        return json.dumps([{
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "created_at": p.created_at.isoformat()
        } for p in projects], indent=2)

    else:
        raise ValueError(f"Resource nêo encontrado: {uri}")

# ============================================================================
# PROMPTS
# ============================================================================

@app.list_prompts()
async def list_prompts() -> list[Prompt]:
    return [
        Prompt(
            name="project_summary",
            description="Gera um resumo do projeto",
            arguments=[
                {"name": "project_id", "required": True}
            ]
        )
    ]

@app.get_prompt()
async def get_prompt(name: str, arguments: dict) -> str:
    if name == "project_summary":
        project_id = arguments["project_id"]

        projects = db.get_projects()
        project = next((p for p in projects if p.id == project_id), None)

        if not project:
            return f"Projeto {project_id} nêo encontrado."

        tasks = db.get_tasks(project_id=project_id)

        prompt = f"""# Resumo do Projeto: {project.name}

## Informações Gerais
- **ID**: {project.id}
- **Descriçêo**: {project.description}
- **Criado em**: {project.created_at.strftime("%d/%m/%Y")}

## Estatísticas de Tarefas
- **Total**: {len(tasks)}
- **Pendentes**: {len([t for t in tasks if t.status == TaskStatus.PENDING])}
- **Em Progresso**: {len([t for t in tasks if t.status == TaskStatus.IN_PROGRESS])}
- **Completadas**: {len([t for t in tasks if t.status == TaskStatus.COMPLETED])}

## Tarefas de Alta Prioridade
"""

        high_priority = [t for t in tasks if t.priority == TaskPriority.HIGH or t.priority == TaskPriority.URGENT]
        for task in high_priority[:5]:
            prompt += f"\n- [{task.priority.value.upper()}] {task.title} ({task.status.value})"

        prompt += "\n\nPor favor, analise este projeto e forneça insights sobre o progresso e possíveis melhorias."

        return prompt

    else:
        raise ValueError(f"Prompt nêo encontrado: {name}")

# ============================================================================
# MAIN
# ============================================================================

async def main():
    """Inicia o servidor MCP via stdio"""
    # Definir contexto padrêo (em produçêo, seria extraído do token)
    current_context["user_id"] = "admin"
    current_context["user_role"] = "admin"

    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### 6.9.4 Como Usar o Sistema

**1. Instalar dependências:**

```bash
cd project_manager_mcp
pip install -r requirements.txt
```

**2. Criar arquivo .env:**

```bash
# .env
DATABASE_PATH=./projects.db
JWT_SECRET_KEY=your-super-secret-key-change-in-production
ANTHROPIC_API_KEY=sk-ant-...
```

**3. Testar o servidor MCP:**

```bash
python mcp_server.py
```

**4. Em outro terminal, testar com cliente:**

```python
# test_mcp.py
from mcp.client import Client
from mcp.client.stdio import stdio_client
import asyncio

async def test():
    async with stdio_client("python", ["mcp_server.py"]) as (read, write):
        async with Client(read, write) as client:
            await client.initialize()

            # Criar projeto
            result = await client.call_tool("create_project", {
                "name": "E-commerce Platform",
                "description": "Plataforma de e-commerce completa"
            })
            print(result.content[0].text)

            # Listar projetos
            dashboard = await client.read_resource("project://dashboard")
            print(dashboard)

asyncio.run(test())
```

---

## 6.10 Resumo e Próximos Passos

### 6.10.1 O Que Aprendemos

Neste módulo, você dominou:

✅ **Fundamentos do MCP**: Arquitetura cliente-servidor, JSON-RPC, transporte
✅ **Servidores MCP**: Como criar servers com tools, resources e prompts
✅ **Clientes MCP**: Como conectar aplicações aos servidores
✅ **Integraçêo com Agentes**: Agno, LangChain, CrewAI + MCP
✅ **Segurança**: Autenticaçêo, autorizaçêo, validaçêo, auditoria
✅ **Projeto Prático**: Sistema completo de gestêo de projetos

### 6.10.2 Melhores Práticas - Resumo

1. **Design de Tools**
   - Uma responsabilidade por tool
   - Validaçêo rigorosa de entradas
   - Idempotência quando possível
   - Confirmaçêo para operações destrutivas

2. **Design de Resources**
   - URIs hierárquicas e descritivas
   - Versionamento quando necessário
   - Metadados ricos
   - Cache quando apropriado

3. **Segurança**
   - Sempre autenticar e autorizar
   - Validar e sanitizar entradas
   - Implementar rate limiting
   - Auditar ações críticas
   - Proteger contra injeções

4. **Observabilidade**
   - Logging estruturado
   - Métricas de performance
   - Rastreamento de erros
   - Audit logs

### 6.10.3 Recursos Adicionais

**Documentaçêo Oficial:**
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/anthropics/mcp-python-sdk)
- [MCP Servers Collection](https://github.com/anthropics/mcp-servers)

**Servidores MCP Prontos:**
- `mcp-server-sqlite`: Acesso a bancos SQLite
- `mcp-server-filesystem`: Operações em arquivos
- `mcp-server-github`: Integraçêo com GitHub
- `mcp-server-google-drive`: Acesso ao Google Drive

**Ferramentas:**
- Claude Desktop: Cliente MCP integrado
- MCP Inspector: Ferramenta de debug para servidores MCP

### 6.10.4 Próximo Módulo

No **Módulo 7: Deploy e Produçêo**, você aprenderá:

🚀 Como fazer deploy de agentes em produçêo
📊 Monitoramento e observabilidade avançados
⚡ Otimizaçêo de performance e custos
🔒 Hardening de segurança para produçêo
☁️ Deploy em diferentes plataformas (AWS, GCP, Azure, etc.)
🐳 Containerizaçêo com Docker e Kubernetes
🔄 CI/CD para sistemas de agentes

### 6.10.5 Exercícios Práticos

**Nível 1 - Básico:**
1. Crie um servidor MCP simples com 3 tools personalizadas
2. Conecte um cliente Agno ao seu servidor
3. Implemente autenticaçêo básica com tokens

**Nível 2 - Intermediário:**
4. Crie um resource que retorna dados em tempo real
5. Implemente rate limiting por usuário
6. Crie um prompt dinâmico que use contexto de múltiplas sources

**Nível 3 - Avançado:**
7. Integre o servidor MCP com um banco de dados PostgreSQL
8. Implemente um sistema de permissões granulares
9. Crie um dashboard web que consome o servidor MCP via HTTP/SSE
10. Implemente circuit breaker e retry logic no cliente

---

## 📚 Referências

1. **Anthropic**. "Model Context Protocol Specification". 2024.
2. **JSON-RPC Working Group**. "JSON-RPC 2.0 Specification". 2010.
3. **OWASP**. "API Security Top 10". 2023.
4. **Martin Fowler**. "Patterns of Enterprise Application Architecture". 2002.

---

**Parabéns! 🎉**

Você completou o Módulo 6 e agora é capaz de criar sistemas robustos de agentes conectados ao mundo real usando o Model Context Protocol. Você aprendeu nêo apenas a teoria, mas também implementou um projeto completo de produçêo.

**No próximo módulo**, vamos levar seus agentes para produçêo com deploy profissional, monitoramento e otimizações avançadas!

---

*"A verdadeira inteligência de um agente nêo vem apenas do LLM, mas das conexões que ele pode fazer com o mundo real. O MCP é a ponte que torna isso possível."*

**→ Próximo: [Módulo 7 - Deploy e Produçêo](../modulo-07/conteudo/Modulo-07-Deploy-Producao.md)**
