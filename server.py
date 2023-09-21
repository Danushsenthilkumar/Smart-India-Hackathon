"""from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-variable', methods=['POST'])
def process_variable():
    # Receive JSON data from the front end
    data = request.json

    # Extract the variable named 'userVariable' from the JSON data
    user_variable = data.get('userVariable', '')

    # Implement your server-side logic based on the received variable
    # Example: You can print it to the console
    print('Received variable:', user_variable)

    # Return a response to the front end (optional)
    response_data = {'message': 'Received variable: ' + user_variable}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)"""
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-spoken-content', methods=['POST'])
def process_spoken_content():
    data = request.json  # Assuming the data is sent as JSON
    spoken_text = data.get('spokenText', '')
    # Add your server-side logic here based on the spoken content
    response_data = {'message': 'Received spoken content: ' + spoken_text}
    return jsonify(response_data)

if __name__ == '__main__':
    # Specify a custom IP address and port
    host = '0.0.0.0'  # Listen on all available network interfaces
    port = 8080  # Use port 8080 (you can change it to any available port)

    app.run(host=host, port=port, debug=True)


