from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('submit.html', name=name, email=email)

if __name__ == '__main__':
    # Bind to 0.0.0.0 so Flask is accessible outside the container
    app.run(host="0.0.0.0", port=5000, debug=True)
