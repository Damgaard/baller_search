import re

from django.core.management.base import BaseCommand

from tqdm import tqdm

from ...utils import clean_known_as, clean_username, get_reddit_instance, redditor_exists
from ....core.models import NerdBaller


class Command(BaseCommand):

    help = "Create Starcraft NerdBaller list from NotSpartacus page."

    # The Implementation relies on the current setup of the page
    # If it changes fundamentally, this will break. I could make this
    # more resilliant, however it was pretty fast to write and I'll just
    # rewrite this if the page happens to be completely rewritten.

    def extract_ballers(self, text):
        """Given a text block, return NerdBaller iterable.

        The iterable will contain (username, known_as, description) tuples.

        """
        no_description_regex = re.compile("\n([^-]*?) - ([^-]*?)(?=\n)")
        description_regex = re.compile("\n(.*?) - (.*?) - (.*?)(?=\n)")
        extract_reddit_regex = re.compile("\[reddit]\(.*?\/user\/(.*?)\)")

        combined = []
        for match in no_description_regex.findall(text):
            known_as = clean_known_as(match[0])
            username = clean_username(extract_reddit_regex.findall(match[1])[0])
            combined.append([known_as, username, ""])

        for match in description_regex.findall(text):
            known_as = clean_known_as(match[0])
            username = clean_username(extract_reddit_regex.findall(match[1])[0])
            combined.append([known_as, username, match[2].strip()])

        return combined

    def get_texts(self, reddit, submission, username):
        """Extract all texts to this submission by author of that username"""
        # TODO: Consider making this a utility function
        submission = reddit.submission(submission)
        not_spartacus = reddit.redditor(username)

        return [submission.selftext] + [com.body for com in submission.comments if com.author == not_spartacus]

    def handle(self, *args, **options):
        reddit = get_reddit_instance()
        texts = self.get_texts(reddit=reddit, submission='lurc5', username="NotSpartacus")

        ballers = []
        for text in texts:
            ballers += self.extract_ballers(text)

        for baller in ballers:
            if NerdBaller.objects.filter(username=baller[1]).exists():
                continue

            if not redditor_exists(username=baller[1], reddit=reddit):
                continue

            NerdBaller.objects.create(
                username=baller[1],
                known_as=baller[0],
                description=baller[2],
            )
