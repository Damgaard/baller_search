from os import path

from django.conf import settings
from django.utils import timezone

from haystack import indexes

from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    score_i = indexes.IntegerField(model_attr='score')

    def get_model(self):
        return Post

    def get_blacklisted_subs(self):
        """Return a list of blacklisted subs."""
        blacklist_location = path.join(str(settings.ROOT_DIR), "blacklisted_subs.txt")

        if not path.exists(blacklist_location):
            return []
        else:
            return self._read_blacklist_file(blacklist_location)

    def _read_blacklist_file(self, blacklist_location):
        """Read and parse blacklist file. Return blacklisted subs."""
        blacklisted_subs = []

        with open(blacklist_location) as infile:
            for line in infile.readlines():
                if not line.startswith("#") and len(line.strip()):
                    blacklisted_subs.append(line.strip())

        return blacklisted_subs

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        blacklisted_subs = self.get_blacklisted_subs()

        return self.get_model().objects.exclude(
            subreddit__in=blacklisted_subs,
        )
