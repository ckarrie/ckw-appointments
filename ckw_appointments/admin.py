from django.contrib import admin
import models

from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


class AppointmentTaskAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title',) + (
        'title', 'urgency', 'time_planned', 'time_taken')
    readonly_fields = ('level',)
    list_display_links = (
        'indented_title',
    )

admin.site.register(models.AppointmentApp)
admin.site.register(models.Appointment)
admin.site.register(models.AppointmentTask, AppointmentTaskAdmin)
admin.site.register(models.AppointmentUpload)
admin.site.register(models.TaskLog)
