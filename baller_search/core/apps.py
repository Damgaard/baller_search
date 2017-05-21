from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from core.models import Post
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
