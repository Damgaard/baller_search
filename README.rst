Baller Search
=============

Easily find posts by sick Nerd Ballers

Running tests
~~~~~~~~~~~~~

::

  $ py.test --ignore virtualenv --reuse-db

To check test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

TODO
----

The grand list of stuff that needs to be done before project can be publiczed

Content
^^^^^^^

 - DONE Add about section (reuse from old Reddit post)
 - DONE Nuke profile/user related views
 - DONE Include users from NotSpartacus post https://www.reddit.com/r/starcraft/comments/lurc5/a_list_of_community_members_reddit_and_twitter/
 - DONE Add better explanation on why to search and suggestions
 - DONE Add whitelisting/blacklisting of domains to prevent popular non-starcraft
    stuff showing up.

General Web
^^^^^^^^^^^

 - DONE Configure Django Compressor
 - DONE Shutdown /admin in production
 - DONE Cookie Warning
 - DONE Google Analytics
 - DONE Add sitemap.xml
 - DONE Add robots.txt
 - DONE Check if any modules need upgrading
 - DONE Switch pip out with pip-tools

Server && Deploy
^^^^^^^^^^^^^^^^

 - DONE Buy domain (hopefully available) :)
 - DONE Add nginx/uwsgi config files to repo
 - DONE Setup SSL
 - DONE Verify A SSL rating on https://www.ssllabs.com/ssltest/analyze.html?d=baller-search.com
 - DONE Verify Django Security Erics pony checker https://www.ponycheckup.com/
 - DONE Initialize on new server via ansible
