# E-Ration Management System

A modern digital solution for managing ration distribution efficiently and transparently. This web application helps users manage their ration cards, request products, and track their quotas digitally.

## Features

- **User Authentication**
  - Secure login and registration system
  - Smart card integration
  - Password encryption using scrypt
  - Session management

- **Dashboard**
  - Real-time quota tracking
  - Available balance display
  - Product catalog
  - Transaction history
  - Monthly distribution schedule

- **Product Management**
  - Request essential commodities
  - Track request status
  - View available stock
  - Price information
  - Quantity limits enforcement

- **Profile Management**
  - View and edit personal information
  - Smart card details
  - Contact information
  - Transaction history

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (Development), MySQL (Production)
- **Frontend**: HTML, TailwindCSS, JavaScript
- **Authentication**: Flask-Login
- **ORM**: SQLAlchemy
- **Server**: Gunicorn

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Brindhasaravana/E-Ration-Management-System.git
cd E-Ration-Management-System
```

2. Create and activate virtual environment: (Not necessary)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db upgrade
```

## Configuration

1. Create a `.env` file in the root directory:
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///database.db
```

2. Update database configuration in `app/__init__.py` if needed:
```python
startLine: 11
endLine: 12
```

## Running the Application

1. Development server:
```bash
flask run
```

2. Production server:
```bash
gunicorn "run:app" --workers 4 --bind 0.0.0.0:8000
```

## Project Structure

```
E-Ration-Management-System/
├── app/
│   ├── __init__.py      # Application factory
│   ├── auth.py          # Authentication routes
│   ├── models.py        # Database models
│   ├── routes.py        # Main routes
│   └── templates/       # HTML templates
├── migrations/          # Database migrations
├── requirements.txt     # Project dependencies
├── run.py              # Application entry point
└── README.md           # Project documentation
```

## API Endpoints

- `/`: Home page
- `/login`: User login
- `/register`: New user registration
- `/dashboard`: User dashboard
- `/profile`: User profile
- `/request-product`: Product request endpoint
- `/product/add`: Add new product (Admin)
- `/product/update`: Update product details (Admin)
- `/product/getAll`: Get all products
- `/product/getById`: Get specific product

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Security Features

- Password hashing using scrypt
- CSRF protection
- Session management
- Input validation
- SQL injection prevention
- XSS protection

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Acknowledgments

- Flask documentation
- TailwindCSS team
- SQLAlchemy documentation
- Python community

