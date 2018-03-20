from collections import OrderedDict
from datetime import timedelta

from django.utils import timezone
from django.views import generic
import models


class AppIndexView(generic.ListView):
    template_name = 'ckw_appointments/materializedcss/index.html'
    queryset = models.AppointmentApp.objects.all()

    def get_queryset(self):
        qs = super(AppIndexView, self).get_queryset()
        if not self.request.user.is_authenticated():
            return qs.none()


        is_staff = self.request.user.is_staff
        for app in qs:
            app.appointments_by_days = OrderedDict()
            today = timezone.now().date()
            end_day = today + timedelta(days=app.overview_days)
            upcoming_appintments = app.appointment_set.filter(
                begin_dt__date__range=(today, end_day),
                subscribers__in=[self.request.user]
            )

            if not is_staff:
                upcoming_appintments = upcoming_appintments.filter(
                    subscribers__in=[self.request.user]
                )

            app.upcoming_appintments = upcoming_appintments
            for i in range(app.overview_days):
                current_day = today + timedelta(days=i)
                appointments_by_day = app.upcoming_appintments.filter(
                    begin_dt__date=current_day
                )
                if appointments_by_day.exists():
                    app.appointments_by_days[current_day] = appointments_by_day

                    for appointment_by_day in appointments_by_day:
                        appointment_by_day.tasks = appointment_by_day.appointmenttask_set.all()
                        for task in appointment_by_day.tasks:
                            task.is_finished = task.get_finished_taskslogs().filter(log_status_by=self.request.user).exists()

        return qs




