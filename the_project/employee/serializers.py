from rest_framework import serializers
from .models import employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        # abstract = True
        model = employee
        fields = ['id', 'name', 'age', 'salary']
