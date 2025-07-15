# Data Flow Diagram for Burger House Project

## Overview
This diagram describes the flow of data between the user, frontend, backend, and database in the Burger House full stack application.

---

## 1. User Interaction
- User interacts with the web interface via a browser.
- Actions include:
  - Browsing burger menu.
  - Clicking "ORDER NOW" buttons or banner cards.
  - Filling reservation form.
  - Submitting order form.

---

## 2. Frontend (HTML, CSS, JavaScript)
- Displays UI components and captures user input.
- JavaScript handles:
  - UI interactivity (menu toggle, modal display).
  - Form validation.
  - Sending HTTP requests to backend API endpoints (`/api/order`, `/api/reservation`).
- Receives responses and displays success/error messages.

---

## 3. Backend (Flask Application)
- Receives API requests from frontend.
- Validates input data.
- Uses SQLAlchemy ORM or raw SQL queries (via `raw_db.py`) to interact with the database.
- Performs CRUD operations:
  - Insert new reservations and orders.
  - Retrieve reservations/orders if needed.
- Sends JSON responses back to frontend.

---

## 4. Database (SQLite)
- Stores data in tables:
  - `reservation` table: stores reservation details (name, email, date, time, people).
  - `order` table: stores order details (student_name, student_id, item).
- Supports queries from backend ORM or raw SQL.

---

## Data Flow Summary

User --> Frontend UI --> API Request --> Backend Flask --> Database  
Database --> Backend Flask --> API Response --> Frontend UI --> User

---

## Diagram (Textual Representation)

```
+-------+       +----------+       +---------+       +----------+
| User  | <---> | Frontend | <---> | Backend | <---> | Database |
+-------+       +----------+       +---------+       +----------+
    |                |                |                 |
    |  Input/Click   |                |                 |
    |--------------->|                |                 |
    |                | Validate/Input |                 |
    |                |--------------->|                 |
    |                |                | Query/Insert    |
    |                |                |---------------> |
    |                |                |                 |
    |                |                |   Response      |
    |                |<---------------|                 |
    |                | Display Result |                 |
    |<---------------|                |                 |
```

---

If you want, I can help you create a graphical diagram using tools like draw.io or provide a more detailed technical diagram.

Let me know your preference.
