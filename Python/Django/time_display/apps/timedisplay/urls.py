from django.conf.urls import url
from . import views           # This line is new!
# Models -- Views -- Templates
urlpatterns = [
    url(r'^$', views.index)
]
