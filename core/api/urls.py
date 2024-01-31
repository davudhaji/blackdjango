from .views import LocationPost
from django.urls import path

urlpatterns = [
    path("location/", LocationPost.as_view()),
]
