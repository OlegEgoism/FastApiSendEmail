import uvicorn
from fastapi import FastAPI, BackgroundTasks
from send_email import send_email_background, send_email_async

app = FastAPI(title='How to Send Email')


@app.get('/')
def index():
    return 'Hello World'


@app.get('/send-email/asynchronous')
async def send_email_asynchronous():
    await send_email_async('Hello World', 'gpttest1988@gmail.com', {
        'title': 'Hello World',
        'name': 'John Doe'
    })
    return 'Success'

@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks,
                          'Регистрация на сайте shukay.by',
                          'gpttest1988@gmail.com',
                          body='Приветствую вас. Вы получили это электронное письмо, поскольку указали свою электронную почту при регистрации на сайте shukay.by <br> Если это не вы, пожалуйста свяжитесь со службой поддержки сайта shukay.by@gmail.com'
    )
    return 'Success'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)