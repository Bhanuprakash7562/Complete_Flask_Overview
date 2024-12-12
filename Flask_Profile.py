from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def portfolio():
    data = {
        'name': 'Bhanuprakash Kocharla',
        'title': 'Software Engineer',
        'about': "Highly skilled Python developer with over 2 years of experience in backend development, specializing in database engineering, data warehousing, data extraction, and data processing. Proficient in various Python frameworks, including Pandas, NumPy, Matplotlib, Scikit-learn, Flask, FastAPI, and Django. Experienced in utilizing Amazon Cloud services, such as AWS EC2, S3, Lambda, and IAM. Additionally, well-versed in Linux environments and shell scripting. Works at fast pace to meet tight deadlines. Enthusiastic team player ready to contribute to company success.",
        'skills': ['Python', 'Flask', 'Django', 'SQL','MySQL', 'AWS Cloud Services', 'AWS EC2', 'AWS Lambda','AWS S3','AWS IAM','Machine Learning','Exploratory Data Analysis','HTML', 'CSS', 'Git'],
        'experience': [
            {
                'title': 'Software Engineer',
                'company': 'Stellar Innovations Private Limited',
                'period': 'April 2024 - Present',
                'description': 'Description of your role and achievements'
            },
            {
                'title': 'Junior Software Engineer',
                'company': 'Stellar Innovations Private Limited',
                'period': 'December 2022 - April 2024',
                'description': 'Description of your role and achievements'
            }
        ],
        'education': [
            {
                'degree': 'Bachelor of Technology in Electrical and Electronics Engineering',
                'institution': 'Damisetty Bala Suresh Institute of Technology',
                'period': '2019 - 2022',
                'description': 'Relevant coursework and achievements'
            }
        ],
        'email': 'banuprakash2326@gmail.com',
        'phone': '+91-8074967810',
        'location': 'Nellore, India'
    }
    
    return render_template('profile.html', **data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)