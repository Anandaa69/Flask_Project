# Flask Web Application
This project is a **Flask-based portfolio website** designed to showcase personal projects and allow user interaction through a secure login system. The application enables users to register, log in, and leave comments on various portfolio items, fostering engagement and feedback.

To ensure a seamless and secure experience, the project integrates **Flask-Login** for authentication, **SQLAlchemy** for efficient database management, and **WTForms** for handling user input. The website provides an intuitive interface where users can explore different portfolio pieces and share their thoughts through a structured commenting system.

With a focus on usability and security, this application also implements **role-based access control** to differentiate user permissions, ensuring that administrative tasks such as comment moderation and content management are restricted to authorized users.

In addition to authentication and user interaction, the project includes a tagging system that allows notes and comments to be categorized effectively. The database schema is designed to support scalability, enabling future expansion with additional features such as image uploads, search filters, and customizable portfolio layouts.

This project serves as a **personalized, interactive portfolio platform** that not only highlights creative works but also encourages meaningful user engagement in a structured and secure environment.
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
**Step 3: Install Poetry:**
   ```bash
   pip install poetry
   ```
**Step 4: Install dependencies with Poetry**
   ```bash
   poetry install
   ```
**Step 5: Run Web:**
   ```bash
   poetry run python port_web/portapp.py
   ```

# Web Application Structure
Here’s a quick overview of the core components of the project:

- **portapp.py**: This is the main entry point for the Flask application. It contains all the route handlers, user authentication, and business logic for managing accounts, notes, and tags.

- **models.py**: This file defines the database models using SQLAlchemy. The **User**, **Role**, **Note**, and **Tag** models are defined here, along with many-to-many relationships for users and roles, and notes and tags.

- **forms.py**: This file contains the form classes, leveraging WTForms. It defines the form fields for registering users, logging in, creating notes, and managing tags. Custom form fields (like **TagListField**) are also used to handle special data types (e.g., lists of tags).

**auth.py**: Contains authentication-related logic, including role-based access control (ACL), which ensures that only authenticated users can access certain pages.

Main Features:
- **User Authentication**: Users can register, log in, and log out.
- **Role Management**: Users can be assigned roles (like "user", "admin"), and access can be controlled based on these roles.
- **Notes & Tags**: Users can create, update, and delete notes, and tags can be assigned to each note.
- **Portfolio Pages**: Different portfolio pages (port_1, port_2, etc.) display notes based on their associated portfolio IDs.

### Folder Structure
```
Flask_Project/ 
│
├── instance
│   ├── database.db                # SQLite database file used to store data for the application.
│
├── port_web/                      # Main web application folder containing the logic and structure of the web app.
│   ├── portapp.py                 # Main application file for running the Flask app. It sets up the routes and runs the server.
│   ├── templates/                 # Folder for HTML templates that render content for different pages in the web app.
│   │   ├── about_me.html          # A page template about the user or application.
│   │   ├── base.html              # Base template that other pages extend, containing common elements like header/footer.
│   │   ├── create_note.html       # Template for creating new notes.
│   │   ├── login.html             # Login page template for user authentication.
│   │   ├── main.html              # Main landing page template of the web app.
│   │   ├── manage_account.html   # Template for managing user account details.
│   │   ├── port1.html, port2.html, port3.html, port4.html  # Different page templates for various port views.
│   │   ├── ports.html             # Template that displays a list of all ports.
│   │   ├── register.html         # User registration page template.
│   │   ├── tags_view.html        # Page for viewing and managing tags.
│   │   ├── update_note.html      # Template for editing/updating a note.
│   │   ├── update_tags.html      # Template for editing/updating tags.
│   ├── static/                    # Folder for static files like images, fonts, CSS, and JavaScript.
│   │   ├── fonts                  # Folder containing font files.
│   │   └── images/                # Folder containing image files used in the web app.
│   ├── models/                    # Folder for database models that define the structure of your data.
│   │   ├── __init__.py            # Initializes the models package.
│   │   ├── models.py              # Defines all the database models like User, Role, Note, Tag, etc.
│   ├── forms/                     # Folder for forms related to user input.
│   │   ├── forms.py               # Contains form classes such as LoginForm, RegisterForm, etc.
│   └── auth/                      # Folder for authentication logic and access control.
│       ├── __init__.py            # Initializes the authentication package.
│       └── acl.py                 # Access control and authentication logic (e.g., roles and permissions).
│
├── venv/                          # Virtual environment folder to isolate the Python environment and dependencies.
│   ├── ...                        # Virtual environment files (e.g., site-packages, Python binaries).
│
├── .gitignore                     # Specifies files and directories that Git should ignore (e.g., `venv/`, `.pyc` files).
├── poetry.lock                    # Poetry lock file for ensuring consistent dependencies across environments.
├── pyproject.toml                 # Configuration file for Poetry, defining project dependencies and metadata.
└── README.md                      # The README file containing project documentation, setup instructions, and usage.
```