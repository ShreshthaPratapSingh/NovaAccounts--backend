from rest_framework import serializers
from .models import Transactions

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "_all_"
        read_only_fields = ('user',)