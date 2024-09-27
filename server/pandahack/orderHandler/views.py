from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recieveEcoFriendlyOrder(request):
    print("Eco Friendly Order Recieved")
    return HttpResponse("Eco Friendly Order Recieved")
