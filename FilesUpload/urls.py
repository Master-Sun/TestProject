from django.conf.urls import url
from .views import files_upload

urlpatterns = [
    url(r'upload_dir/', files_upload),
]