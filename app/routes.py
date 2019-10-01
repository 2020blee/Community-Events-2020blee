import os
from app import app
from flask import render_template, request, redirect

username = "period8"

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"},
        {"event":"Summer Vacation", "date":"2020-06-03"}
    ]



from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:Wbwx6DdQOWZDhcMY@cluster0-6mvgj.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    #Connect to the mongo events database that you made
    events = mongo.db.events
    #Query all Events and stored them as myquery
    myquery = list(events.find({}))
    print("#############" *4)
    print(myquery)
    return render_template('index.html', myquery = myquery)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    test = mongo.db.test
    # insert new data
    test.insert({'name': 'last day of school'})
    # return a message to the user
    return "Added data to database!"

@app.route('/input')
def input():
    return render_template('input.html')


@app.route('/results', methods = ["get", "post"])
def results():
    #Storing user inputs as the variable userdata as a dictionary
    userdata = dict(request.form)
    print(userdata)
    #Stored the event name as a variable
    event_name = userdata['event_name']
    print(event_name)
    #Stored the event date as a variable, separate from event name
    event_date = userdata['event_date']
    print(event_date)
    #Connecting to events database
    events = mongo.db.events
    #Inserts new event to Mongo database
    events.insert({'name': event_name, 'date': event_date})
    #Redirect to index route
    return redirect("/index")

@app.route('/secret')
def delete():
    #We've connected to the events connection inside the MongoDB databse
    events = mongo.db.events
    #Empty curly brackets means find everything
    myquery = {}
    events.delete_many(myquery)
    return "You deleted the database"
