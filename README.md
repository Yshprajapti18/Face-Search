# Face Search Application

This is a Django-based face search application that allows users to host virtual rooms and search for their images through facial recognition within those rooms.

## Features

- Host virtual rooms for organizing images
- Search for images based on facial recognition within hosted rooms
- User-friendly interface

## Installation

Follow these steps to install and set up the application on your local machine.

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- Virtualenv

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/facesearch.git
    cd Face Hunter
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (for accessing the admin interface):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000` to use the application.

## Usage

1. **Hosting a Room:**
    - Log in to the application.
    - Navigate to the "Host Room" section.
    - Follow the instructions to create and host a new room.

2. **Searching for Images:**
    - After hosting a room, navigate to the "Search" section.
    - Upload an image to perform a facial recognition search within the hosted room.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).

---

Thank you for using our Face Search Application!
