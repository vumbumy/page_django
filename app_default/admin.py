from django.contrib import admin

from app_default.models import Project, Job, History


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company', 'env', 'description', 'started', 'ended']
    list_editable = ['name', 'company', 'env', 'description', 'started', 'ended']
    # raw_id_fields = ['subscriber']


class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'description', 'started', 'ended']
    list_editable = ['company', 'description', 'started', 'ended']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer']
    list_editable = ['question', 'answer']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(History, HistoryAdmin)
