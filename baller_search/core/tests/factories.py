import factory


class NerdBallerFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user-{0}'.format(n))
    known_as = factory.Sequence(lambda n: 'known_as-{0}'.format(n))

    class Meta:
        model = 'core.NerdBaller'
        django_get_or_create = ('username', )


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'core.Post'
