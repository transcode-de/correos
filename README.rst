*******
Correos
*******

A local mail server and client to be used as a development tool.

Setup the project::

    $ pip install -r requirements.txt
    $ cd correos_project
    $ python manage.py syncdb

Start the webserver::

    $ python manage.py runserver

Start the SMTP server::

    $ python manage.py runsmtpd

Send a test email::

    $ python manage.py testemail
