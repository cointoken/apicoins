from celery import Celery
from sqlalchemy import create_engine
from datetime import datetime

worker  = Celery('worker')
worker.config_from_object('tasks.celeryconfig')