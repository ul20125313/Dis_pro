# loyalty_cards
loyalty cards

### Quick Start
To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment

2. Run the following commands

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

3. Open a browser and go to http://localhost:8000/

4. Function:
- Generator to Card go '/gen-card/'
- Change Status to Card go 'card_id/change-status/'
- Profil Card '/card_id/'
- Delete to Card go '/card_id/delete/'
