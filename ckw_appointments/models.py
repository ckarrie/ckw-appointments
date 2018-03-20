import os
from django.db import models
from django.apps import apps
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
    description = models.TextField(null=True, blank=True)
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
    filefield = models.FileField(upload_to=upload_handlers.taskupload_handler, null=True, blank=True)

    def get_filename(self):
        return os.path.basename(self.filefield.name)

    def __unicode__(self):
        return self.title

    def get_finished_taskslogs(self):
        return self.tasklog_set.filter(status='finished')

    def get_progress_status(self):
        needed_by = self.appointment.subscribers.all()
        needed_cnt = needed_by.count()
        done_in = self.get_finished_taskslogs()
        done_by = apps.get_model('auth.User').objects.filter(id__in=done_in.values_list('log_status_by', flat=True))
        finished = needed_cnt <= done_in.count()
        return {
            'finished': finished,
            'needed_cnt': needed_cnt,
            'done_in': done_in,
            'done_by': done_by,
            'needed_by': needed_by
        }

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













