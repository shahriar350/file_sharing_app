from django.urls import path
from . import views

urlpatterns = [
    path('', views.SharingView.as_view(), name='sharing_view')
]
