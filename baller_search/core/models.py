from django.db import models
from django.utils.translation import ugettext_lazy as _


class NerdBaller(models.Model):
    """Sick Nerd Ballers, whose posts are real interesting"""

    username = models.CharField(
        _(u"What are they called on Reddit?"),
        max_length=255,
    )

    known_as = models.CharField(
        _(u"The name / speeling they are most commonly known by"),
        max_length=255,
    )

    # TODO: Consider adding
    #  - external link for more info
    #  - small bio or similar
    #  - score modifier ( So more famous people are shown more prominently )


class Post(models.Model):
    """A Post on Reddit"""

    nerdballer = models.ForeignKey(
        'NerdBaller',
    )

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

    permalink = models.CharField(
        _(u"Link where the post can be forever found"),
        max_length=255,
    )

    pub_date = models.DateTimeField(
        _(u"When it was published on Reddit"),
    )

    score= models.IntegerField(
        _(u"Reddit Score"),
        default=0,
    )

    # TODO: Consider what to do with link posts.

    def __unicode__(self):
        return self.title
