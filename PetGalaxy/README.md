# PetGalaxy - Online Pet Store

A complete full-stack e-commerce website for a pet store, built with Django, Bootstrap 5, and SQLite.

## Features
- User Authentication (Register, Login, Logout)
- User Profile and Address Management
- Product Categories (Dogs, Cats, Rabbits, Birds, Fish)
- Session-based Shopping Cart (accessible without login)
- Checkout and Order Management
- Order History
- Search and Filtering
- Soft Neon Theme with subtle animations
- Fully responsive design

## Installation Steps

1. **Clone or download the project** to your local machine.

2. **Open the project folder** in your terminal.

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser** (Admin):
   ```bash
   python manage.py createsuperuser
   ```
   *(Default Admin credentials placeholder: admin / admin)*

8. **Seed the database** with sample categories and products:
   ```bash
   python manage.py seed_data
   ```

9. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

10. **Open the application** in your browser at `http://127.0.0.1:8000/`.

## Screenshots
*(Placeholders for screenshots)*
- Splash Screen
- Home Page
- Product Listing
- Shopping Cart
- Checkout
