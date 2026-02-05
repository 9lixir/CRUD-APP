##Flask CRUD Application with User Authentication

This is a Flask-based CRUD web application with user registration, login, session-based authentication, and PostgreSQL as the database.
Users must log in to access and manage items (Create, Read, Update, Delete).

Features
	•	User Registration (with password hashing)
	•	User Login & Logout
	•	Session-based authentication
	•	Protected routes (only logged-in users can access CRUD pages)
	•	Add, view, update, and delete items
	•	Dashboard showing logged-in user
	•	Bootstrap 5 responsive UI
	•	PostgreSQL database integration


Tech Stack
	•	Backend: Python (Flask)
	•	Frontend: HTML, Bootstrap 5
	•	Database: PostgreSQL
	•	Security: Werkzeug password hashing
	•	Session Management: Flask session
   
## How to Run the Project

1. Clone the repository
2. Create a PostgreSQL database named `crud_lab`
3. Create tables using the provided SQL file
4. Update database credentials in `app.py`
5. Run:
   python app.py
6. Open browser and go to:
   http://127.0.0.1:5000
