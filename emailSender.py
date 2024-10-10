# se crea una función para enviar el correo 
# parametros de entrada: 
# - asunto del correo (subject)
# - contenido del correo (body)
# - los datos de la cuenta de correo electrónico Gmail (user)
# - la contraseña de acceso del correo (pwd) 
# - la dirección de correo electrónico a la que queremos notificar (recipient)
import os


def send_email(subject, body, recipient='cuya210@gmail.com'):
    
    import smtplib
    from email.mime.text import MIMEText

    #Se obtiene el email y contraseña
    user= os.getenv('EMAIL_USER')
    pwd= os.getenv('PASSWORD_USER')

    #contenido del correo
    msg = MIMEText(body)
    
    #el asunto del correo
    msg['Subject'] = subject
    
    #remitente del correo
    msg['From'] = user
    
    #correo destino
    msg['To'] = recipient

   

    try:
        #se utiliza with para que se cierre atmaticamente la conexión con el servidor SMTP
        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as server:
            
            #se envía el comando EHLO al servidor SMTP para identificar al cliente y solicitar capacidades adicionales 
            #inicia la comunicación con el servidor.)
            server.ehlo()
            
            #se inicia el cifrado TLS para asegurar la conexión entre tu aplicación y el servidor SMTP
            #asegura la conexión cifrando la comunicación.
            server.starttls()
            
            #autentica al usuario con su nombre de usuario y contraseña
            server.login(user, pwd)
            
            #se envia el correo
            server.sendmail(user, recipient, msg.as_string())
            
        print('Se envió el correo correctamente')
        
    except smtplib.SMTPAuthenticationError:
        print('Error de autenticación')
        
    except smtplib.SMTPRecipientsRefused:
        print('El destinatario rechazó el mensaje')
 
    except smtplib.SMTPSenderRefused:
        print('El remitente fue rechazado')
        
    except smtplib.SMTPException as e:
        print(f'Error SMTP: {e}')
        
    except Exception as e:
        print(f'Fallo el envío de correo: {e}')
        