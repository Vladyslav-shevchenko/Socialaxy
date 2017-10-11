from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.coming_soon_page, name='coming_soon_page'),
]
