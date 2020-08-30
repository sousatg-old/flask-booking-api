## Initial setup

Create a virtual env and install the dependencies with the following commands

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

To create the database we need to run the migrations

```
flask db update
```

## Run the App

```
flask run --reload --debugger
```
