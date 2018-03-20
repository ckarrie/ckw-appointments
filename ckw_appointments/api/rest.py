from django.utils import timezone
from rest_framework import serializers, generics
from django.apps import apps


class TaskLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('ckw_appointments.TaskLog')
        fields = ['task', 'status', 'log_status_by', 'log_status_at', ]


class CreateTaskLogEntryView(generics.CreateAPIView):
    queryset = apps.get_model('ckw_appointments.TaskLog').objects.all()
    serializer_class = TaskLogSerializer

    def get_serializer(self, *args, **kwargs):
        data = kwargs.get('data', {}).copy()
        data.update({
            'log_status_by': self.request.user.id,
            'log_status_at': timezone.now()
        })
        kwargs['data'] = data
        return super(CreateTaskLogEntryView, self).get_serializer(*args, **kwargs)

    




