# loyalty_cards
loyalty cards

### Quick Start
To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment

2. Run the following commands

add a .env file or write SECRET_KEY = os.urandom(24) #os.getenv('SECRET_KEY') in setting.py

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

3. Open a browser and go to http://localhost:8000/

4. Function:
all of functions can be found in urls.py
