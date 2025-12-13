# Todo API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?style=for-the-badge&logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)

A scalable RESTful API built with **FastAPI** and **PostgreSQL**. This project demonstrates backend architecture using standard CRUD operations, database migrations and strict data validation.

## Key Features

-   **Full CRUD Operations:** Create, Read (All & By ID), Update and Delete tasks.
-   **Smart Updates:** Implementation of `PATCH` method for partial updates (specifically for toggling the `is_complete` status).
-  **Due Dates:** Implementation of datetime sorting to prioritize tasks.
-   **Subtasks:** Relational mapping to allow nested tasks (One-to-Many).
-   **Data Validation:** Strict schema validation using **Pydantic V2**.
-   **Database Persistence:** robust data storage using **PostgreSQL**.
-   **ORM Layer:** Clean database interaction using **SQLAlchemy**.
-   **Migrations:** Database schema version control using **Alembic**.
-   **Modular Architecture:** Codebase organized into distinct layers (Routers, CRUD, Models, Schemas) for maintainability.

## Tech Stack

-   **Framework:** FastAPI
-   **Database:** PostgreSQL
-   **ORM:** SQLAlchemy
-   **Migrations:** Alembic
-   **Serialization/Validation:** Pydantic
-   **Server:** Uvicorn (ASGI)

## Project Structure

This project follows a modular pattern to ensure scalability and separation of concerns:

```text
├── alembic/                # Database migration scripts
├── crud/
│   └── todo_crud.py        # Database interaction logic (Create, Read, Update, Delete)
├── database/
│   └── connections.py      # Database session and connection setup
├── models/
│   └── todo_model.py       # SQLAlchemy database models
├── schema/
│   └── todo_schema.py      # Pydantic models for request/response validation
├── routers/
│   └── todo_router.py      # API Endpoint definitions
├── main.py                 # Application entry point
├── .env                    # Environment variables (Database credentials)
└── alembic.ini             # Alembic configuration
```

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

-   Python 3.10+
-   PostgreSQL installed and running

### 1. Clone the repository

```Bash
git clone https://github.com/rhoda-lee/Todo-App.git
cd your-repo-name
```

### 2. Create a Virtual Environment

```Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```Bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your PostgreSQL credentials:

```Bash
DATABASE_URL=postgresql://username:password@localhost:5432/your_database_name
```

**Note:** Make sure to create the database in PostgreSQL before running migrations.

### 5. Run Database Migrations

Use Alembic to create the tables in your database:

```Bash
alembic upgrade head
```

### 6. Run the Server

```Bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000.`

## API Documentation

FastAPI provides automatic, interactive documentation. Once the server is running, visit:

-   Swagger UI: http://127.0.0.1:8000/docs
-   ReDoc: http://127.0.0.1:8000/redoc

## Endpoints Overview

| **Method** | **Endpoint**  | **Description**                     |
| :--------- | :------------ | :---------------------------------- |
| `GET`      | `/todos/`     | Retrieve all todo items             |
| `POST`     | `/todos/`     | Create a new todo item              |
| `GET`      | `/todos/{id}` | Retrieve a specific item by ID      |
| `PATCH`    | `/todos/{id}` | Update an item (e.g., mark as done) |
| `DELETE`   | `/todos/{id}` | Delete an item                      |

## Future Improvements

This project is currently in active development. Upcoming features include:

-   **Authentication:** User login and JWT token security.
-   **Tagging System:** Many-to-Many relationships for task categorization.

## Author

Rhoda Oduro-Nyarko

-   [GitHub Profile](https://github.com/rhoda-lee)
-   [LinkedIn Profile](https://www.linkedin.com/in/rhoda-oduro-nyarko/)

##

Built with ❤️ using Python and FastAPI.
