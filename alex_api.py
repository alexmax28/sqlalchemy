from flask import Flask, abort, jsonify,request

app = Flask(__name__)


data = [
        {
            "name":"alex",
            "age":18
        },
        {
            "name":"ted",
            "age":20
        },
        {
            "name":"bob",
            "age":19
        }
        ]


@app.route("/",methods=["GET"])
def index():
    return "index page"

@app.route("/tasks",methods=["GET"])
def tasks():
    return jsonify(data)

@app.route("/task2/<name>",methods=["GET"])
def task2(name):
        ans = [x for x in data if x['name'] == name]
        print(ans)
        if len(ans) == 0:
             abort(404)
        else:
             return jsonify(ans)
        
@app.route("/add",methods=["POST"])
def addtask():
    if request.json is None or "name" not in  request.json:
          abort(404)
    add_data = {
         "name":request.json["name"],
         "age":request.json["age"]
    }
    data.append(add_data)
    return jsonify({"data":data}),201

@app.route("/del/<name>",methods=["DELETE"])
def deltask(name):
    res = [x for x in data if x["name"] == name ]
    if len(res) == 0:
        abort(404)
    data.remove(res[0])
    return jsonify({"result":True})

     

    
     

if __name__ == "__main__":
    app.run(debug=True)
