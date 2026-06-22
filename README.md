# FitTrack

A simple workout tracking app built with Django. Log your training sessions and keep a record of your activity, duration, and date.

## Features

- Log workouts with activity type, duration, and date
- View all sessions sorted by most recent
- Clean dark UI built with Bootstrap 5

## Tech Stack

- Python / Django
- SQLite (local) / PostgreSQL (production)
- Bootstrap 5 + Bootstrap Icons
- Deployed on [Render](https://render.com)

## Local Setup

**1. Clone the repo and create a virtual environment**

```bash
git clone https://github.com/tu-usuario/fitness-tracker.git
cd fitness-tracker
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run migrations and start the server**

```bash
python manage.py migrate
python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Deployment (Render)

1. Push the repo to GitHub
2. In Render, create a new **Web Service** connected to the repo
3. Set the following:
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
   - **Start Command:** `gunicorn fitness_project.wsgi:application`
4. Add these environment variables:
   - `SECRET_KEY` — a long random string
   - `DEBUG` — `False`
   - `ALLOWED_HOSTS` — `.onrender.com`
   - `DATABASE_URL` — Internal Database URL from a Render PostgreSQL instance
