from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('socialaxy_main_page.urls')),
    url(r'^chat/', include('socialaxy_chat.urls', namespace='socialaxy_chat')),
    url(r'^soon/', include('socialaxy_coming_soon_page.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
