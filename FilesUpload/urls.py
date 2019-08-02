from django.conf.urls import url
from .views import files_upload, send_email

urlpatterns = [
    url(r'upload_dir/', files_upload),
    url(r'send_email/', send_email),
]