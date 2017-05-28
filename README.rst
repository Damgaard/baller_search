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

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser


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

Content
^^^^^^^

 - DONE Add about section (reuse from old Reddit post)
 - DONE Nuke profile/user related views
 - DONE Include users from NotSpartacus post https://www.reddit.com/r/starcraft/comments/lurc5/a_list_of_community_members_reddit_and_twitter/
 - Add better explanation on why to search and suggestions
 - DONE Add whitelisting/blacklisting of domains to prevent popular non-starcraft
    stuff showing up.

General Web
^^^^^^^^^^^

 - DONE Configure Django Compressor
 - DONE Shutdown /admin in production
 - Cookie Warning
 - Google Analytics
 - DONE Add sitemap.xml
 - DONE Add robots.txt
 - Check if any modules need upgrading
 - Switch pip out with pip-tools

Server && Deploy
^^^^^^^^^^^^^^^^

 - DONE Buy domain (hopefully available) :)
 - Add nginx/uwsgi config files to repo
 - Setup SSL
 - Verify A+ SSL rating on https://www.ssllabs.com/ssltest/analyze.html?d=baller-search.com
 - Verify Django Security Erics pony checker https://www.ponycheckup.com/
 - Initialize on new server via ansible
 - Add `radon cc -anb baller_search config docs requirements utility` to development.
    If there's non-A grade code it shouldn't be deployed.
