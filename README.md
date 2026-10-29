# Roomly — student rental marketplace

A Django starter for students and property owners with registration, role-aware navigation, property and room listings, area/budget/type filters, visit requests, owner visit management, inquiries, and admin-managed photos.

## Run locally

1. Install Python 3.10+ and create a virtual environment: `python -m venv .venv`
2. Activate it and install dependencies: `pip install -r requirements.txt`
3. Create the database: `python manage.py makemigrations accounts listings interactions` then `python manage.py migrate`
4. Optional admin account: `python manage.py createsuperuser`
5. Start the server: `python manage.py runserver`; open http://127.0.0.1:8000/

Register as an Owner to publish rooms or a Student to browse and request visits. Admin is at `/admin/`. The local SQLite DB and uploaded images are created as needed.

## Scope

Real-time chat, callback workflows, payment processing, booking agreements, analytics, and payment history are future extension points; this starter does not take payments. Before deployment, set a strong secret key, disable DEBUG, configure hosts, HTTPS, email, backups, and a production database.
