import os
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckw_appointments.utils import upload_handlers
from django.utils.translation import ugettext_lazy as _


class AppointmentApp(models.Model):
    title = models.CharField(max_length=255)
    read_groups = models.ManyToManyField('auth.Group')
    site = models.ForeignKey('sites.Site', null=True, blank=True)
    overview_days = models.PositiveIntegerField(default=7)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('App')
        verbose_name_plural = _('Apps')


class Appointment(models.Model):
    app = models.ForeignKey(AppointmentApp)
    title = models.CharField(max_length=255)
    description = models.TextField()
    begin_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    subscribers = models.ManyToManyField('auth.User')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')


class AppointmentTask(MPTTModel):
    appointment = models.ForeignKey(Appointment)
    title = models.CharField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True)
    urgency = models.IntegerField(choices=(
        (0, 'low'),
        (50, 'mid'),
        (100, 'high')
    ))

    time_planned = models.FloatField(null=True, blank=True)
    time_taken = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')


class TaskLog(models.Model):
    task = models.ForeignKey(AppointmentTask)
    log_status_by = models.ForeignKey('auth.User')
    log_status_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=(
        ('started', 'started'),
        ('not_required', 'not required'),
        ('not_possible', 'not possible'),
        ('finished', 'finished'),
    ))

    class Meta:
        verbose_name = _('Task Log')
        verbose_name_plural = _('Task Logs')


class AppointmentUpload(models.Model):
    task = models.ForeignKey(AppointmentTask, null=True, blank=True)
    appointment = models.ForeignKey(Appointment)
    filefield = models.FileField(upload_to=upload_handlers.taskupload_handler)
    uploaded_by = models.ForeignKey('auth.User')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_filename(self):
        return os.path.basename(self.filefield.name)

    class Meta:
        verbose_name = _('Upload')
        verbose_name_plural = _('Uploads')











