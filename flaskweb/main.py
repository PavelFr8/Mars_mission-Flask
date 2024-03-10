from flask import Flask, redirect, render_template
from forms.login import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_123'


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


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


if __name__ == '__main__':
    app.run(port='8080', host='127.0.0.1')