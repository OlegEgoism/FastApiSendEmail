import os
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from dotenv import load_dotenv

load_dotenv('.env')


class Envs:
    MAIL_USERNAME = 'shukay.by@gmail.com'
    MAIL_PASSWORD = 'dexk ohge anvu lnwt'
    MAIL_FROM = 'shukay.by@gmail.com'
    MAIL_PORT = 587
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_FROM_NAME = 'Shukay'


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
import html
def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: str):
    # body_str = html.unescape(body)  # Serialize the dictionary to a string
    body_str = """
    <html>
    <body>
    <h1>Приветствую вас!</h1>
    <h3>Вы получили это письмо, потому что зарегистрировались на нашем сайте - shukay.by</h3>
    <h3><font color="red">Если это не вы,</font> пожалуйста свяжитесь со службой поддержки сайта - shukay.by@gmail.com</h3>
    <h2>Спасибо за регистрацию!</h2>
    </body>
    </html>
    """

    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body_str,  # Pass the serialized string instead of the dictionary
        subtype='html',
    )

    fm = FastMail(conf)

    background_tasks.add_task(
        fm.send_message, message, template_name='email.html')