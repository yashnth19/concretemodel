# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:04:54 2022

@author: Yreddy
"""

from flask import Flask, render_template, request
import ML_model

app=Flask(__name__)


@app.route("/")
def hello():
    # return "hello world"
    return render_template("index.html")
 
@app.route("/sub",methods=["POST"])
def submit():
    #data from html to py
    if request.method == "POST":
        ce=request.form["cement"]
        sl=request.form["slag"]
        fl=request.form["flyash"]
        wa=request.form["water"]
        pl=request.form["plasticizer"]
        ca=request.form["Cagg"]
        fa=request.form["Fagg"]
        ag=request.form["age"]
        # print ("the entere values is {}".format(name))
        predict=[ce,sl,fl,wa,pl,ca,fa,ag]
        scale=ML_model.StandardScaler()
        test=scale.fit_transform([predict])
        result=ML_model.model.predict(test)
        #data from py to html
        
        
        return render_template("submits.html", n=result[0])
    
    
if __name__=="__main__":
    app.run()
    

