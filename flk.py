from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process-spoken-content', methods=['POST'])
def process_spoken_content():
    # Receive the spoken content from the front-end
    data = request.json  # Assuming the data is sent as JSON

    # Process the spoken content (you can add your custom logic here)
    spoken_text = data.get('spokenText', '')

    # For demonstration purposes, let's just echo back the received content
    response_data = {'message': 'Received spoken content: ' + spoken_text}

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
