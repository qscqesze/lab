from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    url(r'^logout', view.logout),
    url(r'^register', view.register),
    url(r'^login', view.login),
    url(r'.*', view.hello),
    #url(r'^news.html', view.hello),
    #url(r'^$', view.hello),
]