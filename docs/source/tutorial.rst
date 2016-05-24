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

If you played around for a while, turn to the following chapter that offers 
more information about the whole process. 
