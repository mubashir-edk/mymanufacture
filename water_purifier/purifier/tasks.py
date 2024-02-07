# from celery import shared_task
# from twilio.rest import Client
# from .models import ServiceWork
# import datetime

# # Twilio credentials
# account_sid = ''
# auth_token = ''
# client = Client(account_sid, auth_token)

# @shared_task
# def send_service_sms():
#     # Get today's date and 9 AM
#     today = datetime.date.today()
#     nine_am = datetime.datetime.combine(today, datetime.time(8, 50))

#     # Filter ServiceWork instances with service_date at 9 AM today
#     service_works = ServiceWork.objects.filter(service_date=today)

#     for service in service_works:
#         message = client.messages.create(
#             body=f'Hi {service.customer_code.name}, today is your scheduled service date.',
#             from_='',
#             to='+919526928433'
#         )
#         print(f"SMS sent to {service.customer_code.name} - SID: {message.sid}")














# # from models import *
# # from twilio.rest import Client

# # account_sid = 'ACc65d2d8098ee2f4216eb66fcd9580dba'
# # auth_token = '844937db2ff91d18d7c71cd0a754b807'
# # client = Client(account_sid, auth_token)

# # for service in ServiceWork.objects.all():

# #     message = client.messages.create(
# #         body=f'Hi {service.customer_code.name}, tomorrow {service.service_date} is your scheduled service date.',
# #         from_='+12018904884',
# #         to='+919526928433'
# #     )

# # print(message.sid)