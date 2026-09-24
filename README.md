# Event Registration System

A backend system for managing events and user registrations, built with Django, Django REST Framework, and PostgreSQL. Users can view events, register for them, and manage (view/cancel) their own registrations.

## Features
- View a list of all events
- View details of a specific event
- Register for an event
- View your own registrations
- Cancel a registration

## Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL

## Setup

Clone the repository and move into the folder:
```
git clone <repo-url>
cd event-reg-system
```

Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\Activate.ps1
```

Install dependencies:
```
pip install -r requirements.txt
```

Create a `.env` file in the project root with your PostgreSQL credentials:
```
DB_NAME=event_registration_db
DB_USER=event_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Run migrations:
```
python manage.py migrate
```

Run the app:
```
python manage.py runserver
```

The app will start on `http://localhost:8000`

## API Usage

All registration endpoints require authentication (logged-in user).

Method	    Endpoint	                        Description
GET	        /api/events/	                    Get a list of all events
GET   	    /api/events/<id>/	                Get details of a single event
POST	    /api/registrations/	                Register for an event (send the event ID in the request body the logged-in user is linked automatically)

GET	        /api/registrations/my/	            View your own registrations
DELETE	    /api/registrations/<id>/cancel/	   Cancel one of your own registrations

## Author
Kainat Rasheed — CodeAlpha Backend Development Intern