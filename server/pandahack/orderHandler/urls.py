from django.urls import path
from . import views

urlpatterns = [
    path('sendEcoFriendlyOrder/', views.recieveEcoFriendlyOrder),
]