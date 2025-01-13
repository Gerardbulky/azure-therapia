from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/appointment')
def appointment():
    return render_template("appointment.html")

@app.route('/blog')
def blog():
    return render_template("servblogices.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/feature')
def feature():
    return render_template("feature.html")

@app.route('/service')
def service():
    return render_template("service.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/testimonials')
def testimonials():
    return render_template("testimonials.html")

@app.route('/404')
def error():
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)