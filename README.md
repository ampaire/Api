[![Build Status](https://travis-ci.org/ampaire/Api.svg?branch=develop)](https://travis-ci.org/ampaire/Api)
# Api
this is a repository for creating code for creating Api endpoints.
# project build
The purpose of this project was to create Api endpoints for entries data structure. The endpoints were tested in postman.
The required endpoints were for:
*-get all entries
*-get one entry
*-add an entry
*-delete an entry
*-update/modify an entry
# Required tools
*-Server side Framework: <Flask Python Framework>
*-Linting Library: <Pylint, a Python Linting Library>
*-Style Guide: <PEP8 Style Guide>
*-Testing Framework: <PyTest, a Python Testing Framework>
  
  # Procedure
  Before doing anything you first open the folder where you are going to work in the text editor
 *To work on the project you first install a virtual environment by running
 *$pip install virtualenv
 
 *Later create the virtual environment by running the command in the terminal
 $virtualenv venv
 
 *To activate the virtualenv you need to run this command in the terminal for linux users
 *$source venv/bin/activate
 
 *Install flask by running the command below to install the flask module 
 *$pip install --user flask
 
 *install all the other require tools (pylint,auto pep8, pytest) using the command
 *$pip install <module>
  
 *Install Postman

The endpoints (in the app folder) were created in independent files each on its own github branch. The github branches were later merged to develop. Each feature has its own test framework in the tests folder.
Postman was used to test the endpoints for functionality

 
 
 
 
 

