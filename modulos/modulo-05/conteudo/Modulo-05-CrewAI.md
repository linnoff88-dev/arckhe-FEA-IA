# Módulo 5: Sistemas Multi-Agentes com CrewAI

**Duraçêo:** 12 horas | **Nível:** Avançado

> **Frase-guia:** "Sozinho você vai rápido. Em equipe, você vai longe." - Provérbio Africano

---

![Capa do Módulo 5](../../../imagens-conceituais/modulo5_crewai_multiagent.png)

## Ato 3: A Maestria

> "Você evoluiu de um conversador para um construtor, e de um construtor para um arquiteto. Agora, você se tornará um orquestrador. Este é o ápice da engenharia de agentes: a criaçêo de sistemas onde múltiplos especialistas de IA colaboram, delegam e resolvem problemas que nenhum agente conseguiria sozinho. Com CrewAI, você nêo está mais apenas dando ordens; você está montando uma equipe de elite."

Bem-vindo à **sala de comando**. Até agora, trabalhamos com agentes agindo de forma isolada ou em sequências simples. **CrewAI eleva o jogo** ao introduzir um framework robusto para a colaboraçêo entre agentes.

Inspirado em **equipes humanas eficazes**, ele nos permite:
- Definir **papéis claros**
- Delegar **tarefas específicas**
- Orquestrar **processos colaborativos**
- Resolver **problemas complexos**

Prepare-se para pensar como um **gerente de projetos de IA**, montando a "tripulaçêo" (crew) perfeita para qualquer missêo.

---

## Capítulo 5.1: Conceitos de Multi-Agent Systems (MAS)

### O Que Sêo Sistemas Multi-Agentes?

Um **Sistema Multi-Agentes (MAS)** é uma coleçêo de agentes autônomos que:
- Interagem entre si
- Compartilham informações
- Colaboram em objetivos comuns
- Competem ou negociam quando necessário

**Analogia:** Pense em uma **equipe de desenvolvimento de software**:
- **Product Owner:** Define o que construir
- **Arquiteto:** Planeja a soluçêo técnica
- **Desenvolvedores:** Implementam código
- **QA:** Testa e valida
- **DevOps:** Faz deploy

Cada membro tem expertise específica. Juntos, entregam o que nenhum conseguiria sozinho.

### Por Que Múltiplos Agentes?

#### 1. **Especializaçêo**

```
Agente Generalista:
- Sabe um pouco de tudo
- Mestre em nada
- Performance medíocre em tarefas específicas

vs.

Equipe de Especialistas:
- Pesquisador: 95% de precisêo em pesquisa
- Escritor: Qualidade editorial profissional
- Analista: Insights profundos de dados
```

**Resultado:** Qualidade superior em cada subtarefa.

#### 2. **Paralelismo**

```
Sequencial (1 agente):
Tarefa A → Tarefa B → Tarefa C → Tarefa D
Tempo total: 40 minutos

Paralelo (4 agentes):
Tarefa A ┐
Tarefa B ├→ Combinaçêo final
Tarefa C ┤
Tarefa D ┘
Tempo total: 12 minutos
```

#### 3. **Robustez**

Se um agente falha:
- Outro pode assumir a funçêo
- Sistema continua operacional
- Degradaçêo graceful

#### 4. **Modularidade**

```
❌ Agente Monolítico (10.000 linhas)
- Difícil de debugar
- Difícil de manter
- Difícil de testar

✅ 5 Agentes Especializados (2.000 linhas cada)
- Fácil de debugar
- Fácil de manter
- Fácil de testar
- Reutilizável
```

### Exemplos Reais de MAS

**1. Agência de Marketing Digital**
- **Estrategista:** Análise de mercado
- **Copywriter:** Criaçêo de textos
- **Designer:** Assets visuais
- **Analista:** Métricas e ROI

**2. Consultoria Jurídica**
- **Pesquisador:** Jurisprudência
- **Analista:** Análise de contratos
- **Redator:** Pareceres legais
- **Revisor:** Compliance

**3. Desenvolvimento de Software**
- **Arquiteto:** Design do sistema
- **Backend Dev:** APIs
- **Frontend Dev:** UI/UX
- **QA:** Testes automatizados

---

## Capítulo 5.2: A Arquitetura CrewAI

### Os 5 Componentes Fundamentais

```
┌─────────────────────────────────────────────┐
│                   CREW                      │
│  ┌───────────────────────────────────────┐ │
│  │           PROCESS                     │ │
│  │  (Sequential / Hierarchical)          │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Agent 1 │  │ Agent 2 │  │ Agent 3 │    │
│  │ + Tools │  │ + Tools │  │ + Tools │    │
│  └─────────┘  └─────────┘  └─────────┘    │
│                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Task 1  │  │ Task 2  │  │ Task 3  │    │
│  └─────────┘  └─────────┘  └─────────┘    │
└─────────────────────────────────────────────┘
```

#### 1. **Agents (Agentes)**

Sêo os **especialistas** da sua equipe.

**Definiçêo:**
```python
from crewai import Agent

agent = Agent(
    role="",           # Papel/funçêo
    goal="",           # Objetivo principal
    backstory="",      # História e contexto
    tools=[],          # Ferramentas disponíveis
    verbose=True,      # Logging detalhado
    allow_delegation=False,  # Pode delegar?
    max_iter=15,       # Máximo de iterações
    memory=True        # Memória de longo prazo
)
```

**Atributos-chave:**

- **`role`:** O que o agente faz
  ```python
  role="Senior Data Analyst"
  ```

- **`goal`:** Por que ele existe
  ```python
  goal="Extrair insights acionáveis de dados complexos"
  ```

- **`backstory`:** Quem ele é (persona)
  ```python
  backstory="""
  Você é um analista de dados sênior com 10 anos de experiência
  em análise preditiva e visualizaçêo de dados. Você trabalhou
  em Fortune 500 companies e é conhecido por transformar dados
  brutos em insights estratégicos que impulsionam decisões de
  negócio.
  """
  ```

- **`tools`:** O que ele pode fazer
  ```python
  tools=[search_tool, calculator, database_query]
  ```

#### 2. **Tasks (Tarefas)**

Sêo as **unidades de trabalho** específicas.

**Definiçêo:**
```python
from crewai import Task

task = Task(
    description="",        # O que fazer
    agent=agent,           # Quem faz
    expected_output="",    # Resultado esperado
    context=[],            # Tarefas de contexto
    output_file="",        # Salvar resultado
    callback=None          # Funçêo após conclusêo
)
```

**Atributos-chave:**

- **`description`:** Instruções detalhadas
  ```python
  description="""
  Analise o dataset de vendas (vendas_2024.csv) e:
  1. Identifique as 3 categorias de produtos com maior crescimento
  2. Calcule a taxa de crescimento mês a mês
  3. Identifique padrões sazonais
  4. Sugira 3 ações estratégicas baseadas nos dados
  """
  ```

- **`expected_output`:** Especificaçêo do resultado
  ```python
  expected_output="""
  Relatório em formato Markdown com:
  - Sumário executivo (3-5 bullets)
  - Análise detalhada por categoria
  - Gráficos e tabelas (formato markdown)
  - Recomendações acionáveis numeradas
  """
  ```

- **`context`:** Dependências de outras tasks
  ```python
  context=[research_task, data_cleaning_task]
  # Esta task terá acesso ao output das tasks no context
  ```

#### 3. **Tools (Ferramentas)**

Mesmas que vimos antes, mas agora **compartilhadas** entre agentes.

```python
from crewai_tools import (
    SerperDevTool,      # Busca web
    ScrapeWebsiteTool,  # Scraping
    FileReadTool,       # Ler arquivos
    DirectoryReadTool,  # Ler diretórios
)

# Custom tool
from crewai_tools import tool

@tool
def analyze_sentiment(text: str) -> str:
    """Analisa sentimento de um texto"""
    # Implementaçêo...
    return sentiment_score
```

#### 4. **Process (Processo)**

Define **como** as tasks sêo executadas.

**Opçêo 1: Sequential (Sequencial)**
```python
from crewai import Crew, Process

crew = Crew(
    agents=[agent1, agent2, agent3],
    tasks=[task1, task2, task3],
    process=Process.sequential  # Uma de cada vez, em ordem
)
```

**Fluxo:**
```
Task 1 (Agent 1) → Task 2 (Agent 2) → Task 3 (Agent 3)
     |                  |                   |
  Output 1          Output 2           Output 3
                                           ↓
                                      Resultado Final
```

**Opçêo 2: Hierarchical (Hierárquico)**
```python
crew = Crew(
    agents=[agent1, agent2, agent3],
    tasks=[task1, task2, task3],
    process=Process.hierarchical,  # Gerente orquestra
    manager_llm="gpt-4"            # LLM do gerente
)
```

**Fluxo:**
```
                  ┌─────────────┐
                  │   Manager   │
                  │   (GPT-4)   │
                  └─────────────┘
                        |
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
   ┌─────────┐    ┌─────────┐    ┌─────────┐
   │ Agent 1 │    │ Agent 2 │    │ Agent 3 │
   │ Task A  │    │ Task B  │    │ Task C  │
   └─────────┘    └─────────┘    └─────────┘
```

Manager decide:
- Qual agente usar
- Em que ordem
- Quando delegar
- Como combinar resultados

#### 5. **Crew (Tripulaçêo)**

A **equipe completa** montada.

```python
from crewai import Crew, Process

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, write_task, edit_task],
    process=Process.sequential,
    verbose=2,  # 0=silencioso, 1=básico, 2=detalhado
    memory=True,  # Memória compartilhada
    cache=True,   # Cache de resultados
    max_rpm=10    # Rate limiting
)

# Executar
result = crew.kickoff()
print(result)
```

---

## Capítulo 5.3: Criando Agentes Especializados

### Princípios de Design

#### 1. **Princípio da Responsabilidade Única**

```python
# ❌ Ruim: Agente faz tudo
jack_of_all_trades = Agent(
    role="Assistente Geral",
    goal="Fazer tudo",
    backstory="Faz um pouco de tudo"
)

# ✅ Bom: Agentes especializados
researcher = Agent(
    role="Pesquisador Sênior",
    goal="Encontrar informações precisas e relevantes",
    backstory="Especialista em pesquisa acadêmica e de mercado"
)

writer = Agent(
    role="Redator Criativo",
    goal="Criar conteúdo envolvente e persuasivo",
    backstory="Jornalista premiado com 15 anos de experiência"
)
```

#### 2. **Backstory Rico e Detalhado**

O `backstory` é seu **mega-prompt**. Invista tempo aqui!

```python
# ❌ Backstory fraco
backstory="Você é um analista de dados"

# ✅ Backstory rico
backstory="""
Você é Dr. Ana Silva, uma cientista de dados com PhD em Estatística
pela USP e 12 anos de experiência em análise preditiva.

EXPERTISE:
- Machine Learning e Estatística Avançada
- Visualizaçêo de dados (Matplotlib, Plotly, Tableau)
- SQL, Python, R
- Storytelling com dados

PERSONALIDADE:
- Meticulosa e orientada a detalhes
- Cética - só confia em dados validados
- Comunicadora clara - transforma complexidade em simplicidade
- Proativa em identificar insights nêo óbvios

ABORDAGEM:
1. Sempre valida qualidade dos dados primeiro
2. Usa múltiplas técnicas de análise para confirmar padrões
3. Contextualiza números com impacto de negócio
4. Questiona suposições e vieses

ESTILO DE COMUNICAÇêO:
- Objetiva e direta
- Usa analogias para explicar conceitos técnicos
- Sempre inclui nível de confiança em suas conclusões
- Destaca limitações e riscos
"""
```

#### 3. **Goals Específicos e Mensuráveis**

```python
# ❌ Goal vago
goal="Fazer bom trabalho"

# ✅ Goal específico
goal="""
Analisar dados de vendas para identificar oportunidades de crescimento,
garantindo que:
- Insights sejam baseados em dados verificados
- Recomendações tenham ROI estimado
- Análise seja concluída em <10 minutos
- Relatório seja compreensível para nêo-técnicos
"""
```

### Templates de Agentes por Funçêo

#### Agente Pesquisador

```python
from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

researcher = Agent(
    role="Pesquisador de Mercado Sênior",

    goal="""
    Encontrar e validar informações precisas e atualizadas sobre
    tendências de mercado, competidores e oportunidades de negócio
    """,

    backstory="""
    Você é um pesquisador de mercado com 15 anos de experiência em
    inteligência competitiva. Trabalhou em McKinsey e BCG, liderando
    análises de mercado para Fortune 500.

    ESPECIALIDADES:
    - Pesquisa primária e secundária
    - Análise competitiva
    - Identificaçêo de tendências emergentes
    - Validaçêo de fontes

    METODOLOGIA:
    1. Triangulaçêo de fontes (mínimo 3 fontes independentes)
    2. Priorizaçêo de dados recentes (<6 meses)
    3. Verificaçêo de credibilidade de fontes
    4. Documentaçêo de todas as referências

    PERSONALIDADE:
    - Cético e rigoroso
    - Curiosidade intelectual
    - Atençêo obsessiva a detalhes
    - Compromisso com precisêo factual
    """,

    tools=[search_tool, scrape_tool],
    verbose=True,
    allow_delegation=False  # Pesquisador nêo delega
)
```

#### Agente Escritor

```python
writer = Agent(
    role="Redator de Conteúdo Sênior",

    goal="""
    Criar conteúdo envolvente, persuasivo e otimizado para SEO
    que converte leitores em clientes
    """,

    backstory="""
    Você é Sofia Martins, redatora de conteúdo com 10 anos de experiência
    em marketing digital e jornalismo.

    CONQUISTAS:
    - Artigos publicados em TechCrunch, Wired, The Verge
    - 3x vencedora do prêmio de Content Marketing Institute
    - Especialista em storytelling B2B e B2C
    - Taxa de conversêo média: 8% (indústria: 2%)

    EXPERTISE:
    - Copywriting persuasivo
    - SEO content optimization
    - Storytelling narrativo
    - Adaptaçêo de tom para diferentes audiências

    PRINCÍPIOS:
    - Headline que captura atençêo em <3 segundos
    - Primeiro parágrafo responde "por que devo ler isso?"
    - Estrutura clara: Intro → Desenvolvimento → Call-to-Action
    - Cada parágrafo tem um objetivo claro
    - Usa dados e estatísticas para credibilidade
    - Inclui exemplos concretos e casos de uso

    ESTILO:
    - Voz ativa e energética
    - Sentenças curtas e impactantes
    - Metáforas e analogias para conceitos complexos
    - Equilíbrio entre profissionalismo e acessibilidade
    """,

    tools=[],  # Escritor geralmente nêo precisa de tools externas
    verbose=True,
    allow_delegation=False
)
```

#### Agente Editor

```python
editor = Agent(
    role="Editor-Chefe",

    goal="""
    Garantir que todo conteúdo publicado seja impecável em
    qualidade, precisêo, estilo e alinhamento com brand guidelines
    """,

    backstory="""
    Você é Roberto Alves, editor-chefe com 20 anos de experiência
    editorial em grandes publicações.

    BACKGROUND:
    - Ex-editor da Folha de S.Paulo
    - Graduado em Jornalismo e Letras
    - Especializaçêo em ediçêo de conteúdo digital
    - Membro da Associaçêo Brasileira de Editores

    RESPONSABILIDADES:
    - Fact-checking rigoroso
    - Verificaçêo de gramática e ortografia
    - Consistência de tom e voz
    - Estrutura e flow narrativo
    - SEO e otimizaçêo de performance
    - Compliance com guidelines editoriais

    CHECKLIST DE EDIÇêO:
    □ Headline clara e atraente?
    □ Lead responde quem, o quê, quando, onde, por quê?
    □ Estrutura lógica e fácil de seguir?
    □ Transições suaves entre parágrafos?
    □ Fatos verificados e fontes citadas?
    □ Zero erros gramaticais/ortográficos?
    □ Tom consistente com brand voice?
    □ Call-to-action claro?
    □ Formataçêo (títulos, listas, negrito) otimizada?
    □ Length apropriado para o formato?

    PERSONALIDADE:
    - Perfeccionista (no bom sentido)
    - Olho de águia para detalhes
    - Diplomático ao dar feedback
    - Defensor do leitor
    """,

    tools=[],
    verbose=True,
    allow_delegation=False
)
```

---

## Capítulo 5.4: Design de Tasks Eficazes

### Anatomia de uma Task Perfeita

```python
from crewai import Task

task = Task(
    description="""
    [OBJETIVO CLARO]
    [CONTEXTO E REQUISITOS]
    [INSTRUÇÕES PASSO-A-PASSO]
    [RESTRIÇÕES E GUARDRAILS]
    """,

    agent=assigned_agent,

    expected_output="""
    [FORMATO ESPECÍFICO]
    [CONTEÚDO MÍNIMO ESPERADO]
    [CRITÉRIOS DE QUALIDADE]
    """,

    context=[previous_tasks],  # Dependências
    output_file="result.md",   # Onde salvar
)
```

### Exemplo Completo: Task de Pesquisa

```python
research_task = Task(
    description="""
    **OBJETIVO:**
    Pesquisar e analisar o mercado de Inteligência Artificial Generativa
    no Brasil em 2024.

    **CONTEXTO:**
    Nossa empresa está considerando lançar uma plataforma de IA Gen no
    mercado brasileiro e precisa entender:
    - Tamanho do mercado e projeções
    - Principais players e competidores
    - Tendências e oportunidades
    - Barreiras de entrada e desafios

    **INSTRUÇÕES:**

    1. PESQUISAR tamanho do mercado:
       - Valor atual (em R$)
       - Taxa de crescimento (CAGR 2024-2028)
       - Principais segmentos (B2B vs B2C)

    2. IDENTIFICAR competidores principais:
       - Liste top 5 players
       - Para cada: produto, market share, diferencial competitivo
       - Empresas internacionais que entraram recentemente

    3. ANALISAR tendências:
       - 3 principais tendências emergentes
       - Casos de uso mais populares
       - Tecnologias dominantes (GPT-4, Claude, etc.)

    4. MAPEAR desafios:
       - Barreiras regulatórias (LGPD, etc.)
       - Desafios técnicos (infraestrutura, custos)
       - Percepçêo do mercado

    **REQUISITOS:**
    - Priorize fontes de 2024 (últimos 6 meses)
    - Cite todas as fontes com URLs
    - Valide informações em múltiplas fontes
    - Destaque dados quantitativos com unidades claras

    **RESTRIÇÕES:**
    - Nêo especule - apenas dados verificáveis
    - Se nêo encontrar dado específico, indique claramente
    - Máximo 30 minutos de pesquisa
    """,

    agent=researcher,

    expected_output="""
    Relatório de pesquisa em Markdown com esta estrutura:

    # Análise de Mercado: IA Generativa no Brasil 2024

    ## 1. Sumário Executivo
    - 3-5 bullets com principais findings

    ## 2. Tamanho e Crescimento do Mercado
    - Valor atual: R$ X bilhões
    - CAGR 2024-2028: X%
    - Segmentaçêo B2B/B2C: percentuais

    ## 3. Análise Competitiva
    ### Player 1: [Nome]
    - Produto:
    - Market Share:
    - Diferencial:
    - Fonte: [URL]

    [Repetir para top 5]

    ## 4. Tendências Emergentes
    1. Tendência 1
       - Descriçêo
       - Evidências
       - Fonte: [URL]

    [Repetir para 3 tendências]

    ## 5. Desafios e Barreiras
    - Regulatórios:
    - Técnicos:
    - Mercado:

    ## 6. Fontes Consultadas
    - [Lista completa de URLs]
    """,

    output_file="research_report.md"
)
```

### Context: Passando Informaçêo Entre Tasks

```python
# Task 1: Pesquisar
task_research = Task(
    description="Pesquise sobre IA em educaçêo",
    agent=researcher,
    expected_output="Resumo de pesquisa em 3 parágrafos"
)

# Task 2: Escrever (usa resultado da Task 1)
task_write = Task(
    description="""
    Use os dados da pesquisa para escrever um artigo de blog.

    PESQUISA DISPONÍVEL:
    {task_research.output}

    Crie um artigo de 800 palavras baseado nesses dados.
    """,
    agent=writer,
    context=[task_research],  # Acessa output da task_research
    expected_output="Artigo em Markdown"
)

# Task 3: Editar (usa resultado da Task 2)
task_edit = Task(
    description="""
    Revise e edite o artigo a seguir:

    {task_write.output}

    Aplique checklist editorial completo.
    """,
    agent=editor,
    context=[task_write],
    expected_output="Artigo editado e finalizado"
)
```

---

## Capítulo 5.5: Processos e Workflows

### Process.sequential

Tarefas executadas em **ordem fixa**, uma por vez.

```python
from crewai import Crew, Process

content_crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[task_research, task_write, task_edit],
    process=Process.sequential,
    verbose=2
)

result = content_crew.kickoff()
```

**Execuçêo:**
```
┌──────────────────────────────────────────┐
│ 1. RESEARCH (Researcher)                 │
│    ├─ Busca web...                       │
│    ├─ Analisa fontes...                  │
│    └─ Output: research_report.md         │
└──────────────────────────────────────────┘
                ↓
┌──────────────────────────────────────────┐
│ 2. WRITE (Writer)                        │
│    ├─ Lê research_report.md              │
│    ├─ Escreve artigo...                  │
│    └─ Output: article_draft.md           │
└──────────────────────────────────────────┘
                ↓
┌──────────────────────────────────────────┐
│ 3. EDIT (Editor)                         │
│    ├─ Lê article_draft.md                │
│    ├─ Revisa e edita...                  │
│    └─ Output: article_final.md ✓         │
└──────────────────────────────────────────┘
```

**Quando usar:**
- Workflow linear claro
- Dependências sequenciais
- Ordem de execuçêo crítica

### Process.hierarchical

**Manager AI** decide ordem, delegaçêo e coordenaçêo.

```python
content_crew = Crew(
    agents=[researcher, writer, editor, fact_checker],
    tasks=[task1, task2, task3, task4],
    process=Process.hierarchical,
    manager_llm="gpt-4",  # LLM usado pelo gerente
    verbose=2
)

result = content_crew.kickoff()
```

**Execuçêo:**
```
┌─────────────────────────────────────┐
│     AI MANAGER (GPT-4)              │
│  "Analisar objetivo e planejar..."  │
└─────────────────────────────────────┘
         │
         ├─ Decisêo: "Pesquisa primeiro é essencial"
         ↓
┌─────────────────┐
│   Researcher    │ → Executa pesquisa
└─────────────────┘
         ↓
┌─────────────────────────────────────┐
│     AI MANAGER                      │
│  "Pesquisa concluída. Avaliar se   │
│   dados sêo suficientes ou se      │
│   precisa fact-checking adicional" │
└─────────────────────────────────────┘
         │
         ├─ Decisêo: "Dados OK, seguir para escrita"
         ↓
┌─────────────────┐
│     Writer      │ → Escreve artigo
└─────────────────┘
         ↓
┌─────────────────────────────────────┐
│     AI MANAGER                      │
│  "Artigo pronto. Delegando para   │
│   Editor E Fact-checker em         │
│   PARALELO para otimizar tempo"    │
└─────────────────────────────────────┘
         │
    ┌────┴────┐
    ↓         ↓
┌────────┐  ┌──────────────┐
│ Editor │  │ Fact-Checker │
└────────┘  └──────────────┘
    │         │
    └────┬────┘
         ↓
    [Resultado Final]
```

**Vantagens:**
- **Flexibilidade:** Adapta-se a situações inesperadas
- **Otimizaçêo:** Pode executar tasks em paralelo quando possível
- **Inteligência:** Decide baseado em contexto e resultados
- **Recovery:** Pode requisitar re-trabalho se necessário

**Quando usar:**
- Problemas complexos e nêo-lineares
- Quando ordem ideal nêo é clara antecipadamente
- Quando tasks podem ser paralelizadas
- Projetos que podem precisar de pivots

---

## Capítulo 5.6: Tools e Integrações

### CrewAI Tools Built-in

```python
from crewai_tools import (
    # Busca e Web
    SerperDevTool,        # Google Search via Serper
    ScrapeWebsiteTool,    # Web scraping
    WebsiteSearchTool,    # Busca em site específico

    # Arquivos
    FileReadTool,         # Ler arquivos
    FileWriteTool,        # Escrever arquivos
    DirectoryReadTool,    # Ler diretório
    DirectorySearchTool,  # Buscar em diretório

    # Código
    CodeDocsSearchTool,   # Busca em documentaçêo
    GithubSearchTool,     # Busca no GitHub

    # Dados
    CSVSearchTool,        # Busca em CSV
    JSONSearchTool,       # Busca em JSON
    XMLSearchTool,        # Busca em XML

    # Multimídia
    YoutubeVideoSearchTool,  # Busca em vídeos
    YoutubeChannelSearchTool, # Busca em canais

    # Browsers
    BrowserbaseTool,      # Browser automation
    SeleniumScrapingTool, # Scraping com Selenium
)
```

### Exemplo: Setup de Tools

```python
# 1. Configurar API keys
import os
os.environ["SERPER_API_KEY"] = "seu-serper-key"
os.environ["OPENAI_API_KEY"] = "seu-openai-key"

# 2. Inicializar tools
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileReadTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_tool = FileReadTool(file_path="./data/knowledge_base.txt")

# 3. Criar tool customizada
from crewai_tools import tool

@tool
def analyze_competitors(company_name: str) -> str:
    """
    Analisa competidores de uma empresa.

    Args:
        company_name: Nome da empresa a analisar
    """
    # Implementaçêo...
    return analysis_report

# 4. Atribuir tools a agentes
researcher = Agent(
    role="Researcher",
    tools=[search_tool, scrape_tool, read_tool, analyze_competitors]
)
```

### Custom Tools Avançadas

#### Tool com Database

```python
from crewai_tools import tool
import sqlite3

@tool
def query_sales_database(query: str) -> str:
    """
    Executa consulta SQL no banco de vendas.

    Args:
        query: Query SQL (SELECT apenas)
    """
    # Segurança: permitir apenas SELECT
    if not query.strip().upper().startswith("SELECT"):
        return "Erro: Apenas queries SELECT sêo permitidas"

    try:
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        columns = [description[0] for description in cursor.description]

        # Formatar como tabela markdown
        table = "| " + " | ".join(columns) + " |\n"
        table += "|" + "|".join(["---" for _ in columns]) + "|\n"

        for row in results:
            table += "| " + " | ".join(str(v) for v in row) + " |\n"

        conn.close()
        return table

    except Exception as e:
        return f"Erro na consulta: {str(e)}"
```

#### Tool com API Externa

```python
@tool
def get_stock_price(ticker: str) -> str:
    """
    Retorna preço atual de uma açêo.

    Args:
        ticker: Símbolo da açêo (ex: AAPL, GOOGL)
    """
    import requests

    url = f"https://api.example.com/stock/{ticker}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"{ticker}: ${data['price']} ({data['change']}%)"
    else:
        return f"Erro ao buscar preço de {ticker}"
```

---

## Capítulo 5.7: Memory e Knowledge Sharing

### Tipos de Memory no CrewAI

#### 1. Short-Term Memory (Padrêo)

Memória da execuçêo atual.

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True  # Ativa memória
)
```

Agentes lembram:
- Conversas anteriores na mesma execuçêo
- Resultados de tasks anteriores
- Decisões tomadas

#### 2. Long-Term Memory

Memória persistente entre execuções.

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True,
    memory_config={
        "provider": "mem0",  # Provedor de memória
        "config": {
            "api_key": "mem0-api-key"
        }
    }
)
```

Agentes lembram:
- Execuções anteriores
- Aprendizados acumulados
- Padrões identificados
- Preferências do usuário

#### 3. Entity Memory

Memória estruturada sobre entidades.

```python
# Automaticamente extrai e lembra:
# - Pessoas mencionadas
# - Empresas
# - Produtos
# - Datas importantes
# - Relacionamentos
```

### Knowledge Base Compartilhada

```python
from crewai_tools import FileReadTool, DirectoryReadTool

# Knowledge base como tool
kb_tool = DirectoryReadTool(directory="./knowledge_base")

# Todos os agentes têm acesso
researcher = Agent(tools=[search_tool, kb_tool])
writer = Agent(tools=[kb_tool])
editor = Agent(tools=[kb_tool])
```

---

## Capítulo 5.8: Observabilidade com AgentOps

### Por Que Observabilidade?

Sistemas multi-agentes sêo **caixas-pretas complexas**. Você precisa saber:
- Qual agente está trabalhando?
- Quanto tempo cada task leva?
- Quantos tokens foram usados?
- Quanto $$ você está gastando?
- Por que um agente tomou uma decisêo?
- Onde está o bottleneck?

**AgentOps** resolve isso.

### Setup do AgentOps

```python
# 1. Instalar
pip install agentops

# 2. Criar conta e pegar API key
# https://agentops.ai

# 3. Inicializar (2 linhas!)
import agentops

agentops.init(api_key="sua-agentops-key")

# 4. Criar crew normalmente
crew = Crew(...)
result = crew.kickoff()

# 5. Encerrar sessêo
agentops.end_session("Success")
```

**Isso é tudo!** AgentOps automaticamente rastreia tudo.

### O Que Você Vê no Dashboard

**1. Session Overview**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Session ID: abc123
Duration: 4m 32s
Status: ✅ Success
Total Cost: $0.42
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**2. Agent Timeline**
```
Researcher  ████████░░░░░░░░ (2m 15s)
Writer      ░░░░░░░░██████░░ (1m 45s)
Editor      ░░░░░░░░░░░░░███ (0m 32s)
```

**3. LLM Calls**
```
Model: gpt-4
Calls: 27
Tokens: 45,234
  ├─ Prompt: 32,100
  └─ Completion: 13,134
Cost: $0.42
```

**4. Tool Usage**
```
search_tool: 12 calls (avg 3.2s)
scrape_tool: 5 calls (avg 8.1s)
analyze_data: 3 calls (avg 1.4s)
```

**5. Thought Process (RAW)**
```
[Researcher] Thought: Preciso buscar dados sobre IA no Brasil
[Researcher] Action: search_tool
[Researcher] Action Input: "AI market Brazil 2024"
[Researcher] Observation: Found 10 results...
[Researcher] Thought: Vou analisar os 3 primeiros...
```

### Rastreamento Avançado

```python
import agentops

# Inicializar com tags
agentops.init(
    api_key="key",
    tags=["production", "content-generation", "v2.1"]
)

# Eventos customizados
agentops.record_event(
    name="content_published",
    properties={
        "topic": "AI in Healthcare",
        "word_count": 1250,
        "quality_score": 8.5
    }
)

# Erros e exceções
try:
    result = crew.kickoff()
    agentops.end_session("Success")
except Exception as e:
    agentops.record_error(str(e))
    agentops.end_session("Fail")
```

---

## 📝 Resumo Gráfico do Módulo 5

### Conceitos-Chave

**Multi-Agent Systems:**
- Especializaçêo > Generalizaçêo
- Colaboraçêo > Isolamento
- Inteligência coletiva

**Arquitetura CrewAI:**
```
Crew = Agents + Tasks + Process + Tools + Memory
```

**Componentes:**
1. **Agent:** role + goal + backstory + tools
2. **Task:** description + expected_output + context
3. **Process:** Sequential | Hierarchical
4. **Tools:** Built-in + Custom
5. **Memory:** Short-term + Long-term

**Best Practices:**
- Backstory detalhado
- Tasks bem especificadas
- Um agente, uma responsabilidade
- Observabilidade com AgentOps

---

## 🚀 Projeto Prático: Agência de Criaçêo de Conteúdo

### Objetivo

Criar uma **crew completa** que produz artigos de blog de alta qualidade de forma totalmente autônoma.

### Especificações

**Input:** Tópico do artigo
**Output:** Artigo completo, editado e otimizado para SEO

**Workflow:**
1. **Pesquisar** → Dados e referências
2. **Planejar** → Estrutura do artigo
3. **Escrever** → Rascunho completo
4. **Editar** → Revisêo e polimento
5. **Otimizar SEO** → Keywords e meta

### Implementaçêo Completa

**Arquivo: `content_agency.py`**

```python
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
import agentops

# ============== CONFIGURAÇêO ==============

os.environ["OPENAI_API_KEY"] = "sk-..."
os.environ["SERPER_API_KEY"] = "..."

# AgentOps para observabilidade
agentops.init(api_key="...", tags=["content-agency"])

# Tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# ============== AGENTES ==============

researcher = Agent(
    role="Pesquisador de Conteúdo Sênior",

    goal="""
    Encontrar informações precisas, atualizadas e relevantes
    sobre o tópico, identificando dados, estatísticas, tendências
    e referências confiáveis.
    """,

    backstory="""
    Você é um pesquisador experiente com background em jornalismo
    investigativo. Trabalhou para The New York Times e Reuters,
    especializando-se em fact-checking e pesquisa aprofundada.

    METODOLOGIA:
    - Sempre valida informações em múltiplas fontes
    - Prioriza fontes primárias e dados recentes
    - Documenta todas as referências meticulosamente
    - Identifica tendências e insights nêo-óbvios

    EXPERTISE:
    - Pesquisa acadêmica e de mercado
    - Análise de dados e estatísticas
    - Verificaçêo de fontes e credibilidade
    - Identificaçêo de vieses e falácias
    """,

    tools=[search_tool, scrape_tool],
    verbose=True,
    allow_delegation=False
)

planner = Agent(
    role="Planejador de Conteúdo Estratégico",

    goal="""
    Criar estruturas de artigos estratégicas e envolventes que
    maximizam engajamento, SEO e conversêo.
    """,

    backstory="""
    Você é um estrategista de conteúdo com MBA em Marketing Digital
    e 12 anos de experiência em content strategy para marcas B2B e B2C.

    ESPECIALIDADES:
    - Arquitetura de informaçêo
    - User journey e intent matching
    - SEO content strategy
    - Storytelling frameworks

    ABORDAGEM:
    1. Analisa audiência-alvo e intent
    2. Define estrutura que guia o leitor naturalmente
    3. Incorpora SEO sem sacrificar qualidade
    4. Posiciona CTAs estrategicamente
    5. Otimiza para scanability e engagement

    FRAMEWORKS FAVORITOS:
    - AIDA (Attention, Interest, Desire, Action)
    - PAS (Problem, Agitate, Solution)
    - Hero's Journey
    """,

    tools=[],
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role="Redator de Conteúdo Premium",

    goal="""
    Escrever artigos excepcionais que educam, engajam e convertem,
    mantendo voz de marca consistente e qualidade editorial superior.
    """,

    backstory="""
    Você é uma redatora premiada com portfólio em publicações de
    prestígio (Wired, TechCrunch, Harvard Business Review).

    CONQUISTAS:
    - 5x Content Marketing Award winner
    - Artigos com média de 15min de time-on-page
    - Taxa de conversêo 3x acima da média da indústria

    ESTILO:
    - Voz ativa e dinâmica
    - Sentenças curtas e impactantes
    - Metáforas memoráveis
    - Dados que contam histórias
    - Exemplos concretos e acionáveis

    PRINCÍPIOS:
    - Headline que para o scroll
    - Primeiro parágrafo que prende
    - Cada seçêo entrega valor
    - Flow natural de leitura
    - CTA irresistível
    """,

    tools=[],
    verbose=True,
    allow_delegation=False
)

editor = Agent(
    role="Editor-Chefe de Conteúdo",

    goal="""
    Garantir excelência editorial através de revisêo rigorosa,
    fact-checking, otimizaçêo de SEO e alinhamento com brand voice.
    """,

    backstory="""
    Você é um editor-chefe com 20 anos de experiência editorial,
    incluindo passagens por The Economist e The Atlantic.

    EXPERTISE:
    - Ediçêo de conteúdo longo e curto
    - SEO on-page optimization
    - Fact-checking e verificaçêo
    - Brand voice consistency
    - Performance optimization

    CHECKLIST EDITORIAL:
    □ Fact-checking completo (dados, estatísticas, claims)
    □ Grammar & spelling impecáveis
    □ Estrutura lógica e flow
    □ Tone & voice consistentes
    □ SEO: keywords naturalmente integradas
    □ Headlines e subheadlines otimizadas
    □ Meta description atraente (<160 chars)
    □ Links internos e externos relevantes
    □ Formataçêo (bold, listas, quotes) estratégica
    □ CTA claro e persuasivo
    □ Scanability otimizada

    PERSONALIDADE:
    - Perfeccionista com deadline discipline
    - Defensor incansável do leitor
    - Equilibra qualidade com pragmatismo
    """,

    tools=[],
    verbose=True,
    allow_delegation=False
)

# ============== TASKS ==============

task_research = Task(
    description="""
    **TÓPICO:** {topic}

    **MISSêO:**
    Conduzir pesquisa aprofundada sobre o tópico para coletar:
    - Dados e estatísticas recentes (priorize 2024)
    - Tendências e insights do mercado
    - Casos de uso e exemplos concretos
    - Opiniões de especialistas e thought leaders
    - Referências e fontes confiáveis

    **METODOLOGIA:**
    1. Pesquise em fontes diversas (artigos, estudos, reports)
    2. Valide informações importantes em múltiplas fontes
    3. Documente todas as referências com URLs
    4. Identifique ângulos únicos e insights diferenciados
    5. Compile dados em formato estruturado

    **DELIVERABLE:**
    Relatório de pesquisa com:
    - Sumário executivo (principais findings)
    - Dados e estatísticas (com fontes)
    - Tendências identificadas
    - Casos de uso e exemplos
    - Referências completas (mínimo 5 fontes)
    """,

    agent=researcher,

    expected_output="""
    Documento estruturado em Markdown contendo:

    # Pesquisa: [Tópico]

    ## Sumário Executivo
    - [3-5 bullets com principais insights]

    ## Dados e Estatísticas
    - Dado 1: [valor] (Fonte: [URL])
    - Dado 2: [valor] (Fonte: [URL])
    [...]

    ## Tendências
    1. Tendência 1
       - Descriçêo
       - Evidências
       - Fonte

    ## Casos de Uso
    - Exemplo 1: [descriçêo]
    - Exemplo 2: [descriçêo]

    ## Referências
    1. [Título] - [URL]
    2. [Título] - [URL]
    [...]
    """
)

task_plan = Task(
    description="""
    **PESQUISA DISPONÍVEL:**
    {task_research.output}

    **MISSêO:**
    Criar estrutura estratégica para artigo de blog otimizado
    para SEO e engajamento.

    **REQUISITOS:**
    1. Analise dados da pesquisa
    2. Defina angle único e compelling
    3. Crie estrutura com 5-7 seções principais
    4. Posicione keywords naturalmente
    5. Defina CTAs estratégicos

    **ESTRUTURA DEVE INCLUIR:**
    - Headline attention-grabbing
    - Intro que hook o leitor
    - Seções lógicas e progressivas
    - Exemplos e dados posicionados estrategicamente
    - Conclusêo com CTA forte

    **DELIVERABLE:**
    Outline detalhado do artigo
    """,

    agent=planner,

    context=[task_research],

    expected_output="""
    # Outline: [Título Working]

    ## Headline Options
    1. [Opçêo 1]
    2. [Opçêo 2]
    3. [Opçêo 3]

    ## Meta Description
    [150-160 caracteres]

    ## Estrutura

    ### 1. Introduçêo (150 palavras)
    - Hook: [como começar]
    - Promise: [o que o leitor vai aprender]
    - Relevância: [por que isso importa]

    ### 2. [Seçêo 1 - Título]
    - Ponto principal:
    - Dados/exemplos:
    - Takeaway:

    ### 3. [Seçêo 2 - Título]
    [...]

    ### Conclusêo
    - Resumo:
    - CTA:

    ## Keywords
    - Primary: [keyword]
    - Secondary: [keyword 1], [keyword 2], [keyword 3]

    ## Estimated Length
    1200-1500 palavras
    """
)

task_write = Task(
    description="""
    **OUTLINE:**
    {task_plan.output}

    **PESQUISA:**
    {task_research.output}

    **MISSêO:**
    Escrever artigo excepcional seguindo o outline, incorporando
    dados da pesquisa e mantendo voz de marca profissional mas acessível.

    **GUIDELINES:**
    - Siga estrutura do outline rigorosamente
    - Use dados e estatísticas da pesquisa
    - Incorporate keywords naturalmente
    - Escreva de forma clara e envolvente
    - Use exemplos concretos
    - Mantenha parágrafos curtos (3-4 linhas)
    - Varie estrutura de sentenças
    - Use voz ativa
    - Inclua subheadings descritivos

    **TARGET:**
    1200-1500 palavras

    **DELIVERABLE:**
    Artigo completo em Markdown
    """,

    agent=writer,

    context=[task_research, task_plan],

    expected_output="""
    Artigo completo em Markdown com:
    - Headline final
    - Meta description
    - Introduçêo compelling
    - Corpo bem estruturado
    - Conclusêo com CTA
    - Formataçêo adequada (headings, listas, bold)
    """
)

task_edit = Task(
    description="""
    **ARTIGO PARA EDITAR:**
    {task_write.output}

    **MISSêO:**
    Revisar e polir o artigo aplicando checklist editorial completo.

    **CHECKLIST:**
    □ Fact-check todos os dados e claims
    □ Corrigir erros gramaticais e ortográficos
    □ Otimizar headlines e subheadings
    □ Verificar flow e transições
    □ Garantir keywords bem posicionadas
    □ Melhorar scanability (listas, bold, quotes)
    □ Fortalecer CTA
    □ Adicionar links internos/externos relevantes
    □ Verificar length (ideal: 1200-1500 palavras)

    **SE NECESSÁRIO:**
    - Reescreva seções fracas
    - Adicione exemplos faltantes
    - Melhore clareza
    - Fortaleça argumentos

    **DELIVERABLE:**
    Artigo final publish-ready
    """,

    agent=editor,

    context=[task_write, task_research, task_plan],

    expected_output="""
    # [TÍTULO FINAL OTIMIZADO]

    **Meta Description:** [150-160 chars]

    [ARTIGO COMPLETO E EDITADO]

    ---

    ## Metadata

    **Word Count:** [número]
    **Reading Time:** [X] minutos
    **Primary Keyword:** [keyword]
    **Secondary Keywords:** [lista]

    ## SEO Score: [estimativa de qualidade]
    """
)

# ============== CREW ==============

content_crew = Crew(
    agents=[researcher, planner, writer, editor],

    tasks=[task_research, task_plan, task_write, task_edit],

    process=Process.sequential,

    verbose=2,  # Logging detalhado

    memory=True,  # Compartilhar contexto

    cache=True,  # Cache de resultados
)

# ============== EXECUÇêO ==============

if __name__ == "__main__":
    print("="*60)
    print("🚀 AGÊNCIA DE CRIAÇêO DE CONTEÚDO")
    print("="*60)

    topic = input("\n📝 Digite o tópico do artigo: ")

    print(f"\n🎯 Tópico: {topic}")
    print("\n⏳ Iniciando produçêo do artigo...\n")

    try:
        result = content_crew.kickoff(inputs={"topic": topic})

        print("\n" + "="*60)
        print("✅ ARTIGO CONCLUÍDO!")
        print("="*60)
        print(result)

        # Salvar resultado
        with open("article_final.md", "w", encoding="utf-8") as f:
            f.write(str(result))

        print("\n💾 Artigo salvo em: article_final.md")

        agentops.end_session("Success")

    except Exception as e:
        print(f"\n❌ Erro: {e}")
        agentops.end_session("Fail")
```

### Como Executar

```bash
# 1. Instalar dependências
pip install crewai crewai-tools agentops python-dotenv

# 2. Configurar .env
OPENAI_API_KEY=sk-...
SERPER_API_KEY=...
AGENTOPS_API_KEY=...

# 3. Executar
python content_agency.py
```

### Exemplo de Uso

```
🚀 AGÊNCIA DE CRIAÇêO DE CONTEÚDO

📝 Digite o tópico do artigo: Impacto da IA Generativa na Educaçêo

🎯 Tópico: Impacto da IA Generativa na Educaçêo

⏳ Iniciando produçêo do artigo...

[Researcher] Iniciando pesquisa sobre: Impacto da IA...
[Researcher] Usando: search_tool
[Researcher] Encontrados 15 resultados relevantes
[Researcher] Analisando fontes...
[Researcher] ✓ Pesquisa concluída

[Planner] Analisando dados da pesquisa...
[Planner] Criando estrutura do artigo...
[Planner] ✓ Outline criado

[Writer] Escrevendo artigo baseado no outline...
[Writer] Seçêo 1 completa...
[Writer] Seçêo 2 completa...
[Writer] ✓ Artigo escrito (1.342 palavras)

[Editor] Revisando artigo...
[Editor] Fact-checking: OK
[Editor] Grammar: 3 correções aplicadas
[Editor] SEO: Keywords bem posicionadas
[Editor] ✓ Ediçêo concluída

✅ ARTIGO CONCLUÍDO!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Artigo completo aqui...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💾 Artigo salvo em: article_final.md
```

---

## 💡 Conclusêo e Próximos Passos

### O que você dominou:

✓ **Conceitos de Multi-Agent Systems**
✓ **Arquitetura completa do CrewAI**
✓ **Design de agentes especializados**
✓ **Criaçêo de tasks eficazes**
✓ **Processos Sequential e Hierarchical**
✓ **Tools e integrações**
✓ **Memory compartilhada**
✓ **Observabilidade com AgentOps**
✓ **Projeto production-ready**

### Você agora é capaz de:

- Montar equipes de agentes para qualquer domínio
- Orquestrar workflows complexos
- Delegar inteligentemente
- Monitorar performance e custos
- Construir sistemas escaláveis

---

**No Módulo 6**, exploraremos o **Model Context Protocol (MCP)**, um padrêo revolucionário que universaliza como agentes acessam ferramentas, permitindo que sua crew se conecte a **QUALQUER sistema** de forma padronizada.

---

**Continue para o Módulo 6: Model Context Protocol (MCP)** →
