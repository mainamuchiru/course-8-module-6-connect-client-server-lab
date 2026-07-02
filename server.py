from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'

class Event: 
    def __init__ (self,id,title):
        self.id = id
        self.title = title
        
    def to_dict(self):
        return{"id": self.id, "title": self.title}

events = [{"id": 1, "title": "Hackathon"},{"id": 2, "title":"Career fair"},
          {"id": 3, "title":"Public Speaking"}]


# TASK: Create a route for "/"
# This route should return a JSON welcome message

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome Home"

# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

# TASK: Create a POST route for "/events"
# This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
# 3. Create a new event with a unique ID and the provided title
# 4. Add the new event to the events list
# 5. Return the new event with status code 201

@app.route("/events", methods=["POST"])
def create_events():
    data = request.get_json()
    new_id = max((e.id for e in events), default=0) + 1
    new_event = Event(id=new_id, title=data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

if __name__ == "__main__":
    app.run(debug=True)
