from flask import Flask, request, redirect, url_for, render_template
import numpy as np
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def matrix():
    if request.method == "POST":
        dim_one1=int(request.form["dim_one1"])
        dim_one2=int(request.form["dim_one2"])
        dim_two1=int(request.form["dim_two1"])
        dim_two2=int(request.form["dim_two2"])
        matrix11=request.form["matrix1"]
        matrix22=request.form["matrix2"]
        matrix1 = matrix11.split(" ")
        matrix2 = matrix22.split(" ")
        for i in range(len(matrix1)):
            matrix1[i]=int(matrix1[i])
        for i in range(len(matrix2)):
            matrix2[i]=int(matrix2[i])
        matr1 = np.array(matrix1)
        matr2 = np.array(matrix2)
        matr1.shape = (dim_one1,dim_one2)
        matr2.shape = (dim_two1,dim_two2)
        multiplic = np.matmul(matr1,matr2)
        multiplic = list(multiplic)
        a = ""
        for x in multiplic:
            a = a + "<p>" + str(x) + "</p>"
        global result_is
        result_is = a
        return  redirect(url_for("result"))
    return render_template("matrix.html")

@app.route("/result")
def result():
    return result_is

