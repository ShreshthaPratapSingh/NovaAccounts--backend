from django.urls import path
from .views import AddTransactionView

urlpatterns = [
    path("add/", AddTransactionView.as_view()),
]