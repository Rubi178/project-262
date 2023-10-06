from flask import Flask, render_template, request
import requests 
app=Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")
@app.route("/op", methods=["POST"])
def math_operations():
    e=request.form["text"]
    o=request.form["operations"]
    result= "https://newton.now.sh/api/v2//" + o + "/" + e
    response=requests.get(result)
    return render_template("index.html",equation=e,result=response.json()["result"])
if __name__=="__main__":
    app.run()