from email.message import EmailMessage
import smtplib
import ssl

password = open("senha", 'r').read()
# print(passwprd)
from_email = 'pythonteste777@gmail.com'
to_email = 'matheusaraujoguerra2603@outlook.com'
subject = 'Curso Python'

body = '''
A melhor forma de prever o futuro é criá-lo.
Aprendendo a Linguagem Python.
'''

# 1 - Estruturando a mensagem via e-mail
message = EmailMessage()
message['from'] = from_email
message['to'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 2 - Envio de email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )