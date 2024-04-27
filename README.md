## GEDBOOST Backend
Our Complete backend project using python django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have the following software installed on your system:

- Python 3.x
- pip
- virtualenv

If you're using Ubuntu, you can install these with `sudo apt-get install python3 python3-pip python3-venv`.

### Installing

Steps to start your local development server.

Create a new directory for your project:

```bash
mkdir my_project
cd my_project
Clone the git repository:

git clone https://github.com/micro-hack-alpha-team/PARAM-back-end.git
Create a new virtual environment:

python3 -m venv env
source env/bin/activate  # On Windows use `.\env\Scripts\activate`
Install the Python dependencies on the virtual environment:

pip install -r requirements.txt
Apply the migrations:

python manage.py migrate
Finally, start the development server:

python manage.py runserver
The server should start at localhost:8000


              
