# 🚀 Configuraçêo do GitHub Pages

Este guia explica como configurar o GitHub Pages para hospedar a landing page do curso gratuitamente.

---

## 📋 Pré-requisitos

- Repositório criado no GitHub
- Arquivos da landing page commitados (`landing-page/`)
- Conta GitHub com permissões de admin no repositório

---

## ⚡ Setup Rápido (Modo Fácil)

### Passo 1: Configurar GitHub Pages

1. Vá para o repositório no GitHub
2. Clique em **Settings**
3. No menu lateral, clique em **Pages**
4. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/landing-page`
5. Clique em **Save**

### Passo 2: Aguardar Deploy

- O GitHub vai buildar e fazer deploy automaticamente
- Leva cerca de 1-2 minutos
- Você verá uma mensagem: "Your site is live at https://linnoff88-dev.github.io/

### Passo 3: Acessar o Site

Acesse: `https://linnoff88-dev.github.io/

**Pronto! Seu site está no ar! 🎉**

---

## 🔧 Configuraçêo Avançada (Opcional)

### Usando Domínio Personalizado

Se você quiser usar um domínio próprio (ex: `cursoagentes.com.br`):

#### 1. Configurar DNS

No seu provedor de domínio, adicione os seguintes registros:

**Registro A:**
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Registro CNAME:**
```
www  →  linnoff88-dev.github.io
```

#### 2. Configurar no GitHub

1. Em **Settings** > **Pages**
2. Em **Custom domain**, digite seu domínio
3. Clique em **Save**
4. Marque a opçêo **Enforce HTTPS**

Aguarde a verificaçêo do DNS (pode levar até 24h).

---

## 📁 Estrutura de Arquivos para GitHub Pages

```
FEA-IA/
├── landing-page/              # ← GitHub Pages serve daqui
│   ├── index.html            # Página principal
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   └── assets/               # (se tiver imagens, etc)
├── modulos/                  # Conteúdo do curso
├── README.md
└── ...
```

---

## 🎨 Personalizações

### Atualizar Links no HTML

Edite `landing-page/index.html` e atualize:

```html
<!-- Exemplo de atualizaçêo -->
<a href="https://github.com/linnoff88-dev/FEA-IA">
```

### Adicionar Google Analytics (Opcional)

```html
<!-- No <head> do index.html -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Adicionar Meta Tags para SEO

```html
<!-- No <head> do index.html -->
<meta property="og:title" content="Engenharia de Agentes de IA 2.0">
<meta property="og:description" content="Curso completo e gratuito de Engenharia de Agentes de IA">
<meta property="og:image" content="https://linnoff88-dev.github.io/
<meta property="og:url" content="https://linnoff88-dev.github.io/
<meta name="twitter:card" content="summary_large_image">
```

---

## 🔄 Atualizando o Site

Para atualizar o site:

1. Edite os arquivos em `landing-page/`
2. Commit e push para o GitHub:

```bash
git add landing-page/
git commit -m "update: melhorias na landing page"
git push origin main
```

3. GitHub Pages atualiza automaticamente em 1-2 minutos

---

## 🐛 Troubleshooting

### Problema: Site nêo carrega

**Soluçêo:**
- Verifique se a pasta está configurada corretamente em Settings > Pages
- Aguarde alguns minutos após o primeiro deploy
- Limpe o cache do navegador (Ctrl+Shift+R)

### Problema: CSS nêo está sendo aplicado

**Soluçêo:**
- Verifique os caminhos nos links CSS no `index.html`
- Use caminhos relativos: `css/styles.css` (nêo `/css/styles.css`)

```html
<!-- ✅ CORRETO -->
<link rel="stylesheet" href="css/styles.css">

<!-- ❌ ERRADO -->
<link rel="stylesheet" href="/css/styles.css">
```

### Problema: 404 Not Found

**Soluçêo:**
- Certifique-se que `index.html` existe em `landing-page/`
- Verifique se o branch correto está selecionado em Settings > Pages

### Problema: Deploy falhou

**Soluçêo:**
1. Vá em **Actions** no repositório
2. Veja o log de erro
3. Corrija o problema e faça novo commit

---

## ✅ Checklist Pós-Deploy

- [ ] Site está acessível
- [ ] Todos os links funcionam
- [ ] CSS está sendo aplicado
- [ ] JavaScript está funcionando
- [ ] Responsivo (teste em mobile)
- [ ] Sem erros no console do navegador
- [ ] Links para GitHub estêo corretos
- [ ] Meta tags configuradas

---

## 🎯 Próximos Passos

Após configurar GitHub Pages:

1. **Divulgue o link** nas redes sociais
2. **Adicione ao README** do projeto
3. **Configure analytics** para monitorar visitantes
4. **Otimize SEO** com meta tags apropriadas
5. **Adicione sitemap.xml** para melhorar indexaçêo

---

## 📚 Recursos Adicionais

- [Documentaçêo GitHub Pages](https://docs.github.com/pt/pages)
- [Configurar domínio personalizado](https://docs.github.com/pt/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Jekyll (gerador estático)](https://jekyllrb.com/)
- [Verificar status do deploy](https://github.com/linnoff88-dev/FEA-IA/deployments)

---

## 💡 Dicas Pro

### Cache Busting

Se você atualizar CSS/JS e usuários ainda veem versêo antiga, adicione versêo:

```html
<link rel="stylesheet" href="css/styles.css?v=1.1">
<script src="js/main.js?v=1.1"></script>
```

### Redirecionamentos

Crie um arquivo `_redirects` (para Netlify) ou configure no GitHub Pages:

```
/docs  /modulos  301
/curso /landing-page  301
```

### Performance

- Minifique CSS e JS antes do deploy
- Otimize imagens (use TinyPNG)
- Use lazy loading para imagens:

```html
<img src="image.jpg" loading="lazy" alt="Description">
```

---

<div align="center">

**🎉 Seu curso agora está online e acessível para todo mundo! 🎉**

[Ver Site](https://linnoff88-dev.github.io/ | [Ver Código](https://github.com/linnoff88-dev/FEA-IA)

</div>
