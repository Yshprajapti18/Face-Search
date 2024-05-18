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

![Screenshot 2024-05-14 195313](https://github.com/Yshprajapti18/Face-Search/assets/128960060/156fd5be-df49-48c2-8ca7-0c707e5ac6f5)


1. **Hosting a Room:**
 ![Screenshot 2024-05-14 194005 - Copy](https://github.com/Yshprajapti18/Face-Search/assets/128960060/bda20194-f9cf-4ef3-ba6b-5792cd74070e)
  
    - Log in to the application.
    - Navigate to the "Host Room" section.
    - Follow the instructions to create and host a new room.

2. **Searching for Images:**
![Screenshot 2024-05-14 194619](https://github.com/Yshprajapti18/Face-Search/assets/128960060/b40a6981-f473-4e92-9c42-4719794c100f)

    - After hosting a room, navigate to the "Search" section.
    - Upload an image to perform a facial recognition search within the hosted room.

![Screenshot 2024-05-14 195313](https://github.com/Yshprajapti18/Face-Search/assets/128960060/4f853165-4c82-4385-83db-29e862db67fe)

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).

---

Thank you for using our Face Search Application!
