# RESTful APIs Example

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://djangoproject.com)

This project is just an example on how to consume RESTful APIs using Django.

![RESTful APIs Example Screenshot](https://dzwonsemrish7.cloudfront.net/items/2v0D3l1e3W0D413d1601/Screen%20Shot%202018-02-03%20at%2016.15.08.png)

Read the blog post [How to Use RESTful APIs with Django](https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html).

This project is deployed at [restful-apis-example.herokuapp.com](https://restful-apis-example.herokuapp.com/).

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/sibtc/restful-apis-example.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

*PS: If you have issues installing either `gunicorn` or `psycopg2`, you can remove them from the requirements.txt file and run the command again.*

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/sibtc/restful-apis-example/blob/master/LICENSE).
