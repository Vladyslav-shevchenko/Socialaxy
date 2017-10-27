from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chat/', include('socialaxy_chat.urls', namespace='socialaxy_chat')),
    url(r'^', include('socialaxy_coming_soon_page.urls', namespace='socialaxy_coming_soon')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
