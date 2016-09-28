from sqlalchemy import Table, Column, Integer, String
from flask import Flask
from db import Db   # See db.py

app = Flask(__name__)
# The keys.json file should contain the 4 properties:
# DATABASE, PASSWORD, SERVER, SCHEMA
app.config.from_json('keys.json')

## Setting up database
db = Db(app.config)

#######################################
## ROUTES
## Here we specify the different routes

## First time someone visits the site. They should be shown options for creating
## a new user or logging in as a new user
@app.route('/', methods = ['GET'])
def index():
    pass

## Get user information. Should provide links to various tasks like
## looking at sent messages or received messages or creating a new message
@app.route('/user/<username>', methods = ['GET'])
def user_page(username):
   pass

## Creates a new user. Request body contains the password to be used
## If user/password exists, must ensure it is same or else throw error
@app.route('/user/<username>', methods = ['PUT'])
def user_create(username):
   pass

@app.route('/user/<username>', methods = ['DELETE'])
def user_delete(username):
   pass

## Returns information about a user's messages. We should allow complex
## queries here
@app.route('/user/<username>/messages', methods = ['GET'])
def user_messages(username):
   pass

## Used to post a new message. Body contains information about recipient
@app.route('/user/<username>/messages', methods = ['POST'])
def user_new_message(username):
   pass

## Get a particular message
@app.route('/messages/<id>', methods = ['GET'])
def message_get(id):
   pass

## Change a read status of a message
@app.route('/messages/<id>', methods = ['POST'])
def message_mark_read(id):
   pass

## Delete a message
@app.route('/messages/<id>', methods = ['DELETE'])
def message_remove(id):
   pass

## Get whether a given tag is in place for this message
@app.route('/messages/<id>/tags/<tag>', methods = ['GET'])
def tag_check(id, tag):
   pass

## Adds a tag to a message, if it did not exist
@app.route('/messages/<id>/tags/<tag>', methods = ['PUT'])
def tag_add(id, tag):
   pass

## Removes a tag from a message
@app.route('/messages/<id>/tags/<tag>', methods = ['DELETE'])
def tag_remove(id, tag):
   pass


#####################################

## Starts the application
if __name__ == '__main__':
   app.run()
