import os
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from dotenv import load_dotenv

load_dotenv('.env')

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_FROM=os.getenv('MAIL_FROM'),
    MAIL_PORT=os.getenv('MAIL_PORT'),
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_FROM_NAME=os.getenv('MAIL_FROM_NAME'),
    MAIL_STARTTLS=os.getenv('MAIL_STARTTLS'),
    MAIL_SSL_TLS=os.getenv('MAIL_SSL_TLS'),
)



def send_email_background(background_tasks: BackgroundTasks):
    message = MessageSchema(
        subject='Тестовое сообщение',
        recipients=[''], # Укажите почту кому отправляем
        body='Вы получили это тестовое сообщение',
        subtype='html',
    )

    fm = FastMail(conf)

    background_tasks.add_task(
        fm.send_message, message, template_name='')
