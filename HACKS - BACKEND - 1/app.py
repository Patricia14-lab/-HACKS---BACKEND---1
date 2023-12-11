from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/h1", methods=["GET"])
def fn_h1():
    return{"playload":"Get"}


@app.route("/h2", methods=["POST"])
def fn_h2():
        return{"playload":"POST"}



@app.route("/h3", methods=["PUT"])
def fn_h3():
        return{"playload":"PUT"}
    
    
@app.route("/h4", methods=["DELETE"])
def fn_h4():
        return{"playload":"DELETE"}
    
    
@app.route("/h5", methods=["DELETE","PUT","POST","GET"])
def fn_h5():
    method= request.method
    result = {}
    
    if method =="GET":
        result =  {"playload":"succeses","error": False}
    return result
    
    
@app.route("/h6", methods=["GET", "POST", "DELETE", "PUT"])
def fn_h6():

    metodo = request.method
    result = {}
    
    if metodo == "POST" or metodo == "GET" or metodo == "DELETE":
        result = {"method":metodo, "playload":"success", "error":False}
    else:
        result = {"method":metodo, "payload":None, "error":False}
    return result



@app.route("/h7", methods=["GET"])
def fn_h7():
    
    email= request.args.get("email")
    name= request.args.get("name")

    return jsonify ([{
    "payload":{"email":email, "name":name},
    "error":{"available":False,"err_msg":None},
    "status":200
    }])



@app.route("/h8", methods=["POST"])
def fn_h8():
    
    data = request.get_json()
    
    return {
            "payload":{"email":data["email"], "name":["alias"]},
            "error":{"available":False,"err_msg":None},
            "status":200
            }

@app.route("/h9", methods=["GET"])
def fn_h9():
    lista = ["foo","bar","baz","qux","fred"]
    alias = request.args.get("alias")
    result = {}

    if alias in lista:
        result= {
                "payload":alias,
                "error":{"available":False,"err_msg":None},
                "status":200
                }
    else:
    
        result= {
                "payload":"not found",
                "error":{"available":False,"err_msg":None},
                "status":404
                }
    return result

@app.route("/h10", methods=['POST'])
def fn_h10():
    
    lista = ["foo","bar","baz","qux","fred"]
    data = request.get_json()
    result = {}
    if data["alias"] in lista: 
        result = {"payload":data["alias"]}
    else:
        result = {"payload":"not found"}
    return result
    
    
    if __name__ == "__main__":
        app.run(debug=True)
