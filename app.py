from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'apps.cedric@gmail.com'
app.config['MAIL_PASSWORD'] = 'Patcherian12'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_DEFAULT_SENDER'] = ('All Engineering Solutions','apps.cedric@gmail.com')
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route('/')
def index():
    return 'Welcome aboard!'

@app.route('/bulk')
def bulk():
    users = [{'name': 'Xelopit', 'email': 'xelopit387@mailreds.com'},
             {'name': 'Joyanne', 'email': 'joyanne@freadingsq.com'}]

    with mail.connect() as conn:
        for user in users:
            msg = Message('Another Group Email', recipients=[user['email']])
            msg.html = '<h4>You have recived this email because you are part of a mailing list</h4>'
            with app.open_resource('uploads/img/pic.jpg') as img:
                msg.attach('pic.jpg', 'image/jpg', img.read())
            conn.send(msg)

        return 'Emails sent to group!'


if __name__ == '__main__':
    app.run(debug=True)
