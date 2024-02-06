# from models import *
# from twilio.rest import Client

# account_sid = 'ACc65d2d8098ee2f4216eb66fcd9580dba'
# auth_token = '844937db2ff91d18d7c71cd0a754b807'
# client = Client(account_sid, auth_token)

# for service in ServiceWork.objects.all():

#     message = client.messages.create(
#         body=f'Hi {service.customer_code.name}, tomorrow {service.service_date} is your scheduled service date.',
#         from_='+12018904884',
#         to='+919526928433'
#     )

# print(message.sid)