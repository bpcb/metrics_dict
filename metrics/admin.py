from django.contrib import admin

from .models import Metric

class MetricAdmin(admin.ModelAdmin):
	list_display = ('metric_name', 'metric_description', 'experience')
	search_fields = ['metric_name', 'metric_description']
	ordering = ['metric_name']

admin.site.register(Metric, MetricAdmin)