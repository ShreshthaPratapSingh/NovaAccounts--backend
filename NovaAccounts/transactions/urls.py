from django.urls import path
from .views import AddTransactionView, UserTransactionView, TransactionDetailView

urlpatterns = [
    path("add/", AddTransactionView.as_view()),
    path("", UserTransactionView.as_view()),
    path("<int:pk>/", TransactionDetailView.as_view()),
]