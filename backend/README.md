# Platform for students and tutors
## Local build

Clone this repo by using
```
git clone https://github.com/mshnschnko/BigLab.git
```
### Backend

Everywhere here we assume we are in the `backend` directory
```
python -m venv .venv
.\.venv\Scripts\activate
```
Install all the dependencies by executing:
```
pip install -r requirements.txt
```
Create `backend_project/backend_project/secrets.py` file containing:
```
SECRET_KEY = 'YOUR SECRET KEY'
```
Then import this variable into `backend_project/backend_project/settings.py`
### Database

Create your own database (SQLite, MySQL, PostgreSQL, etc) and modify `backend_project/backend_project/settings.py`:
```
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'APIdb',
		'USER': 'postgres',
		'PASSWORD': '87878987',
		'HOST': '127.0.0.1',
		'PORT': '5432'
	}
}
```
Set your dbname, user, password, host and port. This application is stable with the PostgreSQL and SQLite3.
### Migrations
Run the following code after each database change:
```
python backend_project/manage.py makemigrations
python backend_project/manage.py migrate
```
### Starting the server
To start the development server run the following:
```
python backend_project/manage.py runserver
```
If everything is ok, you will see:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 12, 2022 - 15:40:01
Django version 4.1.2, using settings 'backend_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
