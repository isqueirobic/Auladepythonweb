from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index(): # nomear a função e html para contatenar mehlor no final
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/produto')
def produto():
    return render_template('produto.html')


if __name__ == '__main__':
    app.run(debug=True)
