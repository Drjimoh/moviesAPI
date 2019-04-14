from django.db import models




class Movie(models.Model):
	title= models.CharField(max_length=200, blank=False)
	year = models.IntegerField(default=2019, blank=True, null=True)
	genre = models.CharField(max_length=200, blank=True, null=True)
	ratings = models.IntegerField(blank=True, null=True)


	def __str__(self):
		return self.title + ' ' + str(self.year)

