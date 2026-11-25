#!/usr/bin/env python3
"""
Script para adicionar tópicos expansíveis em todos os módulos
das páginas de níveis (aplicacao.html e estrategico.html)
"""

import re

# Definiçêo dos tópicos para cada módulo
MODULOS_TOPICS = {
    # APLICAÇêO
    "modulo-04": {
        "file": "niveis/aplicacao.html",
        "topics": [
            ("Filosofia Agno: Simplicidade radical", """
                <p><strong>O que você aprenderá:</strong></p>
                <p>Entenda a filosofia por trás do Agno:</p>
                <ul>
                    <li><strong>Zero boilerplate:</strong> Código limpo sem configurações complexas</li>
                    <li><strong>Type-safe:</strong> Pydantic para validaçêo automática</li>
                    <li><strong>Multi-model:</strong> Trocar entre GPT-4, Claude, Gemini sem reescrever código</li>
                    <li><strong>Production-ready:</strong> Built-in retry, caching, observability</li>
                </ul>
                <p><strong>💡 Diferencial:</strong> Criar agentes poderosos com 10x menos código que frameworks complexos.</p>
            """),
            ("Criando agentes com Agno Agent", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Agent class:</strong> Interface simples para criar agentes</li>
                    <li><strong>Tools:</strong> Decorador @agent.tool() para adicionar ferramentas</li>
                    <li><strong>Streaming:</strong> Respostas em tempo real</li>
                    <li><strong>Structured outputs:</strong> Pydantic models como saída</li>
                </ul>
                <p><strong>🔥 Na prática:</strong> Agente completo em 20 linhas de código!</p>
            """),
            ("Tools e structured outputs", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li>Criar ferramentas com type hints automáticos</li>
                    <li>Validaçêo de inputs com Pydantic</li>
                    <li>Outputs estruturados garantidos (nêo mais parsing de JSON!)</li>
                    <li>Composiçêo de ferramentas complexas</li>
                </ul>
                <p><strong>⚡ Benefício:</strong> Elimina 90% dos erros de parsing e validaçêo.</p>
            """),
            ("Multi-model switching", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li>Usar GPT-4, Claude, Gemini com a mesma interface</li>
                    <li>Fallback automático se um modelo falha</li>
                    <li>Escolher modelo baseado em custo/latência/qualidade</li>
                    <li>A/B testing de diferentes modelos</li>
                </ul>
                <p><strong>💰 Economia:</strong> Use modelo mais barato para tarefas simples, modelo premium para complexas.</p>
            """),
            ("Deployment e boas práticas", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li>Estrutura de projeto profissional</li>
                    <li>Environment variables e secrets management</li>
                    <li>Logging e debugging</li>
                    <li>Testing de agentes</li>
                    <li>Deploy em produçêo (Docker, cloud)</li>
                </ul>
                <p><strong>🏗️ Arquitetura:</strong> Do protótipo ao sistema enterprise-ready.</p>
            """)
        ]
    },
    "modulo-05": {
        "file": "niveis/aplicacao.html",
        "topics": [
            ("Conceitos de Multi-Agent Systems (MAS)", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Por que múltiplos agentes?</strong> Especializaçêo, paralelismo, robustez</li>
                    <li><strong>Comunicaçêo:</strong> Como agentes trocam informações</li>
                    <li><strong>Coordenaçêo:</strong> Sincronizar ações de múltiplos agentes</li>
                    <li><strong>Exemplos reais:</strong> Agência de marketing, consultoria jurídica, dev team</li>
                </ul>
                <p><strong>🎯 Analogia:</strong> Como uma equipe humana, cada agente tem sua expertise.</p>
            """),
            ("Arquitetura CrewAI: Agents, Tasks, Tools", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Agents:</strong> Especialistas com role, goal, backstory</li>
                    <li><strong>Tasks:</strong> Unidades de trabalho com expected_output</li>
                    <li><strong>Tools:</strong> Ferramentas que agentes podem usar</li>
                    <li><strong>Crew:</strong> Orquestrador da equipe</li>
                    <li><strong>Process:</strong> Sequential vs Hierarchical</li>
                </ul>
                <p><strong>🏗️ Estrutura:</strong> Componentes modulares que se combinam para resolver problemas complexos.</p>
            """),
            ("Processos: Sequential vs Hierarchical", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Sequential:</strong> Tarefas executadas em ordem (A → B → C)</li>
                    <li><strong>Hierarchical:</strong> Manager agent coordena e delega</li>
                    <li><strong>Quando usar cada um:</strong> Trade-offs e casos de uso</li>
                    <li><strong>Custom workflows:</strong> Criar processos personalizados</li>
                </ul>
                <p><strong>⚙️ Escolha:</strong> Sequential para workflows simples, Hierarchical para complexidade.</p>
            """),
            ("Delegaçêo e colaboraçêo entre agentes", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>allow_delegation=True:</strong> Agentes podem pedir ajuda</li>
                    <li><strong>Context sharing:</strong> Passar informações entre agentes</li>
                    <li><strong>Feedback loops:</strong> Revisêo e melhoria iterativa</li>
                    <li><strong>Conflict resolution:</strong> Lidar com agentes que discordam</li>
                </ul>
                <p><strong>🤝 Colaboraçêo:</strong> Agentes trabalhando juntos sêo mais poderosos que sozinhos.</p>
            """),
            ("Casos de uso reais e padrões", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Content creation pipeline:</strong> Research → Write → Edit → SEO</li>
                    <li><strong>Data analysis team:</strong> Collect → Clean → Analyze → Report</li>
                    <li><strong>Customer support:</strong> Classify → Research → Respond → Escalate</li>
                    <li><strong>Software development:</strong> Plan → Code → Test → Deploy</li>
                </ul>
                <p><strong>💼 Aplicaçêo:</strong> Padrões reutilizáveis para diferentes domínios.</p>
            """)
        ]
    },
    "modulo-06": {
        "file": "niveis/aplicacao.html",
        "topics": [
            ("O que é MCP e por que é revolucionário", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>MCP:</strong> Protocolo aberto da Anthropic para conectar IA a dados</li>
                    <li><strong>Problema:</strong> Cada ferramenta tinha integraçêo custom</li>
                    <li><strong>Soluçêo:</strong> Interface padronizada para tudo</li>
                    <li><strong>Impacto:</strong> IA pode acessar qualquer sistema de forma consistente</li>
                </ul>
                <p><strong>🌐 Visêo:</strong> MCP para IA = HTTP para a web.</p>
            """),
            ("Arquitetura: Servers, Clients, Resources, Tools", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>MCP Server:</strong> Expõe dados e ferramentas via protocolo</li>
                    <li><strong>MCP Client:</strong> Aplicaçêo IA que consome servidores</li>
                    <li><strong>Resources:</strong> Dados que podem ser lidos (URIs)</li>
                    <li><strong>Tools:</strong> Ações que modificam estado</li>
                    <li><strong>Prompts:</strong> Templates reutilizáveis</li>
                </ul>
                <p><strong>🔌 Protocolo:</strong> JSON-RPC 2.0 para comunicaçêo cliente-servidor.</p>
            """),
            ("Criando servidores MCP customizados", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li>Implementar MCP Server do zero</li>
                    <li>Expor APIs, bancos de dados, arquivos via MCP</li>
                    <li>Definir schemas de resources e tools</li>
                    <li>Autenticaçêo e autorizaçêo</li>
                    <li>Deploy e hospedagem de servidores</li>
                </ul>
                <p><strong>🛠️ Poder:</strong> Conectar agentes a QUALQUER sistema que você imaginar!</p>
            """),
            ("Integrando MCP com agentes", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li>Conectar Claude Desktop a servidores MCP</li>
                    <li>Usar MCP com LangChain e CrewAI</li>
                    <li>Discovery de recursos disponíveis</li>
                    <li>Error handling e retry logic</li>
                    <li>Caching e performance</li>
                </ul>
                <p><strong>🔗 Integraçêo:</strong> Agentes com superpoderes via MCP.</p>
            """),
            ("Segurança, autenticaçêo e boas práticas", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Auth:</strong> API keys, OAuth, JWT</li>
                    <li><strong>Permissions:</strong> RBAC e scope control</li>
                    <li><strong>Rate limiting:</strong> Prevenir abuso</li>
                    <li><strong>Input validation:</strong> Sanitizaçêo de dados</li>
                    <li><strong>Audit logging:</strong> Rastreabilidade completa</li>
                </ul>
                <p><strong>🔒 Segurança:</strong> Produçêo-ready com todas as proteções necessárias.</p>
            """)
        ]
    },
    # ESTRATÉGICO
    "modulo-07": {
        "file": "niveis/estrategico.html",
        "topics": [
            ("Diferenças: Dev vs Staging vs Produçêo", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Dev:</strong> Tudo pode falhar, dados de teste</li>
                    <li><strong>Staging:</strong> Replica produçêo, testes finais</li>
                    <li><strong>Produçêo:</strong> 99.9%+ uptime, dados reais, monitoramento 24/7</li>
                    <li><strong>Deployment strategy:</strong> Blue-green, canary, rolling</li>
                </ul>
                <p><strong>⚠️ Realidade:</strong> Em produçêo, Murphy's Law aplica-se sempre!</p>
            """),
            ("Containerizaçêo: Docker para agentes IA", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li>Dockerfile otimizado para agentes Python</li>
                    <li>Multi-stage builds para imagens leves</li>
                    <li>Environment variables e secrets</li>
                    <li>Health checks e readiness probes</li>
                    <li>Docker Compose para stacks completas</li>
                </ul>
                <p><strong>📦 Benefício:</strong> "Funciona na minha máquina" → Funciona em QUALQUER máquina!</p>
            """),
            ("Deploy em Cloud: AWS, GCP, Azure", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>AWS:</strong> ECS, Lambda, EC2</li>
                    <li><strong>GCP:</strong> Cloud Run, GKE, Vertex AI</li>
                    <li><strong>Azure:</strong> Container Apps, AKS, Functions</li>
                    <li><strong>Trade-offs:</strong> Custo, latência, vendor lock-in</li>
                    <li><strong>Plataformas especializadas:</strong> Railway, Fly.io, Render</li>
                </ul>
                <p><strong>☁️ Escolha:</strong> Cloud certa para seu caso de uso e orçamento.</p>
            """),
            ("Monitoramento: Logs, métricas, alertas", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Logs:</strong> Structured logging (JSON), centralization</li>
                    <li><strong>Métricas:</strong> Latência (p50/p95/p99), RPS, error rate, custos</li>
                    <li><strong>Traces:</strong> Distributed tracing para debugging</li>
                    <li><strong>Dashboards:</strong> Grafana, DataDog, New Relic</li>
                    <li><strong>Alertas:</strong> PagerDuty, Slack, email quando algo quebra</li>
                </ul>
                <p><strong>📊 Observabilidade:</strong> Ver TUDO que acontece em produçêo.</p>
            """),
            ("Custos, segurança e CI/CD", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Custos:</strong> Monitorar tokens, compute, storage</li>
                    <li><strong>Otimizaçêo:</strong> Cache, modelos mais baratos para tarefas simples</li>
                    <li><strong>Segurança:</strong> HTTPS, secrets management, input validation</li>
                    <li><strong>CI/CD:</strong> GitHub Actions, GitLab CI, Jenkins</li>
                    <li><strong>Testing:</strong> Unit, integration, e2e tests antes de deploy</li>
                </ul>
                <p><strong>🚀 DevOps:</strong> Deploy confiável e automatizado.</p>
            """)
        ]
    },
    "modulo-08": {
        "file": "niveis/estrategico.html",
        "topics": [
            ("Frameworks: LangChain, CrewAI, AutoGen, LlamaIndex", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>LangChain:</strong> Ecossistema maduro, RAG excelente</li>
                    <li><strong>CrewAI:</strong> Multi-agentes simplificado</li>
                    <li><strong>AutoGen (Microsoft):</strong> Conversas complexas</li>
                    <li><strong>LlamaIndex:</strong> Especialista em indexaçêo e retrieval</li>
                    <li><strong>Semantic Kernel:</strong> Integraçêo Microsoft</li>
                </ul>
                <p><strong>🎯 Escolha:</strong> Framework certo para cada tipo de projeto.</p>
            """),
            ("Observabilidade: LangSmith, W&B, Helicone", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>LangSmith:</strong> Tracing de chains e agentes</li>
                    <li><strong>Weights & Biases:</strong> Experimentos e comparações</li>
                    <li><strong>Helicone:</strong> Monitoring de APIs de LLM</li>
                    <li><strong>Arize AI:</strong> Detecçêo de drift</li>
                </ul>
                <p><strong>🔍 Visibilidade:</strong> Entenda o que seus agentes estêo fazendo.</p>
            """),
            ("Vector Databases: Pinecone, Weaviate, Chroma, Qdrant", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Pinecone:</strong> Managed, escalável</li>
                    <li><strong>Weaviate:</strong> Open-source, GraphQL</li>
                    <li><strong>Chroma:</strong> Leve, ótimo para protótipos</li>
                    <li><strong>Qdrant:</strong> Performance alta</li>
                    <li><strong>pgvector:</strong> PostgreSQL extension</li>
                </ul>
                <p><strong>📊 Escolha:</strong> Vector DB certa para RAG eficaz.</p>
            """),
            ("Tendências: Agentes autônomos, multimodal, edge AI", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Long-running agents:</strong> Operam por dias/semanas</li>
                    <li><strong>Multimodal nativo:</strong> Texto + imagem + áudio + vídeo</li>
                    <li><strong>Edge AI:</strong> Modelos rodando localmente</li>
                    <li><strong>AI Regulation:</strong> EU AI Act, compliance</li>
                    <li><strong>Agentic Web:</strong> Sites projetados para agentes</li>
                </ul>
                <p><strong>🔮 Futuro:</strong> Para onde a tecnologia está caminhando.</p>
            """),
            ("Carreira e mercado de trabalho", """
                <p><strong>O que você aprenderá:</strong></p>
                <ul>
                    <li><strong>Perfis:</strong> AI Engineer, ML Engineer, Prompt Engineer</li>
                    <li><strong>Salários:</strong> Faixas por senioridade e regiêo</li>
                    <li><strong>Skills demandadas:</strong> O que empresas procuram</li>
                    <li><strong>Portfolio:</strong> Como montar projetos que impressionam</li>
                    <li><strong>Networking:</strong> Comunidades, eventos, contribuições open-source</li>
                </ul>
                <p><strong>💼 Próximos passos:</strong> Do curso para o mercado de trabalho.</p>
            """)
        ]
    }
}

print("Script para adicionar tópicos - rodaria aqui mas vou fazer manualmente")
print(f"Total de módulos configurados: {len(MODULOS_TOPICS)}")
