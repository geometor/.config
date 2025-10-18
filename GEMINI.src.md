# GEOMETOR

GEOMETOR is an open-source project for exploring geometry, nature, and logic. It is a Python library for creating symbolic models of geometric constructions, investigating patterns in nature, and exploring abstraction and reasoning.

A key motivation is the exploration of the golden ratio.

## Organization

This project is a monorepo containing several distinct Python packages as subdirectories. Each subdirectory follows a standardized structure to ensure consistency and ease of navigation.

### Standard Repository Structure

A typical repository, `<repo_name>`, will have the following layout:

-   **`src/geometor/<repo_name>/`**: Contains the primary Python source code, organized as a namespace package.
-   **`docsrc/`**: Holds the source files for generating documentation, typically using Sphinx and Jinja templates.
-   **`README.rst`**: The main landing page for the repository, providing an overview, installation, and usage instructions.
-   **`ROADMAP.md`**: Outlines the future development plans, features, and long-term objectives for the repository.
-   **`GEMINI.md`**: A dedicated context file for the Gemini AI, summarizing the repository's purpose, key modules, and development plan.
-   **`pyproject.toml`**: The standard Python project configuration file, defining metadata, dependencies, and build settings.
-   **`constructions/`**: (Used in `explorer`) A directory for storing saved geometric constructions in JSON format. Other repositories may have similar data-specific directories.

### Key Repos

-   **model**: The core library for geometric constructions.
-   **explorer**: A web-based UI for the model, using Flask and SVG.
-   **divine**: Analysis of golden sections in a model.
-   **euclid** and **elements**: Explorations of Euclid's Elements.

## Development Workflow

A key practice in this project is to commit changes frequently after completing a task. The typical workflow is as follows:

1.  **Complete a Task:** Finish a discrete unit of work, such as implementing a feature or fixing a bug.
2.  **Confirm Commit:** The developer will be asked if they want to commit the changes.
3.  **Review Changes:**
    -   Run `git status` to see an overview of modified files.
    -   Run `git diff` on the relevant files to review the specific changes.
4.  **Write Commit Message:** Based on the review, compose a detailed and descriptive commit message.
5.  **Commit:** Stage all changes with `git add .` and then commit.

### Commit Message Format

-   **Subject:** Concise, action-oriented subject line.
-   **Body:** Bullet point details.

### FEATURE Workflow

When starting a new feature, the `FEATURE` workflow is used. This can be triggered by saying **"FEATURE: `<feature-name>`"**.

1.  **Discuss Scope and Requirements:** Collaboratively define the feature's scope, requirements, and implementation plan.
2.  **Create Feature Branch:** Create a new branch for the feature development (`git checkout -b feature/<feature-name>`).
3.  **Implement Feature:** Implement the feature, committing changes frequently.
4.  **Finalize with ROLLUP:** Once the feature is complete, use the `ROLLUP` workflow to finalize the changes.

### ROLLUP Workflow

When a set of related changes is ready to be finalized, the `ROLLUP` workflow is used. This can be triggered by saying **"ROLLUP: `<directory>`"**.

1.  **Analyze Changes:**
    -   Run `git status` to get an overview of all modified, staged, and untracked files.
    -   Review the diffs of the changed files to understand the specific modifications.
2.  **Update Documentation:**
    -   Review and update `README.rst`, `GEMINI.md`, and `ROADMAP.md` to ensure they are consistent with the latest changes.
    -   Remove any completed items from `ROADMAP.md`.
3.  **Increment Version:**
    -   Update the `__version__` string in the project's `src/geometor/<repo_name>/__init__.py`.
4.  **Update Changelog:**
    -   Add a summary of changes to the project's changelog file.
5.  **Commit Changes:**
    -   Stage all changes (`git add .`).
    -   Commit the changes using the standard commit message format.
6.  **Tag and Push:**
    -   Create a git tag for the new version (e.g., `git tag vX.Y.Z`).
    -   Push the commit and the new tag to the remote repository (`git push && git push --tags`).
7.  **Merge to Main (if on a feature branch):**
    -   Checkout the main branch (`git checkout main`).
    -   Merge the feature branch (`git merge feature/<feature-name>`).
    -   Push the merge commit (`git push`).
    -   Delete the feature branch (`git branch -d feature/<feature-name>`).

## Next Steps

-   Implement file management in the explorer UI (new, save, open, etc.) using the model's serialization features.
-   Integrate `divine` analysis into the explorer, running analysis on each new point.
-   Add `hidden` and `guide` properties to elements.
-   Consolidate and clean up the JavaScript.
