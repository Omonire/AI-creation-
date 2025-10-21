# Hospital Management System

A modular, web-based Hospital Management System built with Flask.

## Features

- Role-based access control (Admin, Department Heads, Staff)
- Patient management, EMR, appointments
- Doctor, Nurse, Pharmacy, Lab, Records modules
- Duty roster with interactive calendar
- Notifications and alerts
- Export reports to PDF/CSV

## Prerequisites

- Python 3.8+
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd hospital_management_system
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (optional, create .env file):
   - SECRET_KEY=your-secret-key
   - DATABASE_URL=sqlite:///app.db

5. Initialize the database:
   ```bash
   flask shell
   >>> from hms_app.models import db
   >>> db.create_all()
   >>> exit()
   ```

## Running the Application

```bash
python run.py
```

The application will be available at http://127.0.0.1:5000/

## Usage

- Default admin login: admin@example.com / password
- Create roles and assign users via the admin dashboard.

## Migration to Django

The code is structured modularly to ease migration to Django.

## License

MIT License
