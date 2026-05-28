# Simple E-commerce Platform

A fully functional e-commerce website built with Django (Python), HTML, CSS, Bootstrap, and SQLite.

## Features

- **Product Management:** Add, edit, and categorize products via the Django admin panel.
- **Shopping Cart:** Add, remove, and adjust quantities of products in the cart without a page reload.
- **User Authentication:** Registration, login, and logout functionalities.
- **Checkout:** Finalize orders with shipping details.
- **User Profile:** Manage shipping details and view past order history.
- **Search & Filtering:** Search for products by name and filter by category.
- **Responsive Design:** Mobile-friendly UI using Bootstrap.

## Prerequisites

- Python 3.10+
- `pip` package manager

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd simple_ecommerce
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\Activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (for the admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the platform:**
   - Main site: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

- `simple_ecommerce/`: Project configuration (settings, core URLs).
- `store/`: The main Django app containing models, views, forms, and URL routes.
- `templates/`: HTML templates.
- `static/css/`: Custom styles.
- `media/`: Uploaded product images (created automatically upon uploading via admin).
