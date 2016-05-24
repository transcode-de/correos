..  _tutorial:

********
Tutorial
********

This part of the documentation aims particulary at beginners in programming 
and/or Django and will describe what specific code components are made for and 
how everything in *correos* works together. If you simply want to get to know 
the usage and the facts of the REST API, please refer
to :ref:`the usage chapter <usage>`. 

Let's start!
First please make sure that you have installed everything correctly 
(see: :ref:`installation <installation>`) that you will be able to follow
and try out *correos* at your own device too.

Besides, if necessary, it would be helpful if you would make yourself familiar 
with the following issues:
    * `client-server model <https://en.wikipedia.org/wiki/Client-server_model>`_
    * `OSI model <https://en.wikipedia.org/wiki/OSI_model>`_
    * `Simple Mail Transfer Protocol <https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol>`_
    * `Hypertext Transfer Protocol <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_

For getting to know the basic ideas of Django, we recommend you:
    
    * `django-marcador tutorial <http://django-marcador.keimlink.de/>`_
    * `django docs tutorial <https://docs.djangoproject.com/en/1.9/intro/>`_


Introduction
============

Let's go over some parts of *correos* code to understand what 
is actually happening behind the scenes. 
As you know already - since you found your way here - *correos* implements a
local mail server for testing purposes. That means, for example, if you are 
developing an application including an email function, *correos* will help you 
to find out if this works the way you want it to work. 

*Correos* is delivered with a web interface, so you can easily discover the 
results in your web browser. But the REST API will make your data available for 
many further processes too! 

Let's discover the following graphics to understand the main processes
before we will have a look at the details:

..  _correosgraphics:

.. image:: _static/correos.png
    :width: 650px
    :align: left
    :alt: correos process


The *correos* mail server (SMTPd) is able to receive data from
a mail user agent (MUA) via SMTP. So *correos* can handle any incoming data 
conforming the SMTP standard. To illustrate this process *correos* comes 
with an own client function to send testmails as well. 
The *correos* server will manage it to send the received email data to a 
database where it will be stored.
The REST API is able to communicate with the database in both directions, 
it can send and receive data from it.
A web application of any kind able to communicate via HTTP, can 
connect to the REST API to receive and send data for further processing.
*Correos* comes itself with a web interface, so it is comfortable for you to 
watch the results.


Trying *correos*
=================

Now try it yourself to see how *correos* works. Open your terminal. If you are
using a virtual environment please activate it and navigate to the *correos* 
directory containing the file ``manage.py``. 

To start the Django included webserver to access the web interface please type::

    $ python manage.py runserver

Open your web browser and point to ``http://127.0.0.1:8000/``. 
Go back to the terminal and start the *correos* SMTP server like this::

    $ python manage.py runsmtpd

You can send a test email (with the SMTP server still running) like this::

    $ python manage.py sendtestemail

If you want to send more than 1 test email, add the number behind the command
like this::

     $ python manage.py sendtestemail -c 5

If you played around for a while, turn to the following chapters that offer 
more information about the whole process.

Understanding *correos* 
=======================

Since *correos* is based on the django framework, we will now have a look at
the process happening while *correos* is running. If you need to get more
general information for understanding, please refer to the django documentation
linked above.

models and database
-------------------

* "A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table."*
    -- `Models | Django Documentation <https://docs.djangoproject.com/en/1.9/topics/db/models/>`_

If you navigate to your *correos* project and open the file ``models.py`` you
will find three models:
    * Domain (represents information about the domain of the recipient's email server) 
    * Recipient (represents information about the recipient of the email)
    * Email (represents information about the email itself)

You can see all attributes each model is containing and some functions as well.
Note that the model Recipient contains a ForeignKey field called domain
which connects it to the Domain model (related_name is 'users'), likewise the 
model Email has got one (recipient) that connects it to the Recipient model
(related_name is 'emails').

The Email model contains a custom manager (EmailManager) as well, 
assigned to `objects`. This manager contains important functionality, we will
have a look at now.

custom manager
--------------

Open the file ``managers.py`` to see what the manager is doing.

The EmailManager class contains a function called ``create_from_message``
returning a list of Email objects. These objects are created according to
definitions in the  models.py we discussed above and saved as new 
entries in the database.

As we will see later, the ``create_from_message`` function will be called by
our correos SMTP server after receiving an email from a MUA. 

See the documentation embedded into the code of ``managers.py`` to understand
in which way the manager works in detail.

Note another point here: The ``json.dumps`` function is called to assign 
a JSON string to the header attribute. For more information about JSON,
`read here <http://json.org/>`_.

CorreosSMTPServer
-----------------

Let's now look at the heart of *correos*. Please open the file ``runsmtpd.py``
which you will find inside your *correos* project at the management folder.

As you can see, this file contains two class definitions. 

The class ``Command`` needs to be implemented that the command ``runsmtpd``
works at all. (Remember that you used this command already while trying out 
*correos* in the beginning). Its function ``handle`` keeps the actual logic 
of the command since it instantiates an entity of the ``CorreosSMTPServer``
class and enters a polling loop waiting for incoming emails, that makes the 
server running in the first place. 

The ``CorreosSMTPServer`` class contains a function called ``process_message``,
which is responsible to check if the incoming email has a valid sender
according to the *correos* settings. Setting details you will find in the
:ref:`the usage chapter <usage>`.
If the sender is valid, the ``create_the_message`` function will be called
as discussed earlier.

Please see the embedded code documentation as well to understand all.


That's it on the whole. Going back to our
:ref:`graphics from the beginning <correosgraphics>`, you can see that we
focused on the left side of the process so far. You saw how the *correos*
server is instantiated, how it handles incoming emails send by a MUA and how
the data of the emails is stored to the database. 

Let's now discover what role the REST API plays.
