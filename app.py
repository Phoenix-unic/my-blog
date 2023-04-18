from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/cover')
def cover():
    return render_template('cover.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')



if __name__ == '__main__':
    app.run(debug=True)












