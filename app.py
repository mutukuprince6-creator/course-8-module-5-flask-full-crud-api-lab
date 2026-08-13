from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not title or not str(title).strip():
        return jsonify({"error": "Title is required"}), 400

    new_id = max((event.id for event in events), default=0) + 1
    new_event = Event(new_id, str(title).strip())
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201

# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = next((item for item in events if item.id == event_id), None)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json(silent=True) or {}
    new_title = data.get("title")

    if not new_title or not str(new_title).strip():
        return jsonify({"error": "Title is required"}), 400

    event.title = str(new_title).strip()
    return jsonify(event.to_dict()), 200

# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    for index, event in enumerate(events):
        if event.id == event_id:
            del events[index]
            return "", 204

    return jsonify({"error": "Event not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
