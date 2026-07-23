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
| [doiInSummary](https://github.com/OJSBR/doiInSummary) | generic | Shows the article DOI in the issue summary and journal home page | 3.4 · 3.5 |
| [ojsbrFilenameRename](https://github.com/OJSBR/ojsbrFilenameRename) | generic | Renames the file delivered on download (configurable pattern) | 3.4 · 3.5 |
| [orcidManualEntry](https://github.com/OJSBR/orcidManualEntry) | generic | Restores a manual ORCID field when ORCID OAuth is not configured (authenticated ORCID stays recommended) | 3.5 |
| [reviewerRecommendationManager](https://github.com/OJSBR/reviewerRecommendationManager) | generic | Rename (multilingual), reorder and disable reviewer recommendations without patching core, preserving review history | 3.4 · 3.5 |
| [reviewerDirectory](https://github.com/OJSBR/reviewerDirectory) | generic | Editor-only directory of reviewers (profiles + review stats, active-submission IDs, configurable columns, Excel export) and a period/issue reviewer roster (nominata) | 3.5 |
| [ojsbr-webhook](https://github.com/OJSBR/ojsbr-webhook) | generic | Sends HTTP webhooks when submissions are created and articles published | 3.4 |
| [accessibility](https://github.com/OJSBR/accessibility) | block | Sidebar accessibility controls for readers: zoom in/out, high-contrast toggle and reset (preferences persist across pages) | 3.3 · 3.4 · 3.5 |
| [languageToggleByFlag](https://github.com/OJSBR/languageToggleByFlag) | block | Sidebar language switcher with country flags (also works on OMP/OPS); adapted for 3.5 by OJSBR, original by Lepidus Tecnologia | 3.5 |
| [vlibras](https://github.com/OJSBR/vlibras) | block | Embeds the VLibras widget (the Brazilian government's Portuguese→Libras sign-language translator) with its floating avatar | 3.3 · 3.4 · 3.5 |
| [pln](https://github.com/OJSBR/pln) | generic | PKP Preservation Network (PLN / PKP PN) — unofficial OJS 3.5 build (based on pkp/pln#117), maintained until the official release | 3.5 |

### OMP (Open Monograph Press)

| Plugin | Type | What it does | Versions |
|--------|------|--------------|----------|
| [customMetadata](https://github.com/OJSBR/customMetadata) | generic | Configurable extra metadata fields on the publication Metadata tab | 3.4 · 3.5 |
| [crossref](https://github.com/OJSBR/crossref) | generic | Crossref DOI registration/export for monographs and chapters (fills a gap OMP core lacks) | 3.4 · 3.5 |
| [assignEditorGeneral](https://github.com/OJSBR/assignEditorGeneral) | generic | Automatically assigns all active General Editors to each new submission | 3.5 |

## Installing a plugin

1. Open the plugin's repository and go to **Releases**; download the `.tar.gz` matching your
   OJS/OMP version.
2. In your site: **Settings → Website → Plugins → Upload A New Plugin**, upload the package,
   then enable the plugin.
3. Alternatively, clone the branch matching your version straight into `plugins/generic/`
   (or `plugins/blocks/` for block plugins).

Each repository's README has full installation, configuration and credits.

## Downloads

Direct installable packages (`.tar.gz`). Pick the one matching your OJS/OMP version and
upload it via **Settings → Website → Plugins → Upload A New Plugin**.

| Plugin | Software | OJS/OMP 3.5 | OJS/OMP 3.4 | OJS 3.3 |
|--------|----------|-------------|-------------|---------|
| viewcounter | OJS | [⬇ 1.2.0.0](https://github.com/OJSBR/viewcounter/releases/download/1.2.0.0/viewcounter-1.2.0.0.tar.gz) | [⬇ 1.1.0.0](https://github.com/OJSBR/viewcounter/releases/download/1.1.0.0/viewcounter-1.1.0.0.tar.gz) | — |
| mostRead | OJS | [⬇ 3.5.0.1](https://github.com/OJSBR/mostRead/releases/download/3.5.0.1/mostRead-3.5.0.1.tar.gz) | [⬇ 3.4.0.1](https://github.com/OJSBR/mostRead/releases/download/3.4.0.1/mostRead-3.4.0.1.tar.gz) | — |
| whatsAppContributor | OJS | [⬇ 1.1.0.0](https://github.com/OJSBR/whatsAppContributor/releases/download/1.1.0.0/whatsAppContributor-1.1.0.0.tar.gz) | [⬇ 1.0.0.0](https://github.com/OJSBR/whatsAppContributor/releases/download/1.0.0.0/whatsAppContributor-1.0.0.0.tar.gz) | — |
| doiInSummary | OJS | [⬇ 3.5.0.1](https://github.com/OJSBR/doiInSummary/releases/download/3.5.0.1/doiInSummary-3.5.0.1.tar.gz) | [⬇ 3.4.0.1](https://github.com/OJSBR/doiInSummary/releases/download/3.4.0.1/doiInSummary-3.4.0.1.tar.gz) | — |
| ojsbrFilenameRename | OJS | [⬇ 1.1.0.0](https://github.com/OJSBR/ojsbrFilenameRename/releases/download/1.1.0.0-ojs3.5/ojsbrFilenameRename-1.1.0.0-ojs3.5.tar.gz) | [⬇ 1.1.0.0](https://github.com/OJSBR/ojsbrFilenameRename/releases/download/1.1.0.0-ojs3.4/ojsbrFilenameRename-1.1.0.0-ojs3.4.tar.gz) | — |
| orcidManualEntry | OJS | [⬇ 1.0.0.0](https://github.com/OJSBR/orcidManualEntry/releases/download/1.0.0.0/orcidManualEntry-1.0.0.0.tar.gz) | — | — |
| reviewerRecommendationManager | OJS | [⬇ 1.0.3.0](https://github.com/OJSBR/reviewerRecommendationManager/releases/download/1.0.3.0/reviewerRecommendationManager-1.0.3.0.tar.gz) | [⬇ 1.0.3.0-ojs3.4](https://github.com/OJSBR/reviewerRecommendationManager/releases/download/1.0.3.0-ojs3.4/reviewerRecommendationManager-1.0.3.0-ojs3.4.tar.gz) | — |
| accessibility | OJS | [⬇ 1.0.1.0](https://github.com/OJSBR/accessibility/releases/download/1.0.1.0/accessibility-1.0.1.0.tar.gz) | [⬇ 1.0.0.0-ojs3.4](https://github.com/OJSBR/accessibility/releases/download/1.0.0.0-ojs3.4/accessibility-1.0.0.0-ojs3.4.tar.gz) | [⬇ 1.0.0.0-ojs3.3](https://github.com/OJSBR/accessibility/releases/download/1.0.0.0-ojs3.3/accessibility-1.0.0.0-ojs3.3.tar.gz) |
| vlibras | OJS | [⬇ 1.0.0.0](https://github.com/OJSBR/vlibras/releases/download/1.0.0.0/vlibras-1.0.0.0.tar.gz) | [⬇ 1.0.0.0-ojs3.4](https://github.com/OJSBR/vlibras/releases/download/1.0.0.0-ojs3.4/vlibras-1.0.0.0-ojs3.4.tar.gz) | [⬇ 1.0.0.0-ojs3.3](https://github.com/OJSBR/vlibras/releases/download/1.0.0.0-ojs3.3/vlibras-1.0.0.0-ojs3.3.tar.gz) |
| reviewerDirectory | OJS | [⬇ 1.0.0.0](https://github.com/OJSBR/reviewerDirectory/releases/download/1.0.0.0/reviewerDirectory-1.0.0.0.tar.gz) | — | — |
| languageToggleByFlag | OJS | [⬇ 3.5.0.2](https://github.com/OJSBR/languageToggleByFlag/releases/download/3.5.0.2/languageToggleByFlag-3.5.0.2.tar.gz) | — | — |
| pln | OJS | [⬇ 4.0.0.0](https://github.com/OJSBR/pln/releases/download/4.0.0.0-ojs3.5/pln-4.0.0.0-ojs3.5.tar.gz) | — | — |
| ojsbr-webhook | OJS | — | [⬇ 3.4.build.11](https://github.com/OJSBR/ojsbr-webhook/releases/download/3.4.build.11/ojsbrWebhook-3.4.build.11.tar.gz) | — |
| customMetadata | OMP | [⬇ 1.0.0.0](https://github.com/OJSBR/customMetadata/releases/download/1.0.0.0-omp3.5/customMetadata-1.0.0.0-omp3.5.tar.gz) | [⬇ 1.0.0.0](https://github.com/OJSBR/customMetadata/releases/download/1.0.0.0-omp3.4/customMetadata-1.0.0.0-omp3.4.tar.gz) | — |
| crossref | OMP | [⬇ 1.0.0.0](https://github.com/OJSBR/crossref/releases/download/1.0.0.0-omp3.5/crossref-1.0.0.0-omp3.5.tar.gz) | [⬇ 1.0.0.0](https://github.com/OJSBR/crossref/releases/download/1.0.0.0-omp3.4/crossref-1.0.0.0-omp3.4.tar.gz) | — |
| assignEditorGeneral | OMP | [⬇ 1.0.0.0](https://github.com/OJSBR/assignEditorGeneral/releases/download/1.0.0.0-omp3.5/assignEditorGeneral-1.0.0.0-omp3.5.tar.gz) | — | — |

> The **latest** package of each plugin is always on its repository's *Releases* page.

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

Links diretos de download de cada versão estão na tabela **[Downloads](#downloads)** acima.
Cada repositório traz README completo com instalação, configuração e créditos.

### Créditos

Alguns plugins foram reescritos ou adaptados pela OJSBR a partir de trabalhos anteriores da
comunidade; os autores originais são creditados na seção **Créditos e autoria** de cada
repositório. Entre os trabalhos originais em que nos baseamos estão os de **Antti-Jussi
Nygård (@ajnyga)**, **@zielaq**, **Lepidus Tecnologia**, **STI-FFLCH/USP**, **ABCD/USP** e
**PKP**.

### Licença

Todos os plugins da OJSBR são distribuídos sob a **GNU GPL v3**.
