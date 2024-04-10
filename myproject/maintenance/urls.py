from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Home,name='home'),
    path('senrepair',Sent_repair,name='senrepair'),
    path('orders',OrdersList,name='orders'),
    path('updatestatus/<str:orderid>/<str:status>/',UpdateStatusOrder,name='updatestatus'),
    path('blogs',Posts,name='post'),
    
]