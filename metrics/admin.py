from django.contrib import admin

from .models import Metric, Definition

class DefinitionInline(admin.TabularInline):
	model = Definition
	extra = 0

class MetricAdmin(admin.ModelAdmin):
	list_display = ('metric_name', 'metric_description')
	search_fields = ['metric_name', 'metric_description']
	ordering = ['metric_name']

	inlines = [DefinitionInline]

admin.site.register(Metric, MetricAdmin)