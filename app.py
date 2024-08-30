from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/Blog')
def blog():
    return render_template('Blog.html')

@app.route('/gallery')
def gallery():
    return render_template('Gallery.html') 

@app.route('/contacts')
def contacts():
    return render_template('Contacts.html')  

@app.route('/game')
def game():
    return render_template('Game.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
