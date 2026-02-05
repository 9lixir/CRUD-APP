## Flask CRUD Application with User Authentication

This is a Flask-based CRUD web application with user registration, login, session-based authentication, and PostgreSQL as the database.
Users must log in to access and manage items (Create, Read, Update, Delete).

Features
1. User Registration (with password hashing)
2. User Login & Logout
3. Session-based authentication
4. Protected routes (only logged-in users can access CRUD pages)
5. Add, view, update, and delete items
6. Dashboard showing logged-in user
7. Bootstrap 5 responsive UI
9. PostgreSQL database integration


Tech Stack
1. Backend: Python (Flask)
2. Frontend: HTML, Bootstrap 5
3. Database: PostgreSQL
4. Security: Werkzeug password hashing
5. Session Management: Flask session
   
## How to Run the Project

1. Clone the repository
2. Create a PostgreSQL database named `crud_lab`
3. Create tables using the provided SQL file
4. Update database credentials in `app.py`
5. Run:
   python app.py
6. Open browser and go to:
   http://127.0.0.1:5000
