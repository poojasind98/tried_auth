from django.contrib import admin
from django.db import router
from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter


router  = DefaultRouter()
# router.register("user",views.CustomerViewset)
router.register("prescription",views.PrescriptionViewset)

urlpatterns = [
    path('',views.health,name = 'health'),
    path('register',views.register, name = 'register'),
    path('login',views.LoginView.as_view(),name = 'login'),
    path('test',views.test,name='test')
]

urlpatterns += router.urls
