Baller Search
=============

Easily find posts by sick Nerd Ballers

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test --ignore virtualenv

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Deployment
----------

The following details how to deploy this application.


TODO
----

The grand list of stuff that needs to be done before project can be publiczed

 - Add Google Analytics
 - Configure Django Compressor
 - Include users and links from old post https://www.reddit.com/r/starcraft/comments/nirtb/all_pro_caster_and_baller_created_threads_in/
 - Initialize on new server via ansible
 - DONE Shutdown /admin in production
 - Hide profile/user related views
 - Add FAQ section (reuse from old Reddit post)
 - Add better explanation on why to search
 - DONE Buy domain (hopefully available) :)
 - Setup SSL
 - Test on Erics pony checker https://www.ponycheckup.com/
 - Add `radon cc -anb baller_search config docs requirements utility` to development.
    If there's non-A grade code it shouldn't be deployed.
