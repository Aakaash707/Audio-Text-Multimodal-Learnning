from flask import Flask, render_template, request, session, redirect, url_for
from comp1 import *
from comp2 import *
from comp3 import *
from comp4 import *
import os
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/module_1", methods = ["GET", "POST"])
def module_1():
    if request.method == "GET":
        return render_template("module_1.html")
    elif request.method == "POST":
        opp = open("/Users/aakaash_kb/Downloads/recorded_content.txt", 'r')
        inn = opp.read()
        opp.close()
        sentences = [request.form['input'], inn]
        res = find(sentences)
        res = res[0][0] * 100
        return render_template("results.html", result = res)

@app.route("/module_2", methods = ["GET"])
def module_2():
    if request.method == "GET":
        res1 = convert_audio_to_text("output.wav")
        res2 = convert_audio_to_text("output1.wav")
        res = find([res1, res2])
        res = res[0][0] * 100
        return render_template("results.html", result = res)
    
@app.route("/module_3", methods = ["GET", "POST"])
def module_3():
    if request.method == "GET":
        return render_template("module_3.html")
    elif request.method == "POST":
        inp = request.form["text_area"]
        summarize(inp)
        return render_template("home.html")

@app.route("/module_4", methods = ["GET"])
def module_4():
    if request.method == "GET":
        res = pull()
        return render_template("results.html", result = res)

if __name__ == "__main__":
    app.run(debug=True)