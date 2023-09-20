# Celery Study Project with Django

**Description**: This project is a comprehensive study of Celery integration within a Django application, aimed at understanding sub-tasks and thread management.

## Table of Contents

- **Installation**
- **Usage**
- **Configuration**
- **Tasks and Sub-Tasks**
- **Contributing**
- **License**

## Installation

### Prerequisites
- Python (>=3.x)
- [Virtual Environment](https://docs.python.org/3/library/venv.html) (recommended)

### Steps
1. Clone this repository:
git clone https://github.com/yourusername/celery-django-study.git
cd celery-django-study

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install the project dependencies:
pip install -r requirements.txt

4. Apply database migrations:
python manage.py migrate

5. Start the Celery worker:
celery -A your_project_name worker -l info

6. Start the development server:
python manage.py runserver

Your Celery study project should now be running locally at `http://localhost:8000/`.

## Usage

Explore the Celery integration within the Django application and experiment with sub-tasks to gain a deeper understanding of their functionality.

## Configuration

Environment variables can be set in the `settings.py` file.

## Tasks and Sub-Tasks

Learn how to effectively manage tasks and sub-tasks using Celery within your Django application. Refer to examples in the codebase for guidance.

## Contributing

This project is currently not available for contributions.

## License

This project is licensed under the [MIT License](LICENSE.md). You are free to use, modify, and distribute it.
