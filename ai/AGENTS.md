# Repository Guidelines

These instructions govern agent behavior for this project.

## Mission Critical Coding
- Ensure high reliability and maintainability of all code.
- Include descriptive comments for complex logic.
- Run available tests (`pytest` or `make test`) before committing.

## Documentation
- Place architectural and protocol documentation in `/docs`.
- Keep AI and LLM related materials in `/ai`.
- EchoVault specific assets and files reside in `/echovault`.

## Commits, PRs, and Branching Strategy
- Use clear commit messages summarizing the change.
- Never push commits and PRs to ``main``.
- Use ``dev/[agent-name]`` instead. E.g, dev/codex for Codex, dev/copilot for GitHub Copilot, etc.
