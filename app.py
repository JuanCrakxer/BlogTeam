from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Blog', methods=['GET, POST'])
def Blog():
    return render_template('Blog.html')


@app.route('/home')
def home():
    return render_template('home.html')

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
