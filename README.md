# Habit Tracker

This is a Habit Tracker application built with Django, allowing users to create, track, and manage their habits. The app helps users track streaks, mark habits as completed, and view their progress over time.

## Features

- **User Authentication**: Secure login and registration system to manage users.
- **Habit Creation**: Users can create and manage their personal habits.
- **Habit Completion**: Mark habits as completed for the day, and see a visual representation of streaks.
- **Streak Tracking**: Habit streaks are calculated based on consecutive days of completion.
- **Responsive Design**: The app is mobile-friendly and works well on both desktop and mobile devices.

## Screenshots

![Habit Tracker Screenshot](https://via.placeholder.com/600x400?text=Habit+Tracker+Screenshot)

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite (default for development)
- **Version Control**: Git, GitHub

## Requirements

- Python 3.x
- Django 3.x
- SQLite (default database used)
- Bootstrap (for styling)

## Installation
## Installation

1. Clone the repository:
```bash
git clone https://github.com/dharmateja03/Streakpy.git
cd habit-tracker
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up database:
```bash
python manage.py migrate
```

5. Create admin user:
```bash
python manage.py createsuperuser
```

6. Start development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## Features

- User authentication (login/signup)
- Create and manage habits
- Track daily completion
- View habit streaks
- Simple and intuitive interface

## Usage

1. Create an account or login
2. Add new habits from your dashboard
3. Mark habits as complete daily
4. Track your progress and maintain streaks

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -am 'Add feature'`)
4. Push to branch (`git push origin feature-name`)
5. Open pull request

## License

This project is licensed under the MIT License.

## Stack

- Django
- SQLite
- HTML/CSS
- JavaScript

## Author

Made by Dharma Teja 

Follow these steps to set up and run the project on your local machine.

1. **Clone the repository**:
   ```bash
  
