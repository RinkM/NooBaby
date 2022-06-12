# NooBaby

An app to track and view the nutrition, sleep, and waste of infants.

## To Run NooBaby
Noob_Main.py starts the program.
NoobV2 is the same program, but code has been refactored into multiple files. 
Noob_Main_V2.py runs the 2nd version.

You MUST create a profile to access the app. There is an option to skip the username / password page. It uses a test account to access the app.  It may not work on another computer.

Requires installation of Custom Tkinter in order to view the GUI. More info here : https://github.com/TomSchimansky/CustomTkinter

To install, use : pip3 install customtkinter
Also uses : tkCalender and sqlite3. I don't think they need to be installed.

This is a work in progress. As such, not all features are working or in their final form.

## What works : 
* Creation of SQL relationship database.
* Create, access, store, and modify user-data.
* Allow user to input food, sleep and diaper changes as they happen. 
* GUI Interface
* Tkinter / CTkinter Wigits

## Upcoming Goals
* Display this information in a way similar to Fitbit or Apple health. 
* Use Matplotlib and other modules to visualize the data
* Allow for editing profile information
* Track milestones, growth, height, other information.
* Build a resource library to 
* Adjust the app as the child grows older.  
* Enter food and track macro-nutritional data from US GOV API.



Learning Goals : Create GUI interface, accept user data, store data using relationship database SQL, retreive this data and visually represent it, username / password creation and verification, learn to write cleaner code, practice passing arguments through functions, work on documenting code so it is easier to read, practice importing files, represent DATETIME, eventually post on-line using django or other framework.