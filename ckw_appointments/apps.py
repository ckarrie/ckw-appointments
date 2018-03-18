import datetime

from django.apps import AppConfig

__author__ = 'ckw'


class DefaultCKWAppointmentsConfig(AppConfig):
    name = 'ckw_appointments'
    verbose_name = 'CKW Appointments'

    def ready(self):
        super(DefaultCKWAppointmentsConfig, self).ready()
        # import signal handlers
        import signals
        signals.register_signals(config=self)
