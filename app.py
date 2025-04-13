from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, gaes!"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama anda adalah {}".format(nama)

@app.route('/user/<name>')  
def user(name):
    return f"Hello, {name}!"

@app.route('/user/<int:user_id>')  
def user_id(user_id):
    return f"User ID: {user_id}"

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', username=name)

if __name__ == "__main__":
    app.run(debug=True)