from django.apps import AppConfig


class SocialaxyChatConfig(AppConfig):
    name = 'socialaxy_chat'

    def ready(self):
        from . import signals
