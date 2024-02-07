# # celery.py

# import os
# from celery import Celery
# from celery.schedules import crontab

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'water_purifier.settings')

# app = Celery('water_purifier')

# # Using a string here means the worker doesn't have to serialize the configuration object to child processes.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'send-service-sms-every-day': {
#         'task': 'purifier.tasks.send_service_sms',
#         'schedule': crontab(hour=8, minute=50),  # Runs every day at 9 AM
#     },
# }
