from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    url(r'^news.html', view.news),
    url(r'^$', view.hello),
]