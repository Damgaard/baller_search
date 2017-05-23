import re

from django.core.management.base import BaseCommand
from django.utils import timezone

from tqdm import tqdm
import praw

from ...utils import get_reddit_instance
from core.models import NerdBaller


# Commonly used descriptions, that are actually misnormers
IGNORED_KNOWN_AS = ["observer", ]

class Command(BaseCommand):

    help = "Create Starcraft NerdBaller list from Wiki Page."

    # The Implementation relies on the current setup of the page
    # If it changes fundamentally, this will break. I could make this
    # more resilliant, however it was pretty fast to write and I'll just
    # rewrite this if the page happens to be completely rewritten.

    def handle(self, *args, **options):

        reddit = get_reddit_instance()

        wikipage = reddit.subreddit('starcraft').wiki['verified_users']

        known_as_regex = re.compile("\[(.*?)\]\(.*?\)")

        # Bit hacky way to get the table of NerdBallers
        table = wikipage.content_md.split(":---|:---|:---")[1].strip()
        rows = table.split("\n")

        for row in tqdm(rows):
            row = row.strip()
            cells = row.split("|")

            assert(len(cells) == 3)

            username, description, category = cells
            if username.startswith("/u/"):
                username = username[3:]

            if NerdBaller.objects.filter(username__iexact=username).exists():
                continue

            # Check user actually exists
            try:
                reddit.redditor(username).link_karma
            except Exception:
                continue

            links = known_as_regex.findall(description)

            if len(links) > 1:
                known_as = ""
            elif len(links) == 1:
                known_as = links[0]
            else:
                known_as = description

            if len(known_as.split()) > 1:
                known_as = ""

            if known_as.lower() in IGNORED_KNOWN_AS:
                known_as = ""

            NerdBaller.objects.create(
                username=username,
                known_as=known_as,
            )
