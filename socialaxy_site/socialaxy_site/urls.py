from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('socialaxy_main_page.urls')),
    url(r'', include('socialaxy_coming_soon_page.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

