from email.message import EmailMessage
import smtplib
import ssl
import mimetypes 


password = open('senha', 'r').read()
from_email = 'pythonteste777@gmail.com'
to_email = 'matheusaraujoguerra2603@outlook.com'
subject = 'Proposta de parceria customizada'
body = open('files/index.html.txt', 'r', encoding='utf-8').read()

# 1 - monstrando estrutura do email

message = EmailMessage()
message['from'] = from_email
message['to'] = to_email
message['Subject'] = subject

message.set_content(body, subtype='html')
safe = ssl.create_default_context()

# 2 - Adicionar anexo

anexo = 'files/corpo.txt'
# print(mimetypes.guess_type(anexo)[0])
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )
    
    # 3 - Envio de email

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )

