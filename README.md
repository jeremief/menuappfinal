![Alt text](/static/images/Screenshot.png?raw=true "Final result")

1. Description
--------------
This project is part of Udacity's Full Stack Developer Nanodegree. Its purpose is to implement a web application making use of all CRUD functionalities.


2. How to install
-----------------
To obtain the files in this directory, you can either fork the repository in your own directory or download a zip file to your own machine and extract it. Either way, you should have the unzipped folder on your machine to be able to run it.

You will need to install a few python packages to be able to run the website, most notably Flask and SQLAlchemy.

Using your command line tool, navigate to the folder containing the application.

Your folder should contain six files and two folders called "Static" and "Templates".

1. database_setup.py: sets up the SQLite database used by the Flask application 
2. lotsofmenus.py: used to populate the newly created database
2. finalProject.py: powers the actual application and handles all the url routing
3. README.md: a copy of this document.
4. database_connection_setup.py: a short script that you can use in the command line tool to connect and query the database without accessing the application.
5: restaurantmenu.db:a copy of the database at the time of commit. Feel free to discard it you will be ceating your own in a moment.

The "Static" folder contains all the scripts, css files and picture files used in the application
The "Template folder": conatins all the html templates.


3. How to get started
---------------------
To get started, you need to do the following four steps in your command line:
- Create the database by running 
`>>> python database_setup.py`
- Populate the database with some starting entries 
`>>> python lotsofmenus.py`
- Launch the virtual server running the application:
`>>> python finalProject.py`
- Open your browser on local host on the port 5000: localhost:5000/restaurants

4. Issues and known bugs
------------------------

5. More information
--------------------

6. Licence
----------

7. About
--------