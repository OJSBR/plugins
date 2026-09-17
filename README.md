# OJSBR Plugins

Open-source plugins for **PKP** software — **OJS** (Open Journal Systems) and **OMP** (Open
Monograph Press) — developed and maintained by **[OJSBR](https://ojsbr.com.br)**.

Everything here is released under the **GNU GPL v3**, so the whole PKP community can use,
adapt and contribute. Each plugin lives in its own repository, with one branch per supported
PKP version (`stable-3_5_0`, `stable-3_4_0`, …) and installable packages under **Releases**.

## Catalog

The **Applications** column says which PKP applications each plugin runs on. The
sections below group them by the application they were written for; a plugin that also
runs elsewhere says so in that column.


### OJS (Open Journal Systems)

| Plugin | Applications | Type | What it does | PKP versions |
|--------|--------------|------|--------------|--------------|
| [viewcounter](https://github.com/OJSBR/viewcounter) | OJS | generic | Shows each article's abstract views and downloads on summaries and article pages | 3.4 · 3.5 |
| [mostRead](https://github.com/OJSBR/mostRead) | OJS · OMP | block | Sidebar block with the most-read articles or books of a time window | 3.4 · 3.5 |
| [whatsAppContributor](https://github.com/OJSBR/whatsAppContributor) | OJS | generic | Adds a Phone/WhatsApp (E.164) field to the contributor form and, optionally, to user registration; carries the submitter's phone to their authorship | 3.4 · 3.5 |
| [doiInSummary](https://github.com/OJSBR/doiInSummary) | OJS | generic | Shows the article DOI in the issue summary and journal home page | 3.4 · 3.5 |
| [ojsbrFilenameRename](https://github.com/OJSBR/ojsbrFilenameRename) | OJS · OMP | generic | Delivers submission files under a neutral, standardized name on download, translated into the language of the reader or of the journal (38 languages), or as numbers only | 3.4 · 3.5 |
| [orcidManualEntry](https://github.com/OJSBR/orcidManualEntry) | OJS · OMP | generic | Restores a manual ORCID field (contributor form, user registration and profile) when ORCID OAuth is not configured (authenticated ORCID stays recommended) | 3.5 |
| [requiredAuthorMetadata](https://github.com/OJSBR/requiredAuthorMetadata) | OJS · OMP | generic | Lets the journal require the family name, the affiliation and the biography of every contributor of a submission, each one on its own, and refuse to complete the submission while any of them is missing; journal managers and section editors can be exempt | 3.5 |
| [reviewerRecommendationManager](https://github.com/OJSBR/reviewerRecommendationManager) | OJS | generic | Rename (multilingual), reorder and disable reviewer recommendations without patching core, preserving review history | 3.4 · 3.5 |
| [blindReviewGuard](https://github.com/OJSBR/blindReviewGuard) | OJS | generic | Checks the files a reviewer is about to receive for anything that identifies the authors (document properties, tracked changes, comments, text, file name) and can remove the identifying metadata | 3.5 |
| [coauthorAlert](https://github.com/OJSBR/coauthorAlert) | OJS | generic | Warns authors of supervised work, on the contributors and review steps of the submission wizard, to add their supervisor as a co-author while the author list can still change (and so the supervisor is never invited to review the work), with a live single-author indicator and an acknowledgement required before submitting; every text configurable per language | 3.5 |
| [coAuthorParticipants](https://github.com/OJSBR/coAuthorParticipants) | OJS | generic | Turns the co-authors listed in a submission's contributors into users taking part in its editorial workflow as authors: finds the account by email or creates it, enrols it in the author group, assigns it to the submission and sends an individual email; automatic on new submissions and contributors added later, plus a command line backfill for submissions still in the workflow | 3.5 |
| [staticEditorialTeam](https://github.com/OJSBR/staticEditorialTeam) | OJS · OMP | generic | Brings back the static Editorial Team page: shows the free-text setting of the journal or press instead of the dynamic masthead listing introduced in 3.5 | 3.5 |
| [classicUserEditor](https://github.com/OJSBR/classicUserEditor) | OJS · OMP | generic | Restores direct editing of users (given name, family name, email and roles) for managers and administrators, alongside the 3.5 invitation manager | 3.5 |
| [ojsbrUserRoleFilter](https://github.com/OJSBR/ojsbrUserRoleFilter) | OJS · OMP | generic | Brings the role filter back to the Users & Roles screen, filtering by user group on the server | 3.5 |
| [authorContributorEditor](https://github.com/OJSBR/authorContributorEditor) | OJS | generic | Gives authors back the editing of the contributor list of their own submissions when their user group is allowed to edit submission metadata, as in 3.3/3.4 | 3.5 |
| [reviewerDirectory](https://github.com/OJSBR/reviewerDirectory) | OJS · OMP | generic | Editor-only directory of reviewers (profiles + review stats, active-submission IDs, configurable columns, Excel export) and a period/issue reviewer roster (nominata) | 3.5 |
| [controlledVocabSplitter](https://github.com/OJSBR/controlledVocabSplitter) | OJS · OMP | generic | Splits keywords, subjects, disciplines and supporting agencies pasted as a single line into separate terms whenever a publication is saved or imported (semicolon, comma or period; keeps legal references and species initials whole) | 3.5 |
| [crossrefConference](https://github.com/OJSBR/crossrefConference) | OJS | generic | Deposits DOIs with Crossref as conference proceedings (`<conference>`/`<conference_paper>`) instead of journal records, as a DOI registration agency: event name, edition number, dates and location, and the proceedings DOI the papers hang off | 3.5 |
| [articleMetricsBadges](https://github.com/OJSBR/articleMetricsBadges) | OJS | generic | Article-level metric badges from PlumX, Dimensions and Altmetric, each provider and each position (article page, sidebar block) switchable on its own; renders only on articles with a DOI, every provider disabled by default with its terms of use documented | 3.3 · 3.4 · 3.5 |
| [epubJsViewer](https://github.com/OJSBR/epubJsViewer) | OJS · OPS · OMP | generic | Embedded EPUB galley reader with zoom, table of contents and reading modes, powered by epub.js; continues the `epubViewer` by Lepidus Tecnologia, discontinued in 2025 when its Bibi reading engine stopped being maintained, and never released for 3.5 | 3.5 |
| [ojsbrWebhook](https://github.com/OJSBR/ojsbrWebhook) | OJS | generic | Sends HTTP webhooks when submissions are created and articles published | 3.4 |
| [ojsbrServices](https://github.com/OJSBR/ojsbrServices) | OJS | generic | Creates and follows OJSBR service orders (JATS XML markup) from the journal, against the OJSBR connector | 3.5 |
| [accessibility](https://github.com/OJSBR/accessibility) | OJS · OMP | block | Sidebar accessibility controls for readers: zoom in/out, high-contrast toggle and reset (preferences persist across pages) | 3.3 · 3.4 · 3.5 |
| [languageToggleByFlag](https://github.com/OJSBR/languageToggleByFlag) | OJS · OPS · OMP | block | Sidebar language switcher with country flags (also works on OMP/OPS); adapted for 3.5 by OJSBR, original by Lepidus Tecnologia | 3.5 |
| [vlibras](https://github.com/OJSBR/vlibras) | OJS · OMP | block | Embeds the VLibras widget (the Brazilian government's Portuguese→Libras sign-language translator) with its floating avatar | 3.3 · 3.4 · 3.5 |
| [keywordCloudClassicBeautiful](https://github.com/OJSBR/keywordCloudClassicBeautiful) | OJS · OMP | block | Packed sidebar keyword cloud sized and coloured by frequency (the classic behaviour restored); self-contained, no CDN; original keywordCloud by PKP/SFU, maintained by Lepidus Tecnologia | 3.4 · 3.5 |
| [recommendByAuthor](https://github.com/OJSBR/recommendByAuthor) | OJS | generic | Original recommendByAuthor by PKP/SFU, rewritten by OJSBR: the "articles by the same author" list is materialised by a scheduled task and read from a table, instead of scanning author_settings once per author on every article view (11.9 s → 16.6 ms on a journal of 4,823 articles); matches on a normalised name or ORCID, so it also finds articles the original misses | 3.3 · 3.5 |
| [recommendBySimilarity](https://github.com/OJSBR/recommendBySimilarity) | OJS | generic | Original recommendBySimilarity by PKP/SFU, rewritten by OJSBR: the "similar articles" list is materialised by a scheduled task and read from a table, instead of running a ranked search-index query with correlated subqueries on every article view; same terms and same ordering as the core | 3.3 · 3.5 |
| [citations](https://github.com/OJSBR/citations) | OJS | generic | Citation counts and the list of citing works from Crossref Cited-by, Scopus, Europe PMC and Google Scholar on the article page — OJS 3.5 fork of `RBoelter/citations`, the original plugin by Ronny Bölter, which stops at 3.4 | 3.5 |
| [pln](https://github.com/OJSBR/pln) | OJS | generic | PKP Preservation Network (PLN / PKP PN) — unofficial OJS 3.5 build (based on pkp/pln#117); superseded by the official release 4.0.0.0 in PKP's Plugin Gallery, no further builds | 3.5 |
| [shariff](https://github.com/OJSBR/shariff) | OJS | generic | Privacy-friendly social media share buttons (Shariff) — unofficial OJS/OMP 3.5 build of ojsde/shariff with the Portuguese fixes proposed in ojsde/shariff#54, maintained until the official release | 3.5 |

### OMP (Open Monograph Press)

| Plugin | Applications | Type | What it does | PKP versions |
|--------|--------------|------|--------------|--------------|
| [customMetadata](https://github.com/OJSBR/customMetadata) | OMP | generic | Configurable extra metadata fields on the publication Metadata tab | 3.4 · 3.5 |
| [crossref](https://github.com/OJSBR/crossref) | OMP | generic | Crossref DOI registration/export for monographs and chapters (fills a gap OMP core lacks) | 3.4 · 3.5 |
| [assignEditorGeneral](https://github.com/OJSBR/assignEditorGeneral) | OMP | generic | Automatically assigns all active General Editors to each new submission | 3.5 |
| [requiredMultilingualMetadata](https://github.com/OJSBR/requiredMultilingualMetadata) | OJS · OMP | generic | Require the title, abstract and keywords in languages beyond the submission language | 3.5 |
| [audioPlayer](https://github.com/OJSBR/audioPlayer) | OMP | generic | Turns a book's audio files into a listenable audiobook: play button per file, player bar with in-track seeking, continuous playback, adjustable speed and resume where the listener stopped; serves the file itself with full HTTP Range support, because the core answers `Accept-Ranges: none` | 3.5 |
| [pdfFlipbook](https://github.com/OJSBR/pdfFlipbook) | OMP | generic | Page-turning (flipbook) reading mode for PDF monographs, beside the native PDF viewer and never replacing it — the flipbook paints to canvas, so it has no text selection or screen-reader access. StPageFlip + PDF.js, vendored | 3.5 |

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
| blindReviewGuard | OJS | [⬇ 1.0.2.0](https://github.com/OJSBR/blindReviewGuard/releases/download/1.0.2.0/blindReviewGuard-1.0.2.0.tar.gz) | — | — |
| coauthorAlert | OJS | [⬇ 1.0.1.0](https://github.com/OJSBR/coauthorAlert/releases/download/1.0.1.0/coauthorAlert-1.0.1.0.tar.gz) | — | — |
| coAuthorParticipants | OJS | [⬇ 1.0.1.0](https://github.com/OJSBR/coAuthorParticipants/releases/download/1.0.1.0/coAuthorParticipants-1.0.1.0.tar.gz) | — | — |
| viewcounter | OJS | [⬇ 1.3.0.3](https://github.com/OJSBR/viewcounter/releases/download/1.3.0.3/viewcounter-1.3.0.3.tar.gz) | [⬇ 1.1.1.3](https://github.com/OJSBR/viewcounter/releases/download/1.1.1.3/viewcounter-1.1.1.3.tar.gz) | — |
| mostRead | OJS · OMP | [⬇ 3.5.0.7](https://github.com/OJSBR/mostRead/releases/download/3.5.0.7/mostRead-3.5.0.7.tar.gz) | [⬇ 3.4.0.4](https://github.com/OJSBR/mostRead/releases/download/3.4.0.4/mostRead-3.4.0.4.tar.gz) | — |
| whatsAppContributor | OJS | [⬇ 1.2.0.3](https://github.com/OJSBR/whatsAppContributor/releases/download/1.2.0.3/whatsAppContributor-1.2.0.3.tar.gz) | [⬇ 1.2.0.3](https://github.com/OJSBR/whatsAppContributor/releases/download/1.2.0.3-ojs3.4/whatsAppContributor-1.2.0.3-ojs3.4.tar.gz) | — |
| doiInSummary | OJS | [⬇ 3.5.0.6](https://github.com/OJSBR/doiInSummary/releases/download/3.5.0.6/doiInSummary-3.5.0.6.tar.gz) | [⬇ 3.4.0.4](https://github.com/OJSBR/doiInSummary/releases/download/3.4.0.4/doiInSummary-3.4.0.4.tar.gz) | — |
| ojsbrFilenameRename | OJS · OMP | [⬇ 1.2.1.0](https://github.com/OJSBR/ojsbrFilenameRename/releases/download/1.2.1.0/ojsbrFilenameRename-1.2.1.0.tar.gz) | [⬇ 1.2.0.1](https://github.com/OJSBR/ojsbrFilenameRename/releases/download/1.2.0.1-ojs3.4/ojsbrFilenameRename-1.2.0.1-ojs3.4.tar.gz) | — |
| orcidManualEntry | OJS · OMP | [⬇ 1.1.6.0](https://github.com/OJSBR/orcidManualEntry/releases/download/1.1.6.0/orcidManualEntry-1.1.6.0.tar.gz) | — | — |
| requiredAuthorMetadata | OJS · OMP | [⬇ 1.1.0.0](https://github.com/OJSBR/requiredAuthorMetadata/releases/download/1.1.0.0/requiredAuthorMetadata-1.1.0.0.tar.gz) | — | — |
| reviewerRecommendationManager | OJS | [⬇ 1.0.4.1](https://github.com/OJSBR/reviewerRecommendationManager/releases/download/1.0.4.1/reviewerRecommendationManager-1.0.4.1.tar.gz) | [⬇ 1.0.4.2](https://github.com/OJSBR/reviewerRecommendationManager/releases/download/1.0.4.2-ojs3.4/reviewerRecommendationManager-1.0.4.2-ojs3.4.tar.gz) | — |
| accessibility | OJS | [⬇ 1.0.2.1](https://github.com/OJSBR/accessibility/releases/download/1.0.2.1/accessibility-1.0.2.1.tar.gz) | [⬇ 1.0.2.1](https://github.com/OJSBR/accessibility/releases/download/1.0.2.1-ojs3.4/accessibility-1.0.2.1-ojs3.4.tar.gz) | [⬇ 1.0.2.1](https://github.com/OJSBR/accessibility/releases/download/1.0.2.1-ojs3.3/accessibility-1.0.2.1-ojs3.3.tar.gz) |
| vlibras | OJS | [⬇ 1.0.1.1](https://github.com/OJSBR/vlibras/releases/download/1.0.1.1/vlibras-1.0.1.1.tar.gz) | [⬇ 1.0.1.1](https://github.com/OJSBR/vlibras/releases/download/1.0.1.1-ojs3.4/vlibras-1.0.1.1-ojs3.4.tar.gz) | [⬇ 1.0.1.1](https://github.com/OJSBR/vlibras/releases/download/1.0.1.1-ojs3.3/vlibras-1.0.1.1-ojs3.3.tar.gz) |
| articleMetricsBadges | OJS | [⬇ 1.1.1.0](https://github.com/OJSBR/articleMetricsBadges/releases/download/1.1.1.0/articleMetricsBadges-1.1.1.0.tar.gz) | [⬇ 1.1.1.0](https://github.com/OJSBR/articleMetricsBadges/releases/download/1.1.1.0-ojs3.4/articleMetricsBadges-1.1.1.0-ojs3.4.tar.gz) | [⬇ 1.1.1.0](https://github.com/OJSBR/articleMetricsBadges/releases/download/1.1.1.0-ojs3.3/articleMetricsBadges-1.1.1.0-ojs3.3.tar.gz) |
| recommendByAuthor | OJS | [⬇ 2.0.0.3](https://github.com/OJSBR/recommendByAuthor/releases/download/2.0.0.3/recommendByAuthor-2.0.0.3.tar.gz) | — | [⬇ 2.0.0.1](https://github.com/OJSBR/recommendByAuthor/releases/download/2.0.0.1-ojs3.3/recommendByAuthor-2.0.0.1-ojs3.3.tar.gz) |
| recommendBySimilarity | OJS | [⬇ 2.0.0.3](https://github.com/OJSBR/recommendBySimilarity/releases/download/2.0.0.3/recommendBySimilarity-2.0.0.3.tar.gz) | — | [⬇ 2.0.0.1](https://github.com/OJSBR/recommendBySimilarity/releases/download/2.0.0.1-ojs3.3/recommendBySimilarity-2.0.0.1-ojs3.3.tar.gz) |
| staticEditorialTeam | OJS · OMP | [⬇ 1.0.2.0](https://github.com/OJSBR/staticEditorialTeam/releases/download/1.0.2.0/staticEditorialTeam-1.0.2.0.tar.gz) | — | — |
| classicUserEditor | OJS · OMP | [⬇ 1.0.2.0](https://github.com/OJSBR/classicUserEditor/releases/download/1.0.2.0/classicUserEditor-1.0.2.0.tar.gz) | — | — |
| ojsbrUserRoleFilter | OJS · OMP | [⬇ 1.0.1.0](https://github.com/OJSBR/ojsbrUserRoleFilter/releases/download/1.0.1.0/ojsbrUserRoleFilter-1.0.1.0.tar.gz) | — | — |
| authorContributorEditor | OJS | [⬇ 1.0.0.2](https://github.com/OJSBR/authorContributorEditor/releases/download/1.0.0.2/authorContributorEditor-1.0.0.2.tar.gz) | — | — |
| reviewerDirectory | OJS · OMP | [⬇ 1.0.2.0](https://github.com/OJSBR/reviewerDirectory/releases/download/1.0.2.0/reviewerDirectory-1.0.2.0.tar.gz) | — | — |
| controlledVocabSplitter | OJS · OMP | [⬇ 1.0.2.0](https://github.com/OJSBR/controlledVocabSplitter/releases/download/1.0.2.0/controlledVocabSplitter-1.0.2.0.tar.gz) | — | — |
| crossrefConference | OJS | [⬇ 1.0.1.0](https://github.com/OJSBR/crossrefConference/releases/download/1.0.1.0/crossrefConference-1.0.1.0.tar.gz) | — | — |
| languageToggleByFlag | OJS | [⬇ 3.5.0.7](https://github.com/OJSBR/languageToggleByFlag/releases/download/3.5.0.7/languageToggleByFlag-3.5.0.7.tar.gz) | — | — |
| pln | OJS | [⬇ 4.0.0.3](https://github.com/OJSBR/pln/releases/download/4.0.0.3/pln-4.0.0.3.tar.gz) | — | — |
| shariff | OJS | [⬇ 3.5.1.3](https://github.com/OJSBR/shariff/releases/download/3.5.1.3/shariff-3.5.1.3.tar.gz) | — | — |
| epubJsViewer | OJS · OPS · OMP | [⬇ 1.2.1.0](https://github.com/OJSBR/epubJsViewer/releases/download/1.2.1.0/epubJsViewer-1.2.1.0.tar.gz) | — | — |
| citations | OJS | [⬇ 3.5.0.2](https://github.com/OJSBR/citations/releases/download/3.5.0.2/citations-3.5.0.2.tar.gz) | — | — |
| ojsbrWebhook | OJS | — | [⬇ 1.1.0.0](https://github.com/OJSBR/ojsbrWebhook/releases/download/1.1.0.0/ojsbrWebhook-1.1.0.0.tar.gz) | — |
| ojsbrServices | OJS | [⬇ 1.0.1.0](https://github.com/OJSBR/ojsbrServices/releases/download/1.0.1.0/ojsbrServices-1.0.1.0.tar.gz) | — | — |
| customMetadata | OMP | [⬇ 1.0.1.2](https://github.com/OJSBR/customMetadata/releases/download/1.0.1.2/customMetadata-1.0.1.2.tar.gz) | [⬇ 1.0.1.2](https://github.com/OJSBR/customMetadata/releases/download/1.0.1.2-omp3.4/customMetadata-1.0.1.2-omp3.4.tar.gz) | — |
| crossref | OMP | [⬇ 1.0.0.7](https://github.com/OJSBR/crossref/releases/download/1.0.0.7/crossref-1.0.0.7.tar.gz) | [⬇ 1.0.0.7](https://github.com/OJSBR/crossref/releases/download/1.0.0.7-omp3.4/crossref-1.0.0.7-omp3.4.tar.gz) | — |
| assignEditorGeneral | OMP | [⬇ 1.1.0.0](https://github.com/OJSBR/assignEditorGeneral/releases/download/1.1.0.0/assignEditorGeneral-1.1.0.0.tar.gz) | — | — |
| requiredMultilingualMetadata | OJS · OMP | [⬇ 1.1.1.0](https://github.com/OJSBR/requiredMultilingualMetadata/releases/download/1.1.1.0/requiredMultilingualMetadata-1.1.1.0.tar.gz) | — | — |
| audioPlayer | OMP | [⬇ 1.0.2.0](https://github.com/OJSBR/audioPlayer/releases/download/1.0.2.0-omp3.5/audioPlayer-1.0.2.0-omp3.5.tar.gz) | — | — |
| pdfFlipbook | OMP | [⬇ 0.4.0.0](https://github.com/OJSBR/pdfFlipbook/releases/download/0.4.0.0-omp3.5/pdfFlipbook-0.4.0.0-omp3.5.tar.gz) | — | — |
| keywordCloudClassicBeautiful | OJS · OMP | [⬇ 1.0.3.0](https://github.com/OJSBR/keywordCloudClassicBeautiful/releases/download/1.0.3.0/keywordCloudClassicBeautiful-1.0.3.0.tar.gz) | [⬇ 1.0.3.0](https://github.com/OJSBR/keywordCloudClassicBeautiful/releases/download/1.0.3.0-ojs3.4/keywordCloudClassicBeautiful-1.0.3.0-ojs3.4.tar.gz) | — |

> The **latest** package of each plugin is always on its repository's *Releases* page.

## Credits

Some plugins were rewritten or adapted by OJSBR from earlier community work; upstream authors
are credited in each repository's **Credits & authorship** section. Original authors we build
on include **Antti-Jussi Nygård (@ajnyga)**, **Ronny Bölter (@RBoelter)**, **@zielaq**,
**Lepidus Tecnologia**, **FuturePress (epub.js)**, **STI-FFLCH/USP**, **ABCD/USP** and **PKP**.

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
Nygård (@ajnyga)**, **Ronny Bölter (@RBoelter)**, **@zielaq**, **Lepidus Tecnologia**,
**FuturePress (epub.js)**, **STI-FFLCH/USP**, **ABCD/USP** e **PKP**.

### Licença

Todos os plugins da OJSBR são distribuídos sob a **GNU GPL v3**.
