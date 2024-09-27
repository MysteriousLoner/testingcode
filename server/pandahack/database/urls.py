from django.urls import path
from . import views

urlpatterns = [
    path('getRewards/', views.getRewards),
    path('decreaseBambooCount/', views.decreaseBambooCount),
    path('queryBambooCount/', views.queryBambooCount),
    path('receiveOrder/', views.receiveOrder),
    path('startFlawedDemocracy/', views.startFlawedDemocracy),
    path('cleardb/', views.aryanRaceGo),
    path('initiate-pairs/', views.initiate_pairs),
    path('update-pairs/', views.update_pairs),
]