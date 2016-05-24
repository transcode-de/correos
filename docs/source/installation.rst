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


Project setup
=============

Clone the repository:


Enable the virtual environment:


To set up the project (installing Django please execute following commands at your terminal::

    $ pip install -r requirements/base.txt
    $ cd correos_project/
    $ python manage.py syncdb


Documentation
=============

To view and build the documentation you first have install our documentation
dependencies::

    $ pip install -r requirements/docs.txt

After that you can go into the docs directory and build the documentation::

    $ cd docs/
    docs/ $ make html

Finally you can find the documentation in the build directory.
