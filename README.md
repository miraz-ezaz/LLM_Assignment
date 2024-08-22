# PropertyAI

PropertyAI is a Django-based project designed to manage and update property-related content using the Ollama model for rewriting titles, descriptions, and generating summaries. The project includes CLI commands to perform these operations on all properties within the database.

## Getting Started

### Clone the Repository

To clone the repository, run the following command in your terminal:

```bash
git clone https://github.com/miraz-ezaz/LLM_Assignment.git
```

Navigate into the project directory:

```bash
cd LLM_Assignment
```

### Create the `.env` File

The `.env` file is required to store environment-specific variables, such as database configurations and Ollama model settings. Create a `.env` file inside the `propertyAI` folder.

Here’s a sample content for the `.env` file:

```env
# Default Database Configuration
DEFAULT_DB_ENGINE=django.db.backends.postgresql
DEFAULT_DB_NAME=propertyDB
DEFAULT_DB_USER=admin
DEFAULT_DB_PASSWORD=admin
DEFAULT_DB_HOST=localhost
DEFAULT_DB_PORT=5432

# Ollama Configuration
OLLAMA_MODEL_NAME=rewrite
OLLAMA_CLIENT_PORT=8000
```

Replace the placeholders with your actual database credentials and Ollama configuration.

### Make Migrations

Before running the project, ensure that all migrations are applied to the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### CLI Commands

The project includes several CLI commands for interacting with property data. These commands are designed to update content using the Ollama model.

#### Main Command: `update_content`

This is the primary command used to manage content updates. It has two subcommands:

1. **`rewrite`**: Rewrites the title and description for all properties in the database.
2. **`summarize`**: Summarizes the description for all properties and stores the summary in the database.

#### Subcommands and Their Purpose

- **`rewrite`**: 
  - Purpose: This command rewrites the `title` and `description` fields of all properties using the Ollama model.
  - Usage:
  
    ```bash
    python manage.py update_content rewrite
    ```
  
- **`summarize`**: 
  - Purpose: This command generates a summary of the `description` field for all properties and stores it in the `Summary` table.
  - Usage:
  
    ```bash
    python manage.py update_content summarize
    ```

### How to Use the Commands

To use the commands, simply execute them from the root directory of the `LLM_Assignment` project (where the `manage.py` file is located).

**Example:**

```bash
# Rewrite titles and descriptions for all properties
python manage.py update_content rewrite

# Summarize descriptions for all properties
python manage.py update_content summarize
```

These commands will process all records in the `Hotel` table and perform the respective operations as described.
