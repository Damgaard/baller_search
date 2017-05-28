from django.core.management.base import BaseCommand
from django.utils import timezone

from tqdm import tqdm

from ...utils import get_reddit_instance, shorten_text
from ....core.models import NerdBaller, Post


class Command(BaseCommand):

    help = "Create/Update posts stored locally."

    def handle(self, *args, **options):

        reddit = get_reddit_instance()

        for nerdballer in tqdm(NerdBaller.objects.all()):
            redditor = reddit.redditor(nerdballer.username)

            for post in redditor.submissions.new(limit=1000):

                if Post.objects.filter(reddit_id=post.id).exists():
                    continue

                pub_date = timezone.datetime.utcfromtimestamp(post.created_utc)
                pub_date = pub_date.replace(tzinfo=timezone.utc)

                Post.objects.create(
                    nerdballer=nerdballer,
                    permalink=post.permalink,
                    pub_date=pub_date,
                    reddit_id=post.id,
                    score=post.score,
                    subreddit=post.subreddit.display_name,
                    teaser=shorten_text(post.selftext),
                    title=shorten_text(post.title),
                )
