# socialappbackend

## Installation

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv_name`.
3. Activate the virtual environment:
    - On Windows: `venv_name\Scripts\activate`
    - On macOS and Linux: `source venv_name/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`.
5. Configure environment variables (if applicable).
6. Apply database migrations: `python manage.py migrate`.
7. Start the development server: `python manage.py runserver`.

### Running the Development Server

To start the Django development server, run the following command:

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
#testing
python manage.py test