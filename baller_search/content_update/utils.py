"""Various utility functions for updating content."""

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

import praw


def clean_known_as(text):
    """Remove stauff that may be around a known as description"""
    text = text.strip()
    if not text:
        return ""

    return text.split()[0]


def clean_username(username):
    """Remove stauff that may be around a username"""
    if username.startswith("/u/"):
        username = username[3:]

    # First strip is for whitespace, second for excess tails
    return username.strip().strip("/")


def redditor_exists(username, reddit=None):
    """Returns True if that redditor (still) exists."""
    if reddit is None:
        reddit = get_reddit_instance()

    redditor = reddit.redditor(username)

    # The Redditor object is fetched lazily for optimization purposes. So
    # we have to force the fetching of new data to evaluate whether the
    # user exists or not.

    try:
        redditor._fetch()
        return True
    except:
        return False


def get_reddit_instance():
    """Return Reddit instance.

    Throws ImproperlyConfigured if called without required PRAW settings
    set or being invalid.

    """

    for praw_setting in ["PRAW_CLIENT_ID", "PRAW_CLIENT_SECRET", "PRAW_USER_AGENT"]:
        if getattr(settings, praw_setting) is None:
            err_msg = "Cannot initialize Reddit. {} is not set".format(praw_setting)
            raise ImproperlyConfigured(err_msg)

    try:
        return praw.Reddit(
            client_id=settings.PRAW_CLIENT_ID,
            client_secret=settings.PRAW_CLIENT_SECRET,
            user_agent=settings.PRAW_USER_AGENT)
    except:
        raise ImproperlyConfigured("Cannot initialize Reddit. Unexpected Error")


def shorten_text(text, max_length=255):
    """Shorten text to the max_length. Add ... if text was longer than 255"""

    # Need room for the dots
    assert(max_length > 3)

    # We can fit entire text in text
    if len(text) < max_length:
        return text

    text = text[:max_length]

    return text[:-3].strip().rsplit(" ", 1)[0] + "..."
