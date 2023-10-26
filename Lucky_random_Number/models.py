from django.db import models

# Create your models here.
class Round (models.Model):
	name = models.CharField(max_length=3,primary_key=True)
	date = models.DateTimeField(auto_now_add=True)
	image =  models.ImageField(upload_to='media/image_tauthong',default='default.jpg',null=True,blank=True)

	class Meta:
			ordering = ["name"]
			verbose_name_plural = "Round Table "
			verbose_name = "Round"
	def __str__(self):
		return self.name

class Data (models.Model):

	no = models.CharField(max_length=4,primary_key=True)

	class Meta:
		ordering = ["no"]
		verbose_name_plural = "Data Table "
		verbose_name = "Data"

	def __str__(self):
		return self.no

class Round_Tauthong (models.Model):
	
	round =  models.ForeignKey(Round,on_delete=models.CASCADE)
	member = models.CharField(max_length=20)
	number = models.CharField(max_length=4)		
	date = models.DateField(auto_now_add=True,null=True,blank=True)
	check = models.BooleanField(default=True,blank=True,null=True)

	class Meta:
		ordering = ["number"]
		verbose_name_plural = "Round Tauthong"
		verbose_name = "Round"


	def __str__(self) :
		return str(self.number)