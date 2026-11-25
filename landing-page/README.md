# Landing Page - Engenharia de Agentes de IA 2.0

Landing page responsiva e moderna para o curso de Engenharia de Agentes de IA.

## 🚀 URL ao Vivo

**Site:** https://linnoff88-dev.github.io/

---

## 📁 Estrutura

```
landing-page/
├── index.html          # Página principal
├── css/
│   └── styles.css     # Estilos CSS completos
├── js/
│   └── main.js        # JavaScript para interatividade
├── assets/            # (futuro) Imagens e recursos
├── sitemap.xml        # Mapa do site para SEO
├── robots.txt         # Configuraçêo para crawlers
└── README.md          # Este arquivo
```

---

## 🎨 Características

### Design
- ✅ **Responsivo** - Mobile-first design
- ✅ **Moderno** - Gradientes, glassmorphism, animações
- ✅ **Performance** - CSS otimizado, lazy loading
- ✅ **Acessível** - Semântica HTML5, boas práticas

### Funcionalidades
- ✅ Navegaçêo mobile com menu hamburger
- ✅ Scroll suave entre seções
- ✅ Animações ao scroll (Intersection Observer)
- ✅ Contadores animados nas estatísticas
- ✅ Efeito de digitaçêo no código de exemplo
- ✅ Cards de módulos interativos

### SEO
- ✅ Meta tags completas (Open Graph, Twitter)
- ✅ Sitemap.xml
- ✅ Robots.txt
- ✅ URLs canônicas
- ✅ Estrutura semântica

---

## 🛠️ Tecnologias

- **HTML5** - Estrutura semântica
- **CSS3** - Design moderno com custom properties
- **JavaScript (Vanilla)** - Sem dependências
- **Google Fonts** - Inter e Space Grotesk

---

## 🚀 Deploy

Esta landing page está configurada para GitHub Pages.

### Pré-requisitos
- Repositório no GitHub
- GitHub Pages habilitado

### Configuraçêo

1. **Settings > Pages**
   - Source: Branch `main`
   - Folder: `/landing-page`
   - Save

2. **Aguardar Deploy**
   - ~1-2 minutos
   - Verificar em Actions

3. **Acessar**
   - https://linnoff88-dev.github.io/

Ver guia completo: [GITHUB-PAGES-SETUP.md](../GITHUB-PAGES-SETUP.md)

---

## 🎨 Customizaçêo

### Cores

As cores sêo definidas via CSS custom properties em `css/styles.css`:

```css
:root {
    --primary: #00D9FF;      /* Ciano vibrante */
    --secondary: #8B5CF6;    /* Roxo */
    --dark: #1A1F3A;         /* Azul escuro */
    --text: #E5E7EB;         /* Texto claro */
    /* ... */
}
```

### Conteúdo

Edite `index.html` para atualizar:
- Textos e descrições
- Links para módulos
- Estatísticas
- CTAs

### Estilos

Edite `css/styles.css`:
- Layout e grid
- Animações
- Responsividade
- Temas

### Interatividade

Edite `js/main.js`:
- Navegaçêo
- Animações
- Eventos
- Contadores

---

## 📱 Responsividade

Breakpoints:

```css
/* Mobile: < 768px */
/* Tablet: 768px - 1024px */
/* Desktop: > 1024px */
```

Testado em:
- ✅ Chrome, Firefox, Safari, Edge
- ✅ iOS Safari, Chrome Mobile
- ✅ Resoluções 320px - 2560px

---

## ⚡ Performance

### Otimizações Aplicadas

- ✅ CSS minificado (pode ser melhorado)
- ✅ Lazy loading de animações
- ✅ Preconnect para Google Fonts
- ✅ Uso de Intersection Observer
- ✅ Sem dependências externas pesadas

### Próximas Otimizações

- [ ] Minificar CSS e JS
- [ ] Otimizar e adicionar imagens WebP
- [ ] Service Worker para cache
- [ ] Critical CSS inline

---

## 📊 Analytics (Opcional)

Para adicionar Google Analytics, edite `index.html` e adicione no `<head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## 🐛 Troubleshooting

### CSS nêo carrega
- Verifique paths: `css/styles.css` (relativo)
- Limpe cache do navegador (Ctrl+Shift+R)

### JavaScript nêo funciona
- Verifique console do navegador (F12)
- Confirme que `js/main.js` existe

### 404 no GitHub Pages
- Confirme que `index.html` está na pasta `/landing-page`
- Verifique configuraçêo em Settings > Pages

---

## 📄 Licença

MIT License - Ver [LICENSE](../LICENSE)

---

## 🤝 Contribuindo

Contribuições sêo bem-vindas! Ver [CONTRIBUTING.md](../CONTRIBUTING.md)

**Tipos de contribuições:**
- 🐛 Correções de bugs
- 🎨 Melhorias de design
- ⚡ Otimizações de performance
- 📱 Melhorias de responsividade
- ♿ Melhorias de acessibilidade

---

## 📞 Contato

- **GitHub**: https://github.com/linnoff88-dev/FEA-IA
- **Issues**: https://github.com/linnoff88-dev/FEA-IA/issues
- **Email**: linnoff88-dev@gmail.com

---

<div align="center">

**Feito com ❤️ para a comunidade de IA**

[Ver Site](https://linnoff88-dev.github.io/ | [Ver Código](https://github.com/linnoff88-dev/FEA-IA)

</div>
