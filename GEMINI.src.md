# GEOMETOR

An open-source project for exploring geometry, nature, and logic.

## Overview

A Python library for creating symbolic models of geometric constructions, investigating patterns in nature, and exploring abstraction and reasoning. A key motivation is the exploration of the golden ratio.

## Key Repos

-   **model**: The core library for geometric constructions.
-   **explorer**: A web-based UI for the model, using Flask and SVG.
-   **divine**: Analysis of golden sections in a model.
-   **elements**: Explorations of Euclid's Elements.
-   **seer**: An AI-driven framework for solving abstract reasoning challenges.

## Development Plan

-   Add `hidden` and `guide` properties to elements.

## Workflows

### Create Branch

1.  **Navigate to Repository**: `cd /home/phi/PROJECTS/geometor/<repo_name>`
2.  **Checkout Main**: `git checkout main`
3.  **Pull Latest**: `git pull origin main`
4.  **Create Branch**: `git checkout -b <branch_name>`

### Release Branch

1.  **Navigate to Repository**: `cd /home/phi/PROJECTS/geometor/<repo_name>`
2.  **Update Version**: Increment `__version__` in `src/geometor/<package>/__init__.py`
3.  **Update Changelog**: Add entry to `CHANGELOG.rst`
4.  **Commit Changes**: `git add . && git commit -m "chore: bump version to <version>"`
5.  **Merge to Main**: `git checkout main && git merge <branch_name>`
6.  **Tag Version**: `git tag v<version>`
7.  **Push**: `git push origin main --tags`
