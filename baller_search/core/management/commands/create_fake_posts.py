from django.core.management.base import BaseCommand

from django.utils import timezone

from ...models import Post


class Command(BaseCommand):
    help = "Generate some fake posts for local testing"

    def handle(self, *args, **options):
        # Just do this once
        if Post.objects.count() != 0:
            return

        for tmp in range(7):
            Post.objects.create(title="Hello World", pub_date=timezone.now())
            Post.objects.create(title="World Is On A Flying Turtle", pub_date=timezone.now())
            Post.objects.create(title="Much to say about Nothing", pub_date=timezone.now())
            Post.objects.create(title="Frigthening Flight", pub_date=timezone.now())
            Post.objects.create(title="Flying Tiger, Hidden Dragon", pub_date=timezone.now())
