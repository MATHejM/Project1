from flask import Flask, request, redirect, url_for, render_template
import numpy as np
app = Flask(__name__)

def Multiplication(dim11,dim12,dim21,dim22,mat1,mat2):
    for i in range(len(mat1)):
        mat1[i] = int(mat1[i])
    for i in range(len(mat2)):
        mat2[i] = int(mat2[i])
    matr1 = np.array(mat1)
    matr2 = np.array(mat2)
    matr1.shape = (dim11, dim12)
    matr2.shape = (dim21, dim22)
    multiplic = np.matmul(matr1, matr2)
    multiplic = list(multiplic)
    a = ""
    for x in multiplic:
        a = a + "<p>" + str(x) + "</p>"
    return a

@app.route('/', methods=["GET", "POST"])
def matrix():
    if request.method == "POST":
        dim_one1=int(request.form["dim_one1"])
        dim_one2=int(request.form["dim_one2"])
        dim_two1=int(request.form["dim_two1"])
        dim_two2=int(request.form["dim_two2"])
        matrix1=request.form["matrix1"]
        matrix2=request.form["matrix2"]
        matrix1 = matrix1.split(" ")
        matrix2 = matrix2.split(" ")

        # Checking whether the input is correct
        if dim_one2 != dim_two1:
            return render_template("matrix2.html",message="Dimensions of the matrices are not compatible for multiplication!")
        elif (len(matrix1) != dim_one1*dim_one2) or (len(matrix2) != dim_two1*dim_two2):
            return render_template("matrix2.html",message="You entered a matrix with a number of elements that does not match the number of elements according to the given dimensions!")
        else:
            for i in range(len(matrix1)):
                if (not 47<ord(matrix1[i])<58):
                    return render_template("matrix2.html",message="The elements of matrices are not all numbers. Enter the elements again!")
            for i in range(len(matrix2)):
                if (not 47<ord(matrix2[i])<58):
                    return render_template("matrix2.html",message="The elements of matrices are not all numbers. Enter the elements again!")
            global result_is
            result_is = Multiplication(dim_one1,dim_one2,dim_two1,dim_two2,matrix1,matrix2)
            return  redirect(url_for("result"))
    return render_template("matrix2.html")

@app.route("/result")
def result():
    return result_is
