# twitoff-dspt4
Installation
TODO: instructions for git clone

Setup
TODO: instructions for virtual environment

Also setup a database:

FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
Usage
# Mac:
FLASK_APP=web_app flask run

# Windows:
export FLASK_APP=web_app # one-time thing, to set the env var
flask run
