from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Transactions
from .serializers import TransactionSerializer

# Create your views here.
class AddTransactionView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)