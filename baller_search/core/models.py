from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    """A Post on Reddit"""

    # ForeginKey to Baller

    title = models.CharField(
        max_length=255,
    )
    teaser = models.CharField(
        _(u"First part of the body"),
        blank=True,
        max_length=255,
    )
    reddit_id = models.CharField(
        max_length=64,
    )
    pub_date = models.DateTimeField(
        _(u"When it was published on Reddit"),
    )
    score= models.IntegerField(
        _(u"Reddit Score"),
        default=0,
    )

    def __unicode__(self):
        return self.title

    class Meta:
        pass
