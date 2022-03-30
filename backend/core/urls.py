from django.urls import path
from .views import PersonViewSet

urlpatterns = [
    path('all-list/', PersonViewSet.as_view()),
]
