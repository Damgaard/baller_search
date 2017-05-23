from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

import praw

from core.models import NerdBaller, Post


class Command(BaseCommand):
    help = "Create/Update posts stored locally."

    def extract_teaser(self, post):
        """Extract teaser text from the post"""
        if not post.is_self:
            return ""

        teaser = post.selftext[:255]

        # We can fit entire text in teaser
        if len(teaser) < 255:
            return teaser

        return teaser[:-3].strip().rsplit(" ", 1)[0] + "..."


    def handle(self, *args, **options):

        try:
            reddit = praw.Reddit(
                client_id=settings.PRAW_CLIENT_ID,
                client_secret=settings.PRAW_CLIENT_SECRET,
                user_agent=settings.PRAW_USER_AGENT)
        except:
            print("Failed to initiate Reddit. Cannot update data!")
            return

        for nerdballer in NerdBaller.objects.all():
            redditor = reddit.redditor(nerdballer.username)

            for post in redditor.submissions.new():

                if Post.objects.filter(reddit_id=post.id).exists():
                    continue

                pub_date = timezone.datetime.utcfromtimestamp(post.created_utc)
                pub_date = pub_date.replace(tzinfo=timezone.utc)

                Post.objects.create(
                    nerdballer=nerdballer,
                    permalink=post.permalink,
                    pub_date=pub_date,
                    score=post.score,
                    teaser=self.extract_teaser(post),
                    title=post.title,
                )
