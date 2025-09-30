from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # For now, just print to console.
        # Later, this could send an email or save to a database.
        print(f"Contact form submission from {name} <{email}>: {message}")

        return jsonify({'message': 'Your message has been sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True)