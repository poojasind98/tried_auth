from rest_framework import serializers
from .models import Customer,Prescription
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username' , 'email' , 'password' , 'gender' , 'date_of_birth']
        extra_kwargs = {'password':{'write_only' : True}}

        def create(self, validated_data):
            customer = Customer(
                username = validated_data['username'],
                email = validated_data['email'],
                gender = validated_data['gender'],
                date_of_birth = validated_data['date_of_birth']

            )
            customer.set_password(validated_data['password'])
            customer.save()
            return customer

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'