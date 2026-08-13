# Event Management API

A simple Flask API for managing events in memory. This project demonstrates how to build a small RESTful service using Python, Flask, and JSON-based request/response handling.

## Purpose

The API allows users to:

- Create a new event with `POST /events`
- Update an event title with `PATCH /events/<id>`
- Delete an event with `DELETE /events/<id>`

The application uses an in-memory list of `Event` objects to simulate persistent storage for the lab.

## Routes

### POST /events
Creates a new event.

Request body:

```json
{
  "title": "Hackathon"
}
```

Example response:

```json
{
  "id": 3,
  "title": "Hackathon"
}
```

Status code: `201 Created`

### PATCH /events/<id>
Updates the title of an existing event.

Request body:

```json
{
  "title": "Hackathon 2025"
}
```

Example response:

```json
{
  "id": 1,
  "title": "Hackathon 2025"
}
```

Status code: `200 OK`

### DELETE /events/<id>
Deletes an event by ID.

Example response:

```http
HTTP/1.1 204 No Content
```

Status code: `204 No Content`

### Error handling

If an event is missing:

```json
{
  "error": "Event not found"
}
```

Status code: `404 Not Found`

If the title is missing or empty:

```json
{
  "error": "Title is required"
}
```

Status code: `400 Bad Request`

## Local setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Flask:

```bash
pip install flask
```

3. Run the app:

```bash
python app.py
```

4. Test the API at `http://127.0.0.1:5000`

## Example requests

### Create an event

```bash
curl -X POST http://127.0.0.1:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title":"Hackathon"}'
```

### Update an event

```bash
curl -X PATCH http://127.0.0.1:5000/events/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Hackathon 2025"}'
```

### Delete an event

```bash
curl -X DELETE http://127.0.0.1:5000/events/2
```

## Implementation notes

This project follows Flask best practices:

- Routes use nouns (`/events`) and clear HTTP methods.
- Request data is read with `request.get_json()`.
- Responses are returned with `jsonify()`.
- Inline comments explain the main logic for creating, updating, and deleting events.
- Each route returns meaningful status codes.

## Example JSON responses

### Successful create

```json
{
  "id": 3,
  "title": "Hackathon"
}
```

### Successful update

```json
{
  "id": 1,
  "title": "Hackathon 2025"
}
```

### Missing resource

```json
{
  "error": "Event not found"
}
```

## Summary

This API demonstrates the core structure of a simple RESTful backend:

- route design
- JSON handling
- data modeling
- error responses
- proper HTTP status codes

It is intentionally lightweight and uses an in-memory list so the behavior is easy to understand and test.
