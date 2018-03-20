# My project's README

## Install in existing Django venv

```
virtualenv diditnow
cd virtualenv
source bin/activate

hg clone https://bitbucket.org/ckarrie/ckw-appointments
pip install -e ckw-appointments
pip install django==1.11.9 django-mptt-nomagic django-mptt psycopg2 django-rest-framework

django-admin startproject diditnow_app
```


## settings.py

* Add to INSTALLED_APPS:
  * ```django.contrib.humanize```
  * ```django.contrib.site```
  * ```ckw_appointments``` 
* ```ROOT_URLCONF = 'ckw_appointments.urls_singleapp'```




