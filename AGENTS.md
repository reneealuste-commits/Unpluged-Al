# Unpluged-Al

## Cursor Cloud specific instructions

This repo is **not** a runnable application — there is no server, database, frontend, API, or port. It is a **Python document-generation pipeline**: Markdown/data in `opord/` are compiled into PDF/DOCX/ZIP deliverables by the `opord/generate_*.py` scripts. "Running the app" means executing those generators and confirming the output files are produced.

### Dependencies
- Runtime is Python 3 (`python3`). Third-party libs: `reportlab` (all PDF generators), `python-docx` (imported as `docx`, used by `scripts/build_reference_docx.py`), and `pypandoc` (used by `generate_docx.py`). There is no `requirements.txt`/`pyproject.toml`; deps come only from `import` statements. The startup update script installs them.
- `generate_docx.py` needs a real **pandoc** binary. We install `pypandoc_binary` (pip) which bundles pandoc, so **no system `apt install pandoc` is required**. Verify with `python3 -c "import pypandoc; print(pypandoc.get_pandoc_version())"`.

### Running the generators
All commands run from the `opord/` directory. The canonical build commands are in `opord/README.md` (section "PDF uuendamine"), e.g. `python3 generate_pdf.py`, `python3 generate_packages.py`, `python3 generate_docx.py`, `python3 generate_taskukaardid_pdf.py`. Other working generators: `generate_toidu_pdf.py`, `generate_hindamisvorm_pdf.py`, `generate_loo_taskukaardid_pdf.py`, `generate_olukorda_teadlikkus_pdf.py`.

### Non-obvious gotchas
- **Generators overwrite the committed artifacts in place** (the `*.pdf`, `*.docx`, and `*.zip` files are checked into `opord/`). Running a generator dirties the working tree. If you only ran a generator to verify the environment and don't intend to commit regenerated binaries, restore them with `git checkout -- opord/`.
- `generate_komplimendid_pdf.py` is a **broken, deprecated wrapper** — its own source has an invalid byte and raises `SyntaxError` on import. This is pre-existing (not an environment issue). Use `generate_olukorda_teadlikkus_pdf.py` instead.
- `generate_docx.py` prints harmless `[WARNING] Could not fetch resource ...` lines for remote/missing images; it still succeeds and produces the `.docx`.

### Lint / test
There are **no automated tests and no linters** configured (no `tests/`, pytest, ruff/flake8, or CI). End-to-end verification = run the generators and confirm the PDFs/DOCX/ZIP are produced without error.
