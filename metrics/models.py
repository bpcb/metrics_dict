from django.db import models

class Metric(models.Model):
	metric_name = models.CharField(max_length = 50)
	metric_text = models.TextField(max_length = 500)
	metric_description = models.TextField(max_length = 1000)
	update_date = models.DateTimeField('date updated')

	EXPERIENCE_CHOICES = (
		('ALL', 'All'),
		('Desktop', 'Desktop'),
		('Phone', 'Phone'),
		('Tablet', 'Tablet'),
		('Web', 'Web'),
		('Apps', 'Apps'),
	)

	experience = models.CharField(max_length = 10, choices = EXPERIENCE_CHOICES, default = 'All')

	def __str__(self):
		return self.metric_name
