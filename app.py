from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return f'Thank you, {name}. Your message has been received!'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
