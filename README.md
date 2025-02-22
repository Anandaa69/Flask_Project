# Flask Web Application
This project is a Flask-based web application that uses SQLAlchemy for database management, Flask-Login for user authentication, and various custom forms for handling user input. The application allows users to manage notes, tags, and portfolios while ensuring secure user login and registration functionality.
## How to Run
**1. Clone this repository:**
   ```bash
   git clone https://github.com/Anandaa69/Flask_Project.git
   cd Flask_Project
   ```
**2. Create and activate Virtual Environment**
   ```bash
   python3 -m venv venv
   ```
   **- if you use Window**
   ```bash
   venv\Scripts\activate
   ```
   **- if you use Linux**
   ```bash
   source ./venv/bin/activate
   ```
**4. Install Poetry:**
   ```bash
   pip install poetry
   ```
**5. Install dependencies with Poetry**
   ```bash
   poetry install
   ```
**6. Run Web:**
   ```bash
   poetry run python port_web/portapp.py
   ```