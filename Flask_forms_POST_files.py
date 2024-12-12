from flask import Flask, render_template, request, Response, send_from_directory, jsonify
import pandas as pd
import os, time

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('file_upload.html')
    elif request.method == 'POST':
        username = request.form['Username']
        password = request.form.get('Password')
        if username == 'Bhanuprakash' and password == 'Iamironman':
            return 'Success'
        else:        
            return 'failed'

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['files']
    fname = file.filename
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return fname, df.to_html()

@app.route('/download', methods=['POST'])
def convertcsv():
    excel = request.files['files']
    df = pd.read_excel(excel)
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={'Content-Disposition':'attachment ; filename=result.csv'}  # mandatory..!
    )
    return response

@app.route('/convertcsv_two', methods=['POST'])
def convertcsv_two():
    file = request.files['files']
    df = pd.read_excel(file)
    os.makedirs('downloads', exist_ok=True)
    fname = f'{str(int(time.time())).split()[0]}.csv'
    df.to_csv(os.path.join('downloads', fname))
    return render_template('download.html', filename=fname)

@app.route('/downloadfile/<filename>')
def downloadfile(filename):
    return send_from_directory('downloads', filename, download_name='final.csv')

#----------------------------------------------------------------------------------

@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greetings']
    name = request.json['name']
    with open('file.txt', 'w') as f:
        f.write(f"{greeting}, {name}")
    return jsonify({'message':'Sucessfully returned'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7998, debug=True)