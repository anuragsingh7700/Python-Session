from flask import Flask
app = Flask(__name__)
@app.route("/")
def Home():
    return "Python is Easy!!"

app.run()
