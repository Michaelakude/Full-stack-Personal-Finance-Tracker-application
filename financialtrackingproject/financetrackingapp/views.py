from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.views.generic import TemplateView
# Create your views here.



class IndexView(TemplateView):
    template_name = "index.html"


class BankAccountViewSet(viewsets.ModelViewSet):
  serializer_class = BankAccountSerialzer
  queryset = BankAccount.objects.all()

class UserAccountViewSet(viewsets.ModelViewSet):
  serializer_class = UserCreateSerializer
  queryset = UserAccount.objects.all()