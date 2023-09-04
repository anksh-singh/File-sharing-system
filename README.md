# File-sharing-system



#Setup

Add the required Creds before anything in .env file
HOST_EMAIL=test@gmail.com 
HOST_EMAIL_APP_PASSWORD=xyz
FRONTEND_URL=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=

#Create & Activate virtualenvironment 
python3 -m venv myenv
source myenv\scripts\activate

#Install the project dependencies with:-
pip3 install -r requirements.txt

Now run the project with this command:-
python manage.py runserver


