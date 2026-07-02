# OJSBR Plugins

Open-source plugins for **PKP** software — **OJS** (Open Journal Systems) and **OMP** (Open
Monograph Press) — developed and maintained by **[OJSBR](https://ojsbr.com.br)**.

Everything here is released under the **GNU GPL v3**, so the whole PKP community can use,
adapt and contribute. Each plugin lives in its own repository, with one branch per supported
PKP version (`stable-3_5_0`, `stable-3_4_0`, …) and installable packages under **Releases**.

## Catalog

### OJS (Open Journal Systems)

| Plugin | Type | What it does | Versions |
|--------|------|--------------|----------|
| [viewcounter](https://github.com/OJSBR/viewcounter) | generic | Shows each article's abstract views and downloads on summaries and article pages | 3.4 · 3.5 |
| [mostRead](https://github.com/OJSBR/mostRead) | block | Sidebar block with the most-read articles of a time window | 3.4 · 3.5 |
| [whatsAppContributor](https://github.com/OJSBR/whatsAppContributor) | generic | Adds a Phone/WhatsApp (E.164) field to the contributor form | 3.4 · 3.5 |
| [doiInSummary](https://github.com/OJSBR/doiInSummary) | generic | Shows the article DOI in the issue summary and journal home page | 3.5 |
| [ojsbrFilenameRename](https://github.com/OJSBR/ojsbrFilenameRename) | generic | Renames the file delivered on download (configurable pattern) | 3.4 · 3.5 · *(publishing soon)* |

### OMP (Open Monograph Press)

| Plugin | Type | What it does | Versions |
|--------|------|--------------|----------|
| [customMetadata](https://github.com/OJSBR/customMetadata) | generic | Configurable extra metadata fields on the publication Metadata tab | 3.4 |
| [crossref](https://github.com/OJSBR/crossref) | generic | Crossref DOI registration/export for monographs and chapters (fills a gap OMP core lacks) | 3.5 |

## Installing a plugin

1. Open the plugin's repository and go to **Releases**; download the `.tar.gz` matching your
   OJS/OMP version.
2. In your site: **Settings → Website → Plugins → Upload A New Plugin**, upload the package,
   then enable the plugin.
3. Alternatively, clone the branch matching your version straight into `plugins/generic/`
   (or `plugins/blocks/` for block plugins).

Each repository's README has full installation, configuration and credits.

## Credits

Some plugins were rewritten or adapted by OJSBR from earlier community work; upstream authors
are credited in each repository's **Credits & authorship** section. Original authors we build
on include **Antti-Jussi Nygård (@ajnyga)**, **@zielaq**, **Lepidus Tecnologia**,
**STI-FFLCH/USP**, **ABCD/USP** and **PKP**.

## Contributing

Contributions are welcome in each plugin's repository — see its `CONTRIBUTING.md` and
`CODE_OF_CONDUCT.md`. Please target the branch matching the PKP version you are working on.

## License

All OJSBR plugins are distributed under the **GNU GPL v3**.

---

## 🇧🇷 Português

Plugins de código aberto para os softwares da **PKP** — **OJS** (Open Journal Systems) e
**OMP** (Open Monograph Press) — desenvolvidos e mantidos pela **[OJSBR](https://ojsbr.com.br)**.

Tudo aqui é distribuído sob a **GNU GPL v3**, para que toda a comunidade PKP possa usar,
adaptar e contribuir. Cada plugin fica em seu próprio repositório, com uma branch por versão
suportada do PKP (`stable-3_5_0`, `stable-3_4_0`, …) e pacotes instaláveis em **Releases**.

### Como instalar

1. Abra o repositório do plugin, vá em **Releases** e baixe o `.tar.gz` da sua versão do
   OJS/OMP.
2. No seu site: **Configurações → Website → Plugins → Enviar um novo plugin**, envie o pacote
   e ative o plugin.
3. Como alternativa, clone a branch da sua versão direto em `plugins/generic/` (ou
   `plugins/blocks/` para plugins de bloco).

Cada repositório traz README completo com instalação, configuração e créditos.

### Créditos

Alguns plugins foram reescritos ou adaptados pela OJSBR a partir de trabalhos anteriores da
comunidade; os autores originais são creditados na seção **Créditos e autoria** de cada
repositório. Entre os trabalhos originais em que nos baseamos estão os de **Antti-Jussi
Nygård (@ajnyga)**, **@zielaq**, **Lepidus Tecnologia**, **STI-FFLCH/USP**, **ABCD/USP** e
**PKP**.

### Licença

Todos os plugins da OJSBR são distribuídos sob a **GNU GPL v3**.
