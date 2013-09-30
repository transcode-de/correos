*******
Correos
*******

A local mail server and client to be used as a development tool.

A demo is runnging at http://kg358.gondor.co/

Quickstart
==========

Set up the project::

    $ pip install -r requirements/base.txt
    $ cd correos_project
    $ python manage.py syncdb

Start the webserver to access the web interface::

    $ python manage.py runserver

Start the SMTP server to receive new emails::

    $ python manage.py runsmtpd

Send a test email (with the SMTP server still running)::

    $ python manage.py testemail

Configuration
=============

CORREOS_PORT
    The port the SMTP server listens to (default: ``1025``)

CORREOS_SMTP_LOCAL
    Allows only incoming email from the local machine if set to ``True`` (default: ``True``)

CORREOS_USE_PUBLIC_IP
    Set to ``True`` to start the SMTP server using your public IP address (default: ``False``)

REST API
========

Beside the web interface there is a REST API which makes all the data
available too. The REST API entry point is at ``/api/``.
