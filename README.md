# Flask Web Application
This project is a Flask-based web application that uses SQLAlchemy for database management, Flask-Login for user authentication, and various custom forms for handling user input. The application allows users to manage notes, tags, and portfolios while ensuring secure user login and registration functionality.
## How to Run
**Step 1: Clone this repository:**
   ```bash
   git clone https://github.com/Anandaa69/Flask_Project.git
   cd Flask_Project
   ```
**Step 2: Create and activate Virtual Environment**
   ```bash
   python3 -m venv venv
   ```
   - **if you use Window**
   ```bash
   venv\Scripts\activate
   ```
   - **if you use Linux**
   ```bash
   source ./venv/bin/activate
   ```
**Step:4 Install Poetry:**
   ```bash
   pip install poetry
   ```
**Step 5: Install dependencies with Poetry**
   ```bash
   poetry install
   ```
**Step 6: Run Web:**
   ```bash
   poetry run python port_web/portapp.py
   ```

# Application Structure
Here’s a quick overview of the core components of the project:

- **portapp.py**: This is the main entry point for the Flask application. It contains all the route handlers, user authentication, and business logic for managing accounts, notes, and tags.

- **models.py**: This file defines the database models using SQLAlchemy. The **User**, **Role**, **Note**, and **Tag** models are defined here, along with many-to-many relationships for users and roles, and notes and tags.

- **forms.py**: This file contains the form classes, leveraging WTForms. It defines the form fields for registering users, logging in, creating notes, and managing tags. Custom form fields (like **TagListField**) are also used to handle special data types (e.g., lists of tags).

**auth.py**: Contains authentication-related logic, including role-based access control (ACL), which ensures that only authenticated users can access certain pages.

Main Features:
- **User Authentication**: Users can register, log in, and log out.
- **Role Management**: Users can be assigned roles (like "user" "admin"), and access can be controlled based on these roles.
- **Notes & Tags**: Users can create, update, and delete notes, and tags can be assigned to each note.
- **Portfolio Pages**: Different portfolio pages (port_1, port_2, etc.) display notes based on their associated portfolio IDs.