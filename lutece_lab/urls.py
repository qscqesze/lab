from django.conf.urls import url
 
from . import view
 
urlpatterns = [
    url(r'.*', view.hello),
    #url(r'^login_form.html', view.hello),
    #url(r'^news.html', view.hello),
    #url(r'^$', view.hello),
]