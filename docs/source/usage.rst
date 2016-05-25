..  _usage:

*****
Usage
*****

For requirements and installation please refer to the 
:ref:`installation chapter <installation>`.

web interface
=============

Start the Django included webserver to access the web interface like this::

    $ python manage.py runserver

Open ``http://127.0.0.1:8000/`` in your web browser. 

*correos* SMTPd
===============

Start the *correos* SMTP server like this::

    $ python manage.py runsmtpd

You can send a test email (with the SMTP server still running) like this::

    $ python manage.py sendtestemail

If you want to send more than 1 test email, add the number behind the command
like this::

     $ python manage.py sendtestemail -c 5


settings
========

You can add or configurate settings at the ``settings.py`` within your
project folder. There is an embedded documentation too, so you can find your way
easily.

Here are some important notes:

``CORREOS_PORT``
    The port the SMTP server listens to (default: ``1025``)

``CORREOS_SMTP_LOCAL``
    Allows only incoming email from the local machine if set to ``True``
    (default: ``True``)

``CORREOS_USE_PUBLIC_IP``
    Set to ``True`` to start the SMTP server using your public IP 
    address (default: ``False``)

``DATABASES``
    Add here all used databases and their settings

