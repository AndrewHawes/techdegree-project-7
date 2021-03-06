# Profile Project
This is the project 7 for the Python Web Development Techdegree program.
It's a simple site that allows users to create and edit a profile.

Among other things:
- Users can register for an account.
- Users can upload a profile image and edit it.
- Users can immediately view new and edited profile images on their edit 
page without having to submit the form.
- Users can use an embedded rich text editor to write and format a bio.
- Users have a password meter with interactive hints to help them create a 
password that meets the somewhat stringent password requirements for this site.

## Installation
*Two users are automatically provided when you initialize the database:*
- Normal Account
    - username: bob
    - password: Bartsimpson1234!
- Superuser Account
    - username: admin
    - password: pass  

1. Download the project and change into the project directory.
2. Create a new virtual environment 
    - Windows: `python -m venv env` 
    - Linux/Mac `python3 -m venv env`
3. Activate the virtual environment
    - Windows: `.\env\Scripts\activate`
    - Linux/Mac: `source env/bin/activate`
4. `pip install -r requirements.txt` to install the project dependencies.
   - Required JavaScript files are included with the download.
5. `python manage.py migrate` to initialize the database.
6. `python manage.py loaddata db.json` to load data.
6. `python manage.py runserver` to start the server on port 8000 (default).
7. Open [127.0.0.1:8000](127.0.0.1:8000) in your browser.

From here, you can use one of the existing accounts or create your own account and edit your profile.
