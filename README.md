# DSP_Project
This project is an online examination system.

To run the software your are required to fork the repository in your local device.
open the folder in your local machine

open a new terminal make your in the directory 
create an virtual envoroment and activate your virtual environment

python3 -m venv env  
source env/bin/activate 

install all the requirements using pip install commamd

then run these commands respectiveley

python manage.py makemigrations 

python manage.py migrate

python manage.py runserver 

to login as admin you will need to create a superuser login details
to do this you will need to run this command.

python manage.py createsuperuser

then create your login details