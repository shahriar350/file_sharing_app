from django.urls import path
from . import views

urlpatterns = [
    path('download/<uuid:link>/', views.SharingDownloadView.as_view(), name='sharing_download_view'),
    path('', views.SharingView.as_view(), name='sharing_view')
]
