import os
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from dotenv import load_dotenv

load_dotenv('.env')


class Envs:
    MAIL_USERNAME = 'olegpustovalov220@gmail.com'
    MAIL_PASSWORD = 'iqzu cake sfwf hllj'
    MAIL_FROM = 'olegpustovalov220@gmail.com'
    MAIL_PORT = 587
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_FROM_NAME = os.getenv('MAIN_FROM_NAME')


conf = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT,
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    TEMPLATE_FOLDER='templates/'
)



async def send_email_async(subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype='html',
    )

    fm = FastMail(conf)

    await fm.send_message(message, template_name='email.html')


# def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
#     message = MessageSchema(
#         subject=subject,
#         recipients=[email_to],
#         body=body,
#         subtype='html',
#     )
#
#     fm = FastMail(conf)
#
#     background_tasks.add_task(
#         fm.send_message, message, template_name='email.html')


import json

def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
    body_str = json.dumps(body)  # Serialize the dictionary to a string
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body_str,  # Pass the serialized string instead of the dictionary
        subtype='html',
    )

    fm = FastMail(conf)

    background_tasks.add_task(
        fm.send_message, message, template_name='email.html')