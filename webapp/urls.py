from django.urls import path
from . import views

urlpatterns=[
    path('getFeed', views.getFeed),
    path('postFeed', views.postFeed)
]