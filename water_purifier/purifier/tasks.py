# from celery import Celery
# from datetime import datetime
# from .sms_utils import send_sms
from .models import ServiceAssign

print(ServiceAssign)

# app = Celery('water_purifier')

# @app.task
def send_scheduled_sms():
    # scheduled_dates = ServiceAssign.objects.filter(scheduled_date__time=datetime.strptime('11:15', '%H:%M').time())
    scheduled_dates = ServiceAssign.objects.all()
    print(scheduled_dates)

    # for entry in scheduled_dates:
    #     message = f"Your scheduled message: {entry.message}"
    #     send_sms(message, entry.phone_number)

send_scheduled_sms()