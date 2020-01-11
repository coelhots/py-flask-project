from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin_form')
def login():
    return render_template('signin.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')

    return render_template('thankyou.html', firstName=firstName, lastName=lastName)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
