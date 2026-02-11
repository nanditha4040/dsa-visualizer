from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

def generate_array():
    return [random.randint(1, 15) for _ in range(8)]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        arr = generate_array()
        return redirect(url_for("show_array", data=",".join(map(str, arr))))

    return render_template("index.html", array=None, animate=False)

@app.route("/show/<data>")
def show_array(data):
    arr = list(map(int, data.split(",")))
    return render_template("index.html", array=arr, animate=True)

app.run(debug=True)
