import re

from django.core.management.base import BaseCommand

from tqdm import tqdm

from ...utils import clean_username, get_reddit_instance, redditor_exists
from ....core.models import NerdBaller


class Command(BaseCommand):

    help = "Create Starcraft NerdBaller list from Wiki Page."

    # The Implementation relies on the current setup of the page
    # If it changes fundamentally, this will break. I could make this
    # more resilliant, however it was pretty fast to write and I'll just
    # rewrite this if the page happens to be completely rewritten.

    def handle(self, *args, **options):
        reddit = get_reddit_instance()
        wikipage = reddit.subreddit('starcraft').wiki['verified_users']

        # Bit hacky way to get the table of NerdBallers
        table = wikipage.content_md.split(":---|:---|:---")[1].strip()
        rows = table.split("\n")

        for row in tqdm(rows):
            cells = row.strip().split("|")

            assert(len(cells) == 3)

            username, description, category = cells
            username = clean_username(username)

            if not redditor_exists(username=username, reddit=reddit):
                continue

            NerdBaller.objects.get_or_create(
                username=username,
                known_as=self.extract_known_as(description),
            )

    def extract_known_as(self, description):
        # Commonly used descriptions, that are actually misnormers
        ignored_known_as = ["observer", ]

        known_as_regex = re.compile("\[(.*?)\]\(.*?\)")
        links = known_as_regex.findall(description)

        if len(links) > 1:
            known_as = ""
        elif len(links) == 1:
            known_as = links[0]
        else:
            known_as = description

        # Known usernames are singleword, so if the remaining description
        # is more than one word it is obviously not what they are known as.
        if len(known_as.split()) > 1:
            known_as = ""

        if known_as.lower() in ignored_known_as:
            known_as = ""

        return known_as
