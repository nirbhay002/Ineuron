# MUST REFER TO API_FLASK.ipynb FILE BEFORE OPENING THIS FILE

from flask import Flask, request, jsonify

app = Flask(__name__)  #object of flask class


# Defining a route '/xyz' that will accept both GET and POST methods
# Basically route expose the function to the outer world
@app.route('/xyz', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':  # Checks if the incoming request is a POST request.
        # Extracts values associated with the keys 'num1' and 'num2' from the JSON data sent in the POST request:
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))


@app.route('/abc/sudh', methods=['POST'])
def test1():
    if (request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a + b
        return jsonify(str(result))


@app.route('/abc/sudh/kumar', methods=['POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num4']
        b = request.json['num5']
        result = a + b
        return jsonify(str(result))


@app.route('/abcxyz', methods=['POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['sudh']
        b = request.json['kumar']
        result = a + b
        return jsonify(str(result))


# Wrong way to write a function with GET method:
# To call your function from a web browser, you'll need to make a GET request to the /nir endpoint. However,
# the way your function is currently structured expects JSON data in the request body, which is typically sent in a
# POST request, not a GET request.
# @app.route('/nir', methods=['GET'])
# def test4():
#     if (request.method == 'GET'):
#         a = request.json['sudh']
#         b = request.json['kumar']
#         result = a + b
#         return jsonify(str(result))

# Correct way to write a function with GET method:
@app.route('/nir', methods=['GET'])
def test4():
    if request.method == 'GET':
        a = request.args.get('sudh')  # Retrieves the value of the 'sudh' parameter from the query string.
        b = request.args.get('kumar')  # Retrieves the value of the 'kumar' parameter from the query string.
        result = int(a) + int(b)  # The values are added together, converted to integers, and stored in result
        return jsonify(str(result))  # result is returned as a JSON response.


# Ensures that the Flask application runs only when the script is executed directly, not when imported as a module.
if __name__ == '__main__':
    app.run()  # Running the Flask application

"""1 . write a function to fetch data from sql table via api 
2 . write a functoin to fetch a data from mongodb table """
