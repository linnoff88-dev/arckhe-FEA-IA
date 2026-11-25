# 🤝 Guia de Contribuiçêo

Obrigado por considerar contribuir com o projeto **Engenharia de Agentes de IA 2.0**! Este é um projeto da comunidade, para a comunidade, e toda ajuda é muito bem-vinda.

---

## 📋 Índice

- [Como Posso Contribuir?](#como-posso-contribuir)
- [Processo de Contribuiçêo](#processo-de-contribuiçêo)
- [Padrões e Boas Práticas](#padrões-e-boas-práticas)
- [Reportando Bugs](#reportando-bugs)
- [Sugerindo Melhorias](#sugerindo-melhorias)
- [Code of Conduct](#code-of-conduct)

---

## 🎯 Como Posso Contribuir?

Existem diversas formas de contribuir, independentemente do seu nível técnico:

### 1. 📝 Melhorar a Documentaçêo

- Corrigir erros de ortografia ou gramática
- Adicionar exemplos práticos
- Clarificar explicações confusas
- Traduzir conteúdo para outros idiomas
- Criar diagramas e ilustrações

### 2. 💻 Contribuir com Código

- Adicionar novos exemplos de código
- Melhorar projetos práticos existentes
- Criar novos projetos de demonstraçêo
- Otimizar código existente
- Adicionar testes

### 3. 🐛 Reportar Problemas

- Bugs no código
- Erros na documentaçêo
- Links quebrados
- Problemas de formataçêo

### 4. 💡 Sugerir Melhorias

- Novos casos de uso
- Ferramentas e bibliotecas relevantes
- Tópicos nêo cobertos
- Melhorias de estrutura

### 5. ⭐ Promover o Projeto

- Dar uma estrela no GitHub
- Compartilhar nas redes sociais
- Escrever artigos ou posts sobre o curso
- Recomendar para amigos e colegas

---

## 🔄 Processo de Contribuiçêo

### 1. Fork do Repositório

```bash
# Clone seu fork
git clone https://github.com/seu-usuario/FEA-IA.git

# Entre no diretório
cd FEA-IA

# Adicione o repositório original como upstream
git remote add upstream https://github.com/linnoff88-dev/FEA-IA.git
```

### 2. Crie uma Branch

Use nomes descritivos que expliquem a mudança:

```bash
# Para correções
git checkout -b fix/corrige-typo-modulo-3

# Para novos recursos
git checkout -b feat/adiciona-exemplo-langchain

# Para melhorias na documentaçêo
git checkout -b docs/melhora-readme-modulo-5
```

**Convençêo de nomes:**
- `feat/` - Novos recursos
- `fix/` - Correções
- `docs/` - Documentaçêo
- `refactor/` - Refatoraçêo de código
- `test/` - Adiçêo de testes
- `style/` - Formataçêo

### 3. Faça suas Mudanças

- Siga os padrões do projeto (veja abaixo)
- Teste suas alterações
- Commit com mensagens claras

```bash
# Adicione as mudanças
git add .

# Commit com mensagem descritiva
git commit -m "docs: adiciona exemplo de RAG no Módulo 3"
```

**Padrêo de commits:**

```
tipo(escopo): descriçêo curta

Descriçêo mais detalhada se necessário.

Resolves #123
```

**Tipos:**
- `feat`: Nova feature
- `fix`: Correçêo de bug
- `docs`: Documentaçêo
- `style`: Formataçêo
- `refactor`: Refatoraçêo de código
- `test`: Testes
- `chore`: Manutençêo

### 4. Push e Pull Request

```bash
# Push para seu fork
git push origin sua-branch

# Crie o Pull Request no GitHub
```

**No Pull Request, inclua:**
- Descriçêo clara do que foi alterado
- Por que a mudança é necessária
- Screenshots se aplicável
- Referência a issues relacionadas

---

## 📏 Padrões e Boas Práticas

### Documentaçêo (Markdown)

#### Estrutura de Arquivos

```markdown
# Título Principal (H1)

## Seçêo (H2)

### Subseçêo (H3)

Texto do conteúdo...

```python
# Código Python com syntax highlighting
def exemplo():
    pass
```

**Dica:** Sempre com espaço em branco antes do código para melhor legibilidade.
```

#### Formataçêo

- Use **negrito** para ênfase importante
- Use *itálico* para ênfase leve
- Use `código inline` para nomes de variáveis, funções, etc.
- Use listas numeradas para passos sequenciais
- Use listas com marcadores para itens nêo ordenados

#### Links

```markdown
# Interno (mesmo repositório)
[Veja o Módulo 3](modulos/modulo-03/conteudo/Modulo-03-LangChain.md)

# Externo
[LangChain Docs](https://python.langchain.com/)
```

### Código Python

#### Style Guide

Seguimos o [PEP 8](https://pep8.org/):

```python
# ✅ BOM
def calculate_embedding(text: str, model: str = "text-embedding-3-small") -> list[float]:
    """
    Calcula o embedding de um texto.

    Args:
        text: Texto para gerar embedding
        model: Modelo a ser usado

    Returns:
        Lista de floats representando o embedding
    """
    # Implementaçêo
    pass


# ❌ RUIM
def calc_emb(t,m="text-embedding-3-small"):
    # sem docstring, nomes nêo descritivos
    pass
```

#### Comentários

```python
# Comentários explicam O POR QUÊ, nêo o O QUÊ

# ✅ BOM
# Usar temperature=0 para garantir respostas determinísticas
agent = Agent(model="claude-3-7-sonnet-20250219", temperature=0)

# ❌ RUIM
# Criar agente com temperature 0
agent = Agent(model="claude-3-7-sonnet-20250219", temperature=0)
```

#### Exemplos Completos

Todo exemplo de código deve ser **executável**:

```python
# ✅ BOM - código completo e executável
from agno import Agent
import os

# Configuraçêo
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Criar agente
agent = Agent(
    name="Exemplo",
    model="claude-3-7-sonnet-20250219",
    api_key=ANTHROPIC_API_KEY
)

# Executar
response = agent.run("Olá!")
print(response)


# ❌ RUIM - código incompleto
agent = Agent(...)
response = agent.run("Olá!")
```

### Projetos Práticos

Cada projeto prático deve incluir:

1. **README.md** com:
   - Descriçêo do projeto
   - Pré-requisitos
   - Instalaçêo
   - Como executar
   - Estrutura de arquivos
   - Próximos passos

2. **requirements.txt** com dependências pinadas:

```
agno==0.1.0
anthropic==0.18.0
python-dotenv==1.0.0
```

3. **.env.example** com variáveis necessárias:

```bash
ANTHROPIC_API_KEY=sua-chave-aqui
DATABASE_URL=sqlite:///app.db
```

4. Código bem documentado e modular

---

## 🐛 Reportando Bugs

Antes de reportar um bug, verifique se já nêo existe uma [issue aberta](https://github.com/linnoff88-dev/FEA-IA/issues) sobre o mesmo problema.

### Template de Bug Report

```markdown
**Descriçêo do Bug**
Descriçêo clara e concisa do bug.

**Como Reproduzir**
Passos para reproduzir o comportamento:
1. Vá para '...'
2. Execute '....'
3. Veja o erro

**Comportamento Esperado**
O que deveria acontecer.

**Screenshots**
Se aplicável, adicione screenshots.

**Ambiente:**
 - OS: [ex: Windows 11]
 - Python: [ex: 3.11]
 - Versêo do projeto: [ex: commit abc123]

**Contexto Adicional**
Qualquer outra informaçêo relevante.
```

---

## 💡 Sugerindo Melhorias

### Template de Feature Request

```markdown
**Problema Relacionado**
Descreva o problema que esta feature resolveria.

**Soluçêo Proposta**
Descriçêo clara da soluçêo que você gostaria de ver.

**Alternativas Consideradas**
Outras soluções que você considerou.

**Contexto Adicional**
Screenshots, mockups, links relevantes, etc.
```

---

## 📐 Revisêo de Pull Requests

Quando você submeter um PR:

1. **Seja paciente** - Revisões levam tempo
2. **Responda a comentários** - Esteja aberto a sugestões
3. **Mantenha o PR focado** - Um PR = Uma mudança/feature
4. **Atualize se necessário** - Pode ser pedido mudanças

### O que os revisores vêo verificar:

- ✅ O código funciona?
- ✅ Segue os padrões do projeto?
- ✅ A documentaçêo foi atualizada?
- ✅ Os exemplos sêo claros?
- ✅ Nêo quebra funcionalidades existentes?

---

## 🎨 Design e Estilo Visual

### Emojis no Markdown

Use emojis para melhorar a legibilidade:

```markdown
✅ Tarefa completa
⚠️ Atençêo
📝 Nota importante
💡 Dica
🔥 Destaque
🚀 Novo recurso
```

### Callouts

Use blockquotes para destacar informações:

```markdown
> **💡 Dica:** Use temperature=0 para respostas mais consistentes.

> **⚠️ Atençêo:** Esta operaçêo pode ser custosa.

> **✅ Melhor Prática:** Sempre valide as entradas do usuário.
```

---

## ⚖️ Code of Conduct

Este projeto segue nosso [Código de Conduta](CODE_OF_CONDUCT.md). Ao participar, você concorda em mantê-lo.

**Resumo:**
- Seja respeitoso e profissional
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade
- Mostre empatia com outros membros

---

## ❓ Perguntas?

Se tiver dúvidas sobre como contribuir:

- 💬 Abra uma [Discussion](https://github.com/linnoff88-dev/FEA-IA/discussions)
- 📧 Envie um email para linnoff88-dev@gmail.com
- 🐛 Crie uma [Issue](https://github.com/linnoff88-dev/FEA-IA/issues) com a tag `question`

---

## 🙏 Agradecimentos

Todo contribuidor é adicionado automaticamente à nossa [lista de contribuidores](https://github.com/linnoff88-dev/FEA-IA/graphs/contributors).

**Obrigado por fazer parte desta comunidade! 🎉**

---

<div align="center">

### 🌟 Nêo esqueça de dar uma estrela no projeto!

[![Star History Chart](https://api.star-history.com/svg?repos=linnoff88-dev/FEA-IA&type=Date)](https://star-history.com/#linnoff88-dev/FEA-IA&Date)

</div>
