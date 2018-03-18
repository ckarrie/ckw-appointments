import os

from django.utils import timezone
from django.utils.text import slugify


def taskupload_handler(instance, filename):
    file_root, file_ext = os.path.splitext(filename)
    new_fn = "ckw_appointments/%(app_pk)s/%(subfolder)s/%(pk)s/%(dt)s/%(fn)s" % {
        'app_pk': str(instance.appointment.app.id),
        'subfolder': 'employee_documents',
        'dt': timezone.now().strftime('%Y_%m_%d'),
        'fn': slugify(file_root) + file_ext,
        'pk': str(instance.id),
    }

    return new_fn