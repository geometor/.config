# Agent Instructions for `docsrc` Structure

This document outlines the standards for organizing reStructuredText (`.rst`) files within the `docsrc` directory. Adhering to these standards ensures consistency and proper functionality of navigation, API documentation, and content collections.

## 1. Main Navigation (`index.rst`)

The primary navigation for the documentation is controlled by the `.. toctree::` directive in `docsrc/index.rst`.

-   **Purpose:** To define the top-level structure of the documentation that appears in the main navigation menu.
-   **Configuration:**
    -   `:hidden:`: The `toctree` is hidden from the `index.rst` page itself to allow for a custom introduction.
    -   `:maxdepth: 2`: Sets the maximum depth of the navigation tree to two levels.
-   **Action:** To add a new top-level section to the documentation, add the corresponding `.rst` file or directory `index.rst` to the `toctree` in `docsrc/index.rst`.

**Example (`docsrc/index.rst`):**

```rst
.. toctree::
   :hidden:
   :maxdepth: 2

   mission/index.rst
   usage/index.rst
   modules/index.rst
   ...
```

## 2. API Documentation (`autoapi`)

API documentation is automatically generated from the source code using the `autoapi` extension.

-   **Configuration (`docsrc/conf.py` -> `global_conf.py`):**
    -   `autoapi_dirs = ['../src']`: `autoapi` is configured to scan the `src` directory.
    -   `autoapi_root = 'modules/api'`: The generated API documentation is placed in `docsrc/modules/api`.
-   **Entry Point (`docsrc/modules/index.rst`):**
    -   The `docsrc/modules/index.rst` file serves as the entry point for the API documentation. It includes the `autoapi` generated index.
-   **Action:** No action is required to generate the API documentation. It is automatically generated. To include it in your documentation, ensure that `modules/index.rst` is part of the main `toctree`.

**Example (`docsrc/modules/index.rst`):**

```rst
modules
=======

.. include:: api/index.rst
```

## 3. Content Collections (`collection` directive)

The custom `.. collection::` directive is used to create listings of documents, typically for blogs, logs, or portfolios.

-   **Purpose:** To automatically discover and list documents within a directory, sorted and formatted according to specified options.
-   **Implementation:** The directive is defined in `src/photon_platform/publish/directives/collection.py`.
-   **Options:**
    -   `:type:`: Filters documents by the `type` metadata field in the `.rst` file's frontmatter (e.g., `:type: log`).
    -   `:sort:`: Sorts the documents by a metadata field (e.g., `:sort: date`).
    -   `:reverse:`: Reverses the sort order.
    -   `:template:`: Specifies a Jinja2 template to use for rendering the collection (defaults to `_macros/collection.html`).
    -   `:limit:`: Limits the number of items in the collection.
    -   `:title:`: Sets the title of the collection.
-   **Action:** To create a collection, use the `.. collection::` directive in an `index.rst` file within a subdirectory. Add metadata to the individual `.rst` files that will be part of the collection.

**Example (`docsrc/log/index.rst`):**

```rst
:navigation: header
:order: 3

log
===

.. collection::
   :type: log
   :sort: date
   :reverse:
```

**Example Metadata in a log entry `.rst` file:**

```rst
:type: log
:date: 24.125-164141
:author: phi

My Log Entry Title
==================

This is the content of my log entry.
```

The `:date:` field uses a "journal day" format, which is a floating-point number representing the year and day of the year, followed by a timestamp.

## 4. Page-level Metadata for Navigation

You can control where individual pages appear in the navigation menus (header and footer) by adding metadata to the top of your `.rst` files.

-   `:navigation: header` or `:navigation: footer`: Adds a link to the page in the corresponding navigation menu.
-   `:order: <number>`: Specifies the order of the link in the navigation menu (lower numbers appear first).

**Header Navigation:**

-   `mission/index.rst`: `:navigation: header`, `:order: 1`
-   `usage/index.rst`: `:navigation: header`, `:order: 2`
-   `modules/index.rst`: `:navigation: header`, `:order: 3`
-   `logs/index.rst` (or `logs.rst` if it's a direct file): `:navigation: header`, `:order: 4`

**Footer Navigation:**

-   `about.rst`: `:navigation: footer`, `:order: 1`
-   `connect.rst`: `:navigation: footer`, `:order: 2`
-   `glossary.rst`: `:navigation: footer`, `:order: 3`
-   `todos.rst`: `:navigation: footer`, `:order: 4`
-   `changelog.rst`: `:navigation: footer`, `:order: 5`

**Example (`docsrc/log/index.rst`):**

```rst
:navigation: header
:order: 3

log
===
...
```
