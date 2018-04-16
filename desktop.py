# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 13:07:12 2018

@author: Surya
"""
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


from flask import Flask, render_template
app = Flask(__name__,static_url_path="/static")
from flask import jsonify
import os.path
import sys
import json
from flask import request
# try:
#     import apiai
# except ImportError:
#     sys.path.append(
#         os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
#     )
#     import apiai
#import pyopenssl    
import requests
import csv

@app.route("/")
def template_test():
    print("hello")
    return render_template('initial.html')


@app.route("/rest/api/")
def api_call():
    q = request.args.get('q')
    resp = api_main(q)
    print (resp)
    return (resp)

    
def api_main(Querry):
    train = []
    test = []

    with open("training.csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            train.append(row)
        
    with open("test.csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            test.append(row)


    cl = NaiveBayesClassifier(train)
    cl.classify("This is an amazing library!")
    prob_dist = cl.prob_classify("This one's a doozy.")
    prob_dist.max()
    round(prob_dist.prob("machine"), 2)
    round(prob_dist.prob("no machine"), 2)
    blob = TextBlob(Querry, classifier=cl)
    blob.classify()
    for s in blob.sentences:
        print("\n\n\n" + str(s))
        print("\n" + str(s.classify()))
        return (s.classify)
	
if __name__ == '__main__':
    # app.run(ssl_context='adhoc')
    app.run(debug=True, host='0.0.0.0', port=6969)
