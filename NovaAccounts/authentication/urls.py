from django.urls import path, include
from .views import ProfileView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
]
