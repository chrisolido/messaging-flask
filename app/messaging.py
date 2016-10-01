## messaging.py
##
## Start the application by running `python3 app/messaging.py`
##
from sqlalchemy import Table, Column, Integer, String
from flask import Flask, make_response, json, url_for, request
from db import Db   # See db.py
# import user # See user.py
import message # See message.py

app = Flask(__name__)
# The keys.json file should contain the 4 properties:
# DATABASE, PASSWORD, SERVER, SCHEMA
app.config.from_json('keys.json')
app.config['DEBUG'] = True  # Turn this to True to enable debugging


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
@app.route('/users/<username>', methods = ['GET'])
def user_page(username):
   return make_json_response({
      'user': username,
      'sent': url_for('user_messages', username=username, include='sent'),
      'received': url_for('user_messages', username=username, include='received'),
      'create': {
         'url': url_for('user_new_message', username=username),
         'content': { 'recipient': '', 'title': '', 'body': '' }
      }
   }, 200)

## Creates a new user. Request body contains the password to be used
## If user/password exists, must ensure it is same or else throw error
## In first iteration of the app, no passwords.
@app.route('/users/<username>', methods = ['PUT'])
def user_create(username):
   if len(username) > 20:
      return make_json_response({ 'error': 'long username' }, 400)
   return make_json_response({}, 201, {
      'Location': url_for('user_page', username=username)
   })

@app.route('/users/<username>', methods = ['DELETE'])
def user_delete(username):
   pass

## Returns information about a user's messages. We should allow complex
## queries here
@app.route('/users/<username>/messages', methods = ['GET'])
def user_messages(username):
   args = request.args.to_dict()
   error = message.validate_message_query(args, username)
   if error is not None:
      return make_json_response({ 'error': error }, 400)
   results = db.get_messages(args, username)
   return make_json_response({
      'messages': [
         { 'url': url_for('message_get', id=m['id']) }
         for m in results
      ]
   }, 200)

## Used to post a new message. Body contains information about recipient
## - Validate the message
## - Add to database
@app.route('/users/<username>/messages', methods = ['POST'])
def user_new_message(username):
   contents = request.get_json()
   contents['from'] = username
   error = message.validate_new_message(contents)
   if error is not None:
      return make_json_response({ 'error': error }, 400)
   record_id = db.write_message(contents)
   if record_id is None:
      return make_json_response({ 'error': 'Internal Server Error' }, 500)
   return make_json_response({}, 201, {
      'Location': url_for('message_get', id=record_id)
   })

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
## Helper methods go here

## Helper method for creating JSON responses
def make_json_response(content, response = 200, headers = {}):
   headers['Content-Type'] = 'application/json'
   return make_response(json.dumps(content), response, headers)


#####################################

## Starts the application
if __name__ == '__main__':
   app.run()
