from math import perm
import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Customer,Prescription
from .serializers import CustomerSerializer, PrescriptionSerializer
from rest_framework.decorators import api_view,permission_classes
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework import permissions 
from rest_framework.authentication import TokenAuthentication
# Create your views here.


@api_view(['GET'])
def health(request):
    return Response(
        {
            'message' : "Health Check Successful"
        }, status = 200
    )


class LoginView(KnoxLoginView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        return super(LoginView,self).post(request, format=None)


@api_view(['POST'])
def register(request):
    try:
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
                    "message" : "User Registered successsfully"
                },status = 201)
    
    except Exception as e:
        return Response({
            'message' : e.__str__()
        },status= 400)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def test(request):
    return Response({
        'message' : 'Successfully accessed'
    }, status = 200)


class CustomerViewset(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            return Response({
                "message" : "User Registered successsfully"
            },status = 201)
        else:
            return response



class PrescriptionViewset(ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
