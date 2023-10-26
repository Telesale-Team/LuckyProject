from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Permission (models.Model):
	MedalType = models.TextChoices("MedalType", "lv1 lv2 lv3 lv4 lv5")
	lv = models.CharField(choices=MedalType.choices, max_length=4)
	


class ProfileUser(models.Model):
	 
	username = models.OneToOneField(User,on_delete=models.CASCADE)
	permission = models.ForeignKey(Permission,on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	phone = models.CharField(max_length=10)
	MedalType = models.TextChoices("MedalType", "Line Facebook Phone Telegram etc.,")
	contact = models.CharField(choices=MedalType.choices, max_length=10)
	notice = models.CharField(max_length=255)

	def __str__(self) -> str:
		return self.username