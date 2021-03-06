import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.generic.websockets import WebsocketDemultiplexer

from .models import Thread, UnreadThread, Message, MessageBinding


@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True
        })
    })


@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('users').discard(message.reply_channel)


class WsThread(WebsocketDemultiplexer):
    http_user = True

    consumers = {
        'messages': MessageBinding.consumer,
    }

    def connection_groups(self, thread):
        if Thread.objects.filter(pk=thread, users=self.message.user):
            return ['thread-%s' % thread]
        return []

    def receive(self, content, **kwargs):
        if 'text' in content:
            thread_id = int(kwargs.get('thread'))
            message = Message(
                thread_id=thread_id,
                user=self.message.user,
                text=content.get('text')
            )
            if message and message.thread.users.filter(pk=message.user.pk):
                message.save()

                # Create unread thread for each user in thread,
                # we will delete it latter.
                for user in message.thread.users.all():
                    UnreadThread.objects.get_or_create(
                        thread_id=thread_id,
                        user=user
                    )
        elif 'read' in content:
            # The message was delivered - delete user's unread thread.
            UnreadThread.objects.filter(
                thread_id=int(kwargs.get('thread')),
                user=self.message.user
            ).delete()
