# from sms import Message

# message = Message(
#     'Here is the message',
#     '+9833472041',
#     ['+9082892339']
# )
# message()

from sms import send_sms

send_sms(
    'Here is the message',
    '+9833472041',
    ['+9082892339']
    # fail_silently=False
)