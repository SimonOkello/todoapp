# TodoApp

ToDoApp is a simple Python/Django web app for a todo list.

You can `add`,`edit`, `mark as complete` and `delete` a task

## Setup

The first thing to do is to clone the repository:

```bash
git clone https://github.com/SimonOkello/todoapp.git
cd todoapp
```

## Create a virtual environment to install dependencies in and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```
## Then install the dependencies:

```bash
pip install -r requirements.txt
```
## Usage

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

http://127.0.0.1:8000/

```
## Technologies
- [Django 3.2](https://www.djangoproject.com/) |Back-end
- [Bulma](https://bulma.io/) |Front-end
- [PostgreSQL](https://www.postgresql.org/) |Database


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)