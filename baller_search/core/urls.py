from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^$', views.MySearchView.as_view(), name='home'),
    url(r'^sh/?$', views.MySearchView.as_view(), name='search_view'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
]
