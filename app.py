from flask import Flask, request, send_from_directory, jsonify, render_template, redirect, url_for, session, Response, make_response, send_file

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/signup")
def signup_page():
    return render_template('signup.html')

@app.route("/login")
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)