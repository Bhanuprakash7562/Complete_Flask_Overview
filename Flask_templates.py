from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/home', methods=['GET', 'POST'])
def home():
    name = 'bhanu'
    lang = 'python'
    ll = [10,20,30,40,50,60,70]
    return render_template('index.html', name=name, lang=lang, lis=ll)

@app.route('/temptut', methods=['GET', 'POST'])
def index():
    ll = [10,20,30,40,50,60,70]
    return render_template('homepage.html', lis=ll)

@app.route('/filter', methods=['GET', 'POST'])
def filters():
    text = "Hello world"
    return render_template('filters.html', txt=text)

# Creating custom filters (Note: Go through 'filters' fuction for reference)
@app.template_filter('reverse_str')
def reverse_str(s):
    return s[::-1]

# Redirecting to other functions from one functions
@app.route('/redirect_url')
def redirect_url():
    return redirect(url_for('filters'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7999, debug=True)