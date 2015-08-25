from django.db import models
from datetime import datetime

class Metric(models.Model):
	metric_name = models.CharField(max_length = 50)
	metric_description = models.TextField(max_length = 1000)

	def __str__(self):
		return self.metric_name

class Definition(models.Model):
	metric = models.ForeignKey(Metric)
	sql = models.TextField(max_length = 1000)
	start_date = models.DateField('Definition start date', default = datetime.now().date())
	end_date = models.DateField('Definition end date', default = None, null =True)
	is_active = models.BooleanField(default = True)

	EXPERIENCE_CHOICES = (
		('ALL', 'All'),
		('Desktop', 'Desktop'),
		('Phone', 'Phone'),
		('Tablet', 'Tablet'),
		('Web', 'Web'),
		('Apps', 'Apps'),
	)

	experience = models.CharField(max_length = 10, choices = EXPERIENCE_CHOICES, default = 'All')
