import uvicorn
from fastapi import FastAPI, BackgroundTasks
from send_email import send_email_background

app = FastAPI(title='Как отправить электронное письмо')


@app.get('/')
def index():
    return 'Sending messages by email - http://127.0.0.1:8000/docs'


@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks)
    return 'Success'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
