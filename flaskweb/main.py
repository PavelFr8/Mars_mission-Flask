from flask import Flask, redirect, render_template, request, url_for, session
from flaskweb.data import db_session
from forms.login import LoginForm
import os
import json
from data.users import User
from data.jobs import Jobs
from forms.registr import RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user
from forms.loginform import LoginForm
from forms.jobform import JobForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_123'
app.config['UPLOAD_FOLDER'] = 'static/img/carousel'

login_manager = LoginManager()
login_manager.init_app(app)

imgs = ['4.png', '7.png', '13.png', '17.png']


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('logs.html', jobs=jobs)


@app.route('/training/<prof>')
def training(prof):
    param = {
        'prof': prof,
    }
    return render_template('training.html', title='Тренировка', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    person = {'surname': 'Вовочкин', 'name': 'Вова', 'education': 'Низкое',
              'profession': 'Безработный', 'sex': 'Вовацераптор', 'motivation': 'Печеньки',
              'ready': 'Бог его знает...'}
    return render_template("auto_answer.html", title="Анкета", person=person)


@app.route('/list_prof/<sp>')
def list_prof(sp):
    param = {
        'sp': sp,
    }
    return render_template('list_prof.html', **param)


@app.route('/login_astro', methods=['GET', 'POST'])
def login_astro():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_astro.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    params = {
        'list': ['Скот Ридли', 'Дмитрий Нагиев', 'Лёша Вовочкин', 'Вова Лёшечкин', 'Огурец', 'Ин Су Лин'],
    }
    return render_template('distribution.html', title='По каютам!', **params)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    params = {
        'sex': sex,
        'age': age
    }
    return render_template('table.html', title='Личная каюта', **params)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'POST':
        file = request.files['file']
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        imgs.append(file.filename)
        # print(imgs)

    return render_template('carusel.html', title='Галерея', imgs=imgs)


@app.route('/member')
def member():
    with open('templates/workers.json', 'r', encoding='utf-8') as json_file:
        workers = json.load(json_file)

    return render_template('member.html', workers=workers)


@app.route('/logs')
def logs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('logs.html', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='регистрация', form=form, message='Пароли не совпадают')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='регистрация', form=form,
                                   message='такой пользователь уже есть')

        user = User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/job', methods=['GET', 'POST'])
def job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('job.html', title='Новая работа', form=form)


if __name__ == '__main__':
    db_session.global_init("db/mars.db")
    app.run(port='8080', host='127.0.0.1')
