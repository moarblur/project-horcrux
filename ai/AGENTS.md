# Repository Guidelines

These instructions govern agent behavior for this project.

## General Guidelines
- Always follow the project's coding standards.
- Maintain a clean and organized codebase.
- Use meaningful variable and function names.
- Write code that is easy to read and understand.
- Avoid unnecessary complexity and over-engineering.
- Keep dependencies up to date and document any major changes.
- Use version control effectively, committing often with clear messages.
- Write unit tests for new features and bug fixes.

## Coding Standards
- Follow PEP 8 for Python code style.
- Use 4 spaces for indentation.
- Limit lines to 79 characters.
- Use descriptive names for variables, functions, and classes.
- Use type hints for function signatures.
- Use f-strings for string formatting in Python 3.6+.
- Use `snake_case` for variable and function names.
- Use `CamelCase` for class names.
- Use `UPPER_CASE` for constants.
- Avoid using global variables unless absolutely necessary.
- Use `assert` statements for debugging and testing.
- Use `logging` for logging messages instead of `print`.
- Use `docstrings` for all public modules, functions, classes, and methods.
- Use `__init__.py` files to mark directories as Python packages.
- Organize imports in the following order:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library specific imports
- Use `isort` to automatically sort imports.
- Use `black` for code formatting.
- Use `mypy` for type checking.
- Use `flake8` for linting. 
- Use `bandit` for security checks.
- Use `pydocstyle` for checking compliance with Python docstring conventions.
- Use `pytest` for testing.
- Use `coverage` to measure code coverage of tests.
- Use `pre-commit` hooks to enforce coding standards before committing.
- Use `make` commands for common tasks (e.g., `make test`, `make lint`, `make format`).
- Use `docker` for containerization and environment consistency.
- Use `docker-compose` for multi-container applications.
- Use `poetry` for dependency management and packaging.
- Use `pip-tools` for managing Python dependencies.
- Use `virtualenv` or `venv` for creating isolated Python environments.
- Use `git` for version control.
- Use `git flow` for branching and merging strategies.
- Use `GitHub Actions` for continuous integration and deployment.
- Use `Sphinx` for generating documentation.
- Use `mkdocs` for project documentation.

## Mission Critical Coding
- Ensure high reliability and maintainability of all code.
- Include descriptive comments for complex logic.
- Run available tests (`pytest` or `make test`) before committing.
- Use `pre-commit` hooks to automatically format code and run linters before committing.
- Document any non-obvious code decisions in the code comments.
- Use version control effectively, committing often with clear messages.
- Use feature branches for new features or bug fixes.
- Use `dev/[agent-name]` branches for development work.
- Conduct code reviews for all pull requests.
- Ensure all code is peer-reviewed before merging into `main`.

## Documentation
- Place architectural and protocol documentation in `/docs`.
- Keep AI and LLM related materials, status trackers, agent logs etc. in `/ai`.
- EchoVault specific assets, code and files reside in `/echovault`.
- Use Markdown for documentation files.
- Use clear and concise language.
- Document all public APIs and endpoints.
- Include examples and usage instructions.
- Keep documentation up to date with code changes.
- Use `mkdocs` for project documentation.

## Commits, PRs, and Branching Strategy
- Use `git commit` to commit changes.
- Use clear commit messages summarizing the change.
- Never push commits and PRs to ``main``.
- Use ``dev/[agent-name]`` instead. E.g, dev/codex for Codex, dev/copilot for GitHub Copilot, etc.
- PRs must be reviewed by at least one other agent or contributor.
- Use the following PR template:
  ```
  ## Description
  <!-- Describe the changes made in this PR -->

  ## Related Issues
  <!-- Link to any related issues or tasks -->

  ## Checklist
  - [ ] Code follows project guidelines
  - [ ] Tests have been added/updated
  - [ ] Documentation has been updated if necessary
  ```
- Use `git flow` for branching and merging strategies.
- Use `git rebase` to keep feature branches up to date with `main` or contributor/maintainer defined branch.
- Use `git merge` to merge feature branches into `main`.
- Use `git cherry-pick` to apply specific commits from one branch to another.
- Use `git tag` to create tags for releases.
- Use `git stash` to temporarily save changes that are not ready to be committed.
- Use `git reset` to undo commits or changes.
- Use `git revert` to create a new commit that undoes the changes made by a previous commit.
- Use `git log` to view commit history.
- Use `git diff` to view changes between commits or branches.
- Use `git status` to view the current status of the repository.

## Security and Privacy
- Never hardcode sensitive information (e.g., API keys, passwords) in the codebase.
- Use environment variables to manage sensitive information.
- Use `.env` files for local development and ensure they are not committed to version control.
- Use `gitignore` to exclude sensitive files and directories from version control.
- Regularly review and update dependencies to patch security vulnerabilities.
- Use `bandit` to check for security issues in the code.
- Use `safety` to check for known vulnerabilities in dependencies.
- Use `secrets` module in Python to generate secure random numbers and strings.
- Use `cryptography` library for encryption and decryption of sensitive data.
- Use HTTPS for all network communications.
- Use secure coding practices to prevent common vulnerabilities (e.g., SQL injection, XSS).
- Regularly review and update security policies and practices.
- Use `OWASP` guidelines for secure coding practices.
- Use `CVE` databases to check for known vulnerabilities in dependencies.
- Use `Snyk` or similar tools to monitor dependencies for vulnerabilities.
- Use `GitHub Security Alerts` to monitor for vulnerabilities in dependencies.
- Use `GitHub Dependabot` to automatically update dependencies with security patches.
- Use `GitHub Code Scanning` to automatically scan code for security vulnerabilities.
- Use `GitHub Secret Scanning` to automatically scan for sensitive information in code.
- Use `GitHub Actions` to automate security checks and tests.
- Use `GitHub Issues` to track security vulnerabilities and issues.
- Use `GitHub Discussions` to discuss security practices and issues with the community.
- Use `GitHub Projects` to manage security-related tasks and issues.
- Use `GitHub Security Policy` to define security practices and procedures for the project.
- Use `GitHub Security Advisory` to disclose security vulnerabilities in the project.
- Use `GitHub Security Lab` to collaborate with the community on security issues.
- Use `GitHub Security Audit Log` to monitor security-related activities in the repository.
- Use `GitHub Security Notifications` to receive notifications about security issues in the repository.
- Use `GitHub Security Insights` to gain insights into security issues in the repository.
- Use `GitHub Security Best Practices` to follow best practices for security in the repository.
- Use `GitHub Security Training` to train contributors on security best practices.

## AI and LLM Specific Guidelines
- Use AI and LLMs responsibly and ethically.
- Ensure AI-generated code adheres to the project's coding standards.
- Review AI-generated code for correctness and security before merging.
- Use AI and LLMs to assist with repetitive tasks, but do not rely on them for critical decisions.
- Document any AI or LLM usage in the code comments.
- Use AI and LLMs to generate documentation, but review and edit the output for accuracy and clarity.
- Use AI and LLMs to assist with testing, but ensure tests are comprehensive and cover edge cases.
- Use AI and LLMs to assist with debugging, but do not rely solely on them for identifying issues.
- Use AI and LLMs to assist with code reviews, but ensure reviews are thorough and cover all aspects of the code.