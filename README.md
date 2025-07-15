# Burger House Project

## Overview
Burger House is a web application for a burger restaurant that allows customers to view the menu, make table reservations, and place food orders online. The backend is built with Flask and uses SQLite for data storage. The frontend is a responsive website with interactive UI elements.

## Features
- View burger menu and special offers
- Book a table reservation with date, time, and number of people
- Place food orders with customer details and selected burger
- Responsive design with animations and modal order form
- REST API endpoints for reservations and orders

## Technologies Used
- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5, CSS3, JavaScript
- ScrollReveal.js for animations
- Remix Icon for icons

## Setup Instructions

1. Clone the repository or download the project files.

2. Navigate to the backend directory:
   ```
   cd Burger_House/backend
   ```

3. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
   ```

4. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the Flask application:
   ```
   python app.py
   ```

6. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
- Use the navigation menu to explore different sections.
- Use the reservation form to book a table.
- Click "ORDER NOW" on any burger to open the order form modal.
- Fill in your details and submit the order.

## Notes
- The database file `reservations.db` is created automatically on first run.
- API endpoints:
  - POST `/api/reservation` - Create a new reservation
  - GET `/api/reservations` - Get all reservations
  - POST `/api/order` - Place a new order

## Future Improvements
- Add user authentication
- Add order history and management
- Improve UI/UX with better feedback and validation
- Deploy to a production server with HTTPS and security features

## License
This project is open source and free to use.
