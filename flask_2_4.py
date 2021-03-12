from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import glob

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class LoginForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('Войти')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    f = form.photo.data
    images_list = []
    for i in glob.glob('static/img/*'):
        images_list.append(i.split('\\')[-1])
    len_list = len(images_list)
    if form.validate_on_submit():
        images_list = []
        for i in glob.glob('static/img/*'):
            images_list.append(i.split('\\')[-1])
        len_list = len(images_list)
        name_file = 'static/img/' + str(secure_filename(f.filename))
        with open(name_file, 'wb') as file:
            file.write(f.read())
    return render_template('login_2.html', title='Пейзажи Марса', images_list=images_list, len_list=len_list, form=form)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')