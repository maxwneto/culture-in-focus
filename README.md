## Product Management App

### Overview

This repository contains a simple yet functional product management application built using the Django framework. The app allows users to add, view, and manage products efficiently. It's an excellent example for those looking to understand the basics of creating web applications with Django.

### Features

- **Add Products**: Users can add new products by filling out a form with the product's name, description, and price.
- **View Products**: A list of all added products is displayed, showing their names, descriptions, and prices.
- **User-friendly Interface**: The app features a clean and simple interface that makes it easy to navigate and use.

### Technical Details

- **Framework**: Django (Python)
- **Database**: SQLite (default configuration, easily switchable to other databases)
- **Templates**: HTML templates for rendering the user interface

### Functionalities

1. **Add Product**:
    - Accessible via the `/add_product/` URL.
    - A form where users can input the product's name, description, and price.
    - Form validation and error handling.

2. **View Product List**:
    - Accessible via the `/product_list/` URL.
    - Displays a list of all products with their details.

3. **Home Page**:
    - Accessible via the root URL (`/`).
    - Provides navigation links to add products and view the product list.

### Getting Started

#### Prerequisites

- Python 3.x
- Django 5.0.7

#### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/product-management-app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd product-management-app
    ```
3. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Apply the database migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Run the development server:
    ```sh
    python manage.py runserver
    ```
7. Open your web browser and go to `http://127.0.0.1:8000/` to use the application.

### Project Structure

- `prod_projeto/`: Main project directory.
  - `settings.py`: Configuration for the Django project.
  - `urls.py`: URL routing for the project.
- `produtos/`: Application directory.
  - `models.py`: Defines the `Produto` model.
  - `forms.py`: Defines the form for adding products.
  - `views.py`: Contains the logic for handling requests and rendering templates.
  - `urls.py`: URL routing for the application.
  - `templates/produtos/`: HTML templates for the application.
    - `home.html`: Template for the home page.
    - `add_product.html`: Template for the add product page.
    - `product_list.html`: Template for the product list page.

### Future Enhancements

- **Edit and Delete Products**: Implement functionality to edit and delete products.
- **Search and Filter**: Add search and filter capabilities to the product list.
- **User Authentication**: Implement user authentication to restrict access to certain features.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss changes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
