# Project

PyTaskManager is a lightweight task management application built with FastAPI, HTML, and Bootstrap 5. It allows users to manage their tasks by providing a user-friendly interface for adding, editing, and deleting tasks. The application utilizes an SQLite database to store task information, ensuring simplicity and ease of use.

#### Key Features:

-   Create, Read, Update, and Delete tasks seamlessly.
-   View tasks with details such as title, description, and status.
-   Filter tasks based on their status for better organization.
-   Responsive and intuitive user interface powered by Bootstrap 5.
    Efficient backend powered by FastAPI for quick API responses.

### Todo

-   [ ] Create an index.html file in a templates folder.
-   [ ] Design a simple interface using Bootstrap 5 for displaying tasks, adding new tasks, and editing existing tasks.
-   [ ] Link your HTML file to the FastAPI backend.
-   [ ] Use FastAPI's templates and static files support to render HTML and serve static assets.
-   [ ] Test your CRUD operations by running the FastAPI development server (uvicorn main:app --reload).
-   [ ] Use tools like curl or tools like HTTP Client extension to interact with your API.
-   [ ] Provide instructions on how to run the project.

### In Progress

### Done ✓

-   [x] Create a new project directory for your PyTaskManager.
        Project Setup:
-   [x] Set up a virtual environment: python -m venv venv
-   [x] Activate the virtual environment: source venv/bin/activate (Linux/macOS) or venv\Scripts\activate (Windows).
-   [x] Install FastAPI and SQLite libraries: pip install fastapi uvicorn(standard)
        databases
-   [x] Create an SQLite database file (e.g., tasks.db) in your project directory.
-   [x] Define a Task table with columns for id, title, description, and status.
-   [x] Create a main.py file for your FastAPI backend.
-   [x] Define FastAPI app and connect to the SQLite database using the databases
        library.
-   [x] Implement CRUD operations (Create, Read, Update, Delete) for tasks.
-   [x] Document your code, especially the API endpoints.
