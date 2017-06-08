from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

app.run(debug=True)
# Nothing after the debug line will be read.
