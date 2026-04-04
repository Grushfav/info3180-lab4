# INFO3180 Lab 4: File Uploads with Flask
### Gavin Seaton -620043505

This lab demonstrates how to build a Flask application that supports **file uploads**, secure storage, and listing of uploaded images. It integrates Flask-WTF for form handling, Flask-Login for authentication, and uses `secure_filename()` to ensure safe file saving.

---

## Features
- User authentication (login/logout with Flask-Login).
- Upload images (`.jpg`, `.png`) via a secure form.
- Store files in a configured `UPLOAD_FOLDER`.
- List uploaded images in a responsive grid layout.
- Serve uploaded files via `/uploads/<filename>`.
- Navigation menu with conditional login/logout links.

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Grushfav/info3180-lab4.git
   cd info3180-lab4

2. Create and activate a virtual environment
    ```
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies
    ```
    pip install -r requirements.txt

4. Database setup
    ```
    flask db init
    flask db migrate
    flask db upgrade

5. Create User- Open Flask Shell
    ```
    from app import db
    from app.models import UserProfile

    user = UserProfile(
    first_name="YourFirstName",
    last_name="YourLastName",
    username="someusername",
    password="somepassword")

    db.session.add(user)
    db.session.commit()
    quit()

Set up .env file
```
FLASK_DEBUG=True
FLASK_RUN_PORT=8080
FLASK_RUN_HOST=0.0.0.0
SECRET_KEY= secret_key
UPLOAD_FOLDER= 
DATABASE_URL=postgresql://username:password@localhost/databasename

```


# File Structure

**Routes**
    /upload → Upload a new image file.

    /files → List all uploaded images in a grid.

    /uploads/<filename> → Serve a specific uploaded file.

    /logout → Log out the current user.

**Templates**
    upload.html → File upload form.

    files.html → Displays uploaded images in a grid using CSS Grid.

    header.html → Navigation bar with conditional login/logout and “View Images” link.

**Stap Shot**
![Upload Form Screenshot](app/static/Image/Screenshot.png)
