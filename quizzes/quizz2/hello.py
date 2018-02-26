from flask import Flask,request, jsonify,Response

app = Flask(__name__)
element = 0
my_dict_user = {}
@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def new_users():
    name = request.form["name"]
    global element
    element += 1
    my_dict_user[element] = name
    json_data = {
        'id' : element,
        'name' : name
    }
    js = jsonify(json_data)
    js.status_code = 201
    return js

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'User not found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/users/<int:value>', methods=['GET'])
def user_given_id(value):
    if value > element:
        return  not_found()
    elif value in my_dict_user:
        json_data = {
            'id' : value,
            'name' : my_dict_user[value]
        }
        resp = jsonify(json_data)
        resp.status_code = 200
        return resp
    return not_found()

@app.route('/users/<int:value>', methods=['DELETE'])
def user_del(value):
    if value > element:
        return  not_found()
    elif value in my_dict_user:
        json_data = {
            'id' : value,
            'name' : my_dict_user[value]
        }
        del my_dict_user[value]
        resp = jsonify(json_data)
        resp.status_code = 204
        return resp
    return not_found()
    
