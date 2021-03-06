from flask import Flask, render_template

app = Flask(__name__, static_folder="../build/static", template_folder="../build")

@app.route("/")
def root():
    return render_template('index.html')

app.debug=True
app.run(host='0.0.0.0')