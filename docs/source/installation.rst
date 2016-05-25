..  _installation:

************
Installation
************

Prerequisites
=============

pip and setuptools
------------------

Please make sure you have the latest version of pip and setuptools installed.
For installation and/or help, go to:

* `pip documentation <https://pip.pypa.io/en/stable/>`_
* `setup tools documentation <https://github.com/pypa/setuptools>`_

virtual environment
-------------------

You can create a virtual environment using
`virtualenv <https://virtualenv.pypa.io/en/latest/index.html>`_. 
Please see its documentation for installation and further information.


Project setup
=============

At the moment *correos* requires the following:

* Django (1.5.4)
* django-filter (0.7)
* django-uuidfield (0.4.0)
* djangorestframework (2.3.8)
* python-dateutil (1.5) 

We recommend you to enable a virtual environment before installing *correos* to 
avoid conflicts with other projects you are working on. 

To clone the repository using git, please type::

    $ git clone git@github.com:transcode-de/correos.git

To set up the project please execute following commands at your terminal::

    $ pip install -r requirements/base.txt
    $ cd correos_project/
    $ python manage.py syncdb


Documentation setup
===================

We use `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ to document *correos*.
To view it in your browser, you first have install the documentation
dependencies::

    $ pip install -r requirements/docs.txt

After that you can go into the docs directory and build the documentation::

    $ cd docs/
    docs/ $ make html

Finally you can find the documentation in the build directory.
