from flask import Flask, render_template, session

app = Flask(__name__, template_folder='templates')
app.secret_key = 'some key'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('session.html', message='root func')

@app.route('/set_data', methods=['GET', 'POST'])
def set_data():
    session['name'] = 'bhanu'
    session['greet'] = 'Hi Good evening'
    return render_template('session.html', message='session message')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7997, debug=True)