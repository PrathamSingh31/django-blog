# 📰 Django Blog Project
This is a personal blog web application built with Django. 
It includes user authentication, profile management, image uploads, and full CRUD functionality for blog posts. 
This project was developed by following Corey Schafer's Django tutorial series and customizing it along the way to suit my learning and development goals.

## 🔍 Features

- 👤 User Registration, Login, Logout, and Password Reset
- 📝 Create, Edit, and Delete Blog Posts
- 👀 View All Posts or Filter by Author
- 📷 User Profile with Image Upload
- 🧼 Django Crispy Forms (with Bootstrap 4)
- 🖼 Post thumbnails using `ImageField` and Pillow
- 📚 Pagination and basic search functionality
- 🔐 Admin Panel for managing content

---

## 🛠️ Technologies Used

- Python 3.11+
- Django 5.2.4
- SQLite (default, easy to set up)
- Bootstrap 4 for UI
- Pillow (for image handling)
- django-crispy-forms
- crispy-bootstrap4

---
## 🚀 Getting Started

### 1. Clone the Repository


git clone https://github.com/PrathamSingh31/django-blog.git
cd django-blog

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
# Apply Migrations
python manage.py migrate
# Run the Server
python manage.py runserver
Then go to: http://127.0.0.1:8000

📁 Project Structure
myproject/
├── blog/               # Main blog app
├── users/              # User accounts & profiles
├── static/             # Static files (CSS, JS)
├── media/              # Uploaded images
├── templates/          # HTML templates
├── myproject/          # Project settings and URLs
├── db.sqlite3          # Database
├── manage.py
├── requirements.txt
└── README.md

# 🙋‍♂️ About Me
I'm Pratham, a budding Django developer learning by building real-world applications.
You can check out more of my work here:
GitHub: https://github.com/PrathamSingh31
LinkedIn: https://linkedin.com/in/prathamsingh31

