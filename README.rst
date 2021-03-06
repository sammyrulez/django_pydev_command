===============================
Django PyDev Management Command
===============================

This is a Djnago app that adds a managment command to create the required files to open your Django project with a PyDev powered Eclipse.

.. image:: https://travis-ci.org/sammyrulez/django_pydev_command.png?branch=master



************
Intsallation
************

**Option one:**
Clone this repo

``git clone https://github.com/sammyrulez/django_pydev_command.git``

and install in your enviroment

``python setup.py install``

**Option two:**

Use pip

``pip install -e git+https://github.com/sammyrulez/django_pydev_command.git#egg=django_pydev_command``

Then add the app to the installed apps in your setings.py

``INSTALLED_APPS = (...,'pydev',)``



*****
Usage
*****

From your project folder

``python manage.py eclipse interpeter_name python_version``

where

1. **interpeter_name** is the name of a python interpeter enviroment defined in the eclipse target workspace

2. **python_version** is the verscion of the python interpeter you are going to use

Other options are:

- **target_path** where the eclipse project file are going to be created

- **related-projects** projects in the target eclipse workspace you want to add to this project PYTHON_PATH

- **--src** adopt the "source folder" pydev convention ( all source files of the application in a folder named ''src'')



Notes
=====

I created this because I hate to commit IDE related files ( and I hate to find repos with those file already there)

Tested on Windows and OSX, Eclipse Juno Service Release 2, PyDev 2.7.3

Code coverage:

========================================= ========= ========= ====== =======
Name                                      Stmts     Miss      Cover  Missing
========================================= ========= ========= ====== =======
__init__.py                                   -        -         -   
management\__init__.py                        -        -         -   
management\commands\__init__.py               -        -         -   
management\commands\eclipse.py               61        -       100%  
management\commands\resources\__init__.py      -        -         -   
**TOTAL**                                    61        -       100%  
========================================= ========= ========= ====== =======




