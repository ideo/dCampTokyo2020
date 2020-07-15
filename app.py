from flask import Flask, render_template, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5004)
