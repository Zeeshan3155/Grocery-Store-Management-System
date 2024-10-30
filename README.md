
# Grocery Store Management System

A web-based grocery store management system built with the Django framework. This application allows users to manage products and orders in a streamlined way, enabling CRUD (Create, Read, Update, Delete) operations for products and viewing order details. The project includes dynamic frontend elements powered by HTML, CSS, and JavaScript, with MySQL as the database backend.


## Features

1. **Order Management**: View all orders and their details.
2. **Product Management**:
   * Add new products with attributes like name, price, and quantity.
   * Edit the name or price of existing products.
   * Delete products from the inventory.
3. **New Order Creation**: Add items to a new order, calculate the total, and save order details.
4. **Dynamic UI**: Interactive pages with JavaScript for enhanced user experience.


## Screenshots
## Demo

## Project Structure
The application consists of four main pages:

- **Orders**: Displays a list of all orders placed.
- **Order Details**: Shows detailed information about a selected order.
- **Product Details**: Lists all available products with options to add, edit, or delete.
- **New Order**: A form to create new orders, including product selection and quantity input.
## Technology Stack
- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Libraries**: 
  - Select2 for enhanced dropdowns in forms
  - Bootstrap (optional) for styling
## Setup  Instructions
1. **Clone the Repository**:
```bash
    git clone https://github.com/yourusername/grocery-store-management.git
   cd grocery-store-management
```

2. **Install Dependencies**: 
```bash 
    pip install -r requirements.txt
```

3. **Database Configuration**:
* Create a MySQL database named grocery_store_db.
* Update the DATABASES section in settings.py with your MySQL credentials.

4. **Migrate Database**:
```bash
    python manage.py makemigrations
    python manage.py migrate
```

 **Run the Server**:
```bash
python manage.py runserver
```
Access the application at http://127.0.0.1:8000.




# Hi, I'm Zeeshan! 👋
Explore more of my projects on my [Portfolio Website](https://zeeshan-ahmed.netlify.app/). 