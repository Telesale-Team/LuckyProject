from django.urls import path,include
from .views import *
urlpatterns = [
    
	path('',Home,name='home'),
    path('data-table/',Lucky_Random,name='data-teble'),
    path('import-data/',Import_data,name='import'),
    path('add-reward/<str:no>',Add_Reward,name='add-reward'),
    path('save-data',Save,name='save-data')

]