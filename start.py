## Django is a python package for web development

## what we need to know about django
# installing django package using pip(python package manager) CMD used pip install django
"""
Identify a location on your computer where your going to keep your django projects 
(django-admin startproject myfirst)..."python -m django startproject myproject

"""


# from that location you create a django project
# frm your django project, you create a django app...
"""
django-admin startproject myfirst)..."python -m django startproject myproject
"""

# once you have created a django app you install the django app...
"""
 (python manage.py startapp fruits)
 For installing you go to the seettings.py file and under installed apps you add you project created.
"""
# after creating you create a super user
# start the server and check if everything is running properly..
"""
 python manage.py runserver
 incase you want to run it via a web browser ......localhost:8000, 127.0.0.1:8000
"""
# Package installer for python (pip)

##donot temper with the manage.py file because it has all the commands we need to develop the project
## The inner folder is the configuration folder
##settings.py and url.py is the configuration file
##asgi.py aint ours


#server communication
# get me this pageor index page the server responds wit 200 wc is oky
##404 is not found
## how the web server communicates witha client server
## we are going to use sqlite 3
# by default the database is named db.sqlite 3

## activate the db ()
"""
(creates user tables and other tables) python manage.py migrate
create a super user (python manage.py createsuperuser)
"""
## go and create a folder templates where your html is stored

"""

"""