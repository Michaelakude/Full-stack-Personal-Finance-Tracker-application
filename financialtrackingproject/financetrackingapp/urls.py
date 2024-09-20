from django.urls import path, include
from rest_framework import routers
from . import views
from financetrackingapp import views

router = routers.DefaultRouter()
router.register(r'BankAccount', views.BankAccountViewSet)
router.register(r'UserAccount', views.UserAccountViewSet)

urlpatterns = [
  path('', include(router.urls))
  ]