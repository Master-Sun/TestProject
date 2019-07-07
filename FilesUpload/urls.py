from django.conf.urls import url, include
from django.contrib import admin
from .views import files_upload

urlpatterns = [
    url(r'upload_dir/', files_upload),
]