from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
WALID_EMAIL = "dancho@gmail.com"
WALID_PASSWORD = "1234"

@app.route('/FlashCard', methods=['GET', 'POST'])
def FlashCard():
    show_id = None      #Ничего не показываем
    if request.method == 'POST':
        show_id = int(request.form["card_id"])
    return render_template('FlashCard.html', cards=cards,show_id=show_id)

cards = [
    {"id":1, "question":"Какого цвета Обама?", "answer": "Блондин"},
    {"id":2, "question":"Какова скорость света?", "answer": "299 792 458 м/с"},
    {"id":3, "question":"Кто был первым космонавтом?", "answer": "Юрий Гагарин"},
    {"id":4, "question":"Самый популярный супергерой Марвел?", "answer": "Человек паук"},
    {"id":5, "question":"Как меня зовут?", "answer":"Данияр"},
    {"id":6, "question":"Кто самый сильный человек в мире?", "answer":"Эдди Хол"},
    {"id":7, "question":"Кто самый красавчик?", "answer":"Раян Гослинг"},
    {"id":8, "question":"A?", "answer":"A?"},
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == WALID_EMAIL and password == WALID_PASSWORD:
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html', error = "НЕВЕРНЫЙ ПАРОЛЬ")


    return render_template("login.html")
@app.route('/welcome')
def welcome():                             #деф нужен для того что бы сайт показыывался
    return render_template('welcome.html')
history=[]
@app.route('/calculator', methods=["GET","POST"])
def calculator():
    expression = request.form.get("expression","")
    button = request.form.get("button","")

    if button == "AC":
        expression = ""
    elif button == "=":
        try:
            result = str(eval(expression))
            history.append(f"{expression} = {result}")
            expression = result

        except:
            result="Ошибка"
            history.append(f"{expression} = ошибка")
            expression = ""
    else:
        expression = expression + button
        result = expression
    return render_template('calculator.html', result=result,expression=expression, history=history)



if __name__ == '__main__':
    app.run(debug=True)






































