from django.conf.urls import url

from audioselector import views

urlpatterns = [
    url(r'upload$', views.model_form_upload, name="upload_form")
]