import django_filters
from .models import *

class User_Data_Filter(django_filters.FilterSet):

	class Meta:
		model = Round_Tauthong
		fields = '__all__'