from celery import Celery

app  = Celery('getaddress')
app.config_from_object('app.config')