# Module Interaction Diagram for Burger House Project

## Overview
This document describes how the different modules in the Burger House project interact with each other to deliver the full stack functionality.

---

## Modules and Their Roles

1. **backend/app.py**
   - Main Flask application.
   - Defines API endpoints for reservations and orders.
   - Uses SQLAlchemy ORM for database operations.
   - Serves the frontend HTML template.
   - Can optionally use raw SQL functions from `raw_db.py`.

2. **backend/raw_db.py**
   - Provides raw SQL query functions as an alternative to SQLAlchemy.
   - Functions to insert and retrieve reservations and orders.
   - Can be imported and used by `app.py` or other modules.

3. **backend/static/main.js**
   - Frontend JavaScript.
   - Handles UI interactions like menu toggle, modal display.
   - Validates forms and sends API requests to backend endpoints.
   - Processes responses and updates UI accordingly.

4. **backend/templates/index.html**
   - Main HTML template rendered by Flask.
   - Contains the structure of the website including order modal and reservation form.
   - Links to CSS and JS static files.

5. **backend/static/style.css**
   - Stylesheet for the frontend UI.

6. **run_project.bat**
   - Batch script to automate environment setup and running the Flask app.

7. **backend/requirements.txt**
   - Lists Python dependencies.

---

## Interaction Flow

- **User** interacts with the **frontend UI** (index.html + main.js + style.css).
- **main.js** captures user actions and sends HTTP requests to **Flask API endpoints** in **app.py**.
- **app.py** processes requests, performs validation, and interacts with the **database** via:
  - SQLAlchemy ORM methods, or
  - Raw SQL functions from **raw_db.py** (optional).
- Database changes or queries are executed on the SQLite database file.
- Responses are sent back to **main.js**, which updates the UI accordingly.

---

## Diagram (Textual)

```
+----------------+        +----------------+        +-----------------+
| Frontend (JS,  | <----> | Flask Backend  | <----> | SQLite Database |
| HTML, CSS)     |        | (app.py)       |        | (reservations.db)|
+----------------+        +----------------+        +-----------------+
         |                        |                         |
         |                        |                         |
         |                        |                         |
         |                        |                         |
         |                        |                         |
         |                        |                         |
         +------------------------+-------------------------+
                                  |
                           Optional use of
                           raw_db.py for
                           raw SQL queries
```

---

If you want, I can help you create a graphical version of this module interaction diagram.

Let me know if you want me to proceed with that or provide any further details.
