import datetime
from django.core.cache import cache
from django.conf import settings


def active_user_middleware(get_response):

    def middleware(request):
        current_user = request.user
        if request.user.is_authenticated():
            now = datetime.datetime.now()
            cache.set('seen_%s' % current_user.username, now,
                      settings.USER_LASTSEEN_TIMEOUT)

        return get_response(request)

    return middleware
