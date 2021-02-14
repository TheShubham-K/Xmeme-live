## Xmeme

A web application for memer's

## Teach Stack

- Python Django framework for API's
- Bootstrap 4 for customizing the application
- Postgresql for database
- Docker for containerizing
- Heroku for front deployment
- Heroku-Postgres for publishing the database online


## setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/TheShubham-K/Xmeme-live.git
$ cd crio_xmeme
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ env\Scripts\activate
```


Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

make a .env file in the crio_xmeme project directory `(not in the root directory)` and save your ``SECRET_KEY`` in it in the following way :
```sh 
SECRET_KEY=your_secret_key
```


Once `pip` has finished downloading the dependencies and finished setting .env file.

```sh
(env)$ cd crio_xmeme
```

Download postgresql in your machine and also install pgAdmin 4 for postgresql.

```sh
https://www.pgadmin.org/download/pgadmin-4-windows/
```
After u have finished installing follow these instructions for migrating the database.

open terminal and navigate to the project directory and activate your virtual environment.

```sh
python manage.py migrate 
```

this will create a new database for your local machine.

```sh
python manage.py runserver 
```

and this will start the server locally in your machine.


These are the list of API routes to navigate through.

```sh
http://localhost:8081/  # Memes Stream List
http://localhost:8081/memes/  # Memes Stream json List 
http://localhost:8081/memes/<id>/ # to a particular meme with id (place the id of the meme in place of <id> in integer number format)
http://localhost:8081/memes-form/ # to add a new meme in the memes list
http://localhost:8081/memes-update/3/ # to update a meme.
```

