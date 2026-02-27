# Contributing to GEOMETOR

First off, thank you for considering contributing to GEOMETOR! This project is a collaborative effort, and we welcome all contributions. To ensure the project remains stable and maintainable, we follow a set of development guidelines.

## The Core Philosophy: Protect the `main` Branch

Our primary goal is to ensure that the `main` branch always represents a stable, production-ready state. To achieve this, **direct pushes to the `main` branch are prohibited.** All changes, from minor bugfixes to major features, must be integrated through a Pull Request process.

## The Branching Model

We use a branching model inspired by Git Flow. The two primary, long-lived branches are `main` and `develop`.

-   **`main`**: This branch is our sacred, stable release branch. It is only ever updated by merging the `develop` branch into it to create a new version.
-   **`develop`**: This is the primary integration branch for all new features and bugfixes. All feature branches are created from `develop` and are merged back into `develop`.
-   **Feature Branches**: All new work is done on a feature branch.
    -   **Naming Convention:** Use a descriptive name prefixed with `feature/`, `bugfix/`, or `docs/`.
        -   `feature/sse-integration`
        -   `bugfix/fix-save-button-state`
        -   `docs/update-readme`
    -   Feature branches should always be created from the latest version of the `develop` branch.

## The Development Workflow

Here is the step-by-step process for contributing a change to the GEOMETOR project.

### Step 1: Create Your Feature Branch

Before you start writing any code, make sure you have the latest version of the `develop` branch, and then create your new branch from it.

```bash
# Switch to the develop branch
git checkout develop

# Pull the latest changes
git pull origin develop

# Create your new feature branch
git checkout -b feature/your-feature-name
```

### Step 2: Do Your Work

Make your changes in the feature branch. Commit your work early and often with clear, descriptive commit messages.

```bash
# ... write code and stage your changes ...
git add .

# Commit your changes
git commit -m "feat: Implement the new toolbar component"
```

### Step 3: Push Your Branch to GitHub

When you are ready to get feedback or your feature is complete, push your branch to the remote repository on GitHub.

```bash
git push origin feature/your-feature-name
```

### Step 4: Open a Pull Request (PR)

Go to the GEOMETOR repository on GitHub. You will see a prompt to create a Pull Request from your new branch.

-   **Target Branch:** Ensure the PR is targeting the `develop` branch.
-   **Title:** Write a clear and concise title for your PR.
-   **Description:** Provide a detailed description of the changes you made, why you made them, and any relevant context. If your PR addresses a GitHub Issue, be sure to link it.

### Step 5: Code Review and Automated Checks

Once your PR is open, two things will happen:

1.  **Automated Checks (CI):** Our GitHub Actions workflow will automatically run all tests against your changes. The PR will be blocked from merging if any tests fail.
2.  **Code Review:** A project maintainer will review your code, provide feedback, and may request changes.

### Step 6: Merge and Clean Up

Once the PR is approved and all checks have passed, a maintainer will merge it into the `develop` branch. After your branch is merged, you can safely delete your local branch.

```bash
# Switch back to the develop branch
git checkout develop

# Delete your local feature branch
git branch -d feature/your-feature-name
```

## Versioning and Releases

We follow **Semantic Versioning (SemVer)** (`MAJOR.MINOR.PATCH`).

When the `develop` branch has accumulated enough features for a new release, a maintainer will open a final PR to merge `develop` into `main`. Once merged, a new version tag (e.g., `v0.2.0`) will be created on the `main` branch to mark the official release.

Thank you for helping us build a better GEOMETOR!
