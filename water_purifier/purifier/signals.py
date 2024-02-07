# from models import *
# from twilio.rest import Client

# account_sid = '......'
# auth_token = '......'
# client = Client(account_sid, auth_token)

# for service in ServiceWork.objects.all():

#     message = client.messages.create(
#         body=f'Hi {service.customer_code.name}, tomorrow {service.service_date} is your scheduled service date.',
#         from_='',
#         to=''
#     )

# print(message.sid)