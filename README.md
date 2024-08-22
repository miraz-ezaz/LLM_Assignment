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

### Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. Here's how to create and activate a virtual environment:

1. **Create a Virtual Environment**:

   ```bash
   python3 -m venv env
   ```

   This will create a new directory named `env` containing the virtual environment.

2. **Activate the Virtual Environment**:

   - On **Linux/MacOS**:

     ```bash
     source env/bin/activate
     ```

   - On **Windows**:

     ```bash
     .\env\Scripts\activate
     ```

   Once activated, your terminal prompt should change to indicate that the virtual environment is active.

### Install Project Dependencies

With the virtual environment activated, install the project dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install all necessary packages required for the project.

### Create the `.env` File

The `.env` file is required to store environment-specific variables, such as database configurations and Ollama model settings. Create a `.env` file inside the `propertyAI` folder.

Here’s a sample content for the `.env` file:

```env
# Default Database Configuration
DEFAULT_DB_ENGINE=django.db.backends.postgresql
DEFAULT_DB_NAME=your_database_name
DEFAULT_DB_USER=your_database_username
DEFAULT_DB_PASSWORD=your_database_password
DEFAULT_DB_HOST=your_database_host
DEFAULT_DB_PORT=your_database_port

# Ollama Configuration
OLLAMA_MODEL_NAME=your_ollama_model_name
OLLAMA_CLIENT_PORT=your_ollama_client_port
```

Replace the placeholder values with your actual configuration:

- **`DEFAULT_DB_ENGINE`**: The database engine Django should use (e.g., `django.db.backends.postgresql`).
- **`DEFAULT_DB_NAME`**: The name of your PostgreSQL database.
- **`DEFAULT_DB_USER`**: The username for your PostgreSQL database.
- **`DEFAULT_DB_PASSWORD`**: The password for your PostgreSQL database.
- **`DEFAULT_DB_HOST`**: The host of your PostgreSQL database (e.g., `localhost`).
- **`DEFAULT_DB_PORT`**: The port on which your PostgreSQL database is running (e.g., `5432`).

- **`OLLAMA_MODEL_NAME`**: The name of the Ollama model you are using (e.g., `rewrite`).
- **`OLLAMA_CLIENT_PORT`**: The port on which the Ollama client is running (e.g., `8000`).

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