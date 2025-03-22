from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/receive_message', methods=['POST'])
def receive_message():
    message = request.get_json()
    print(f"Received message: {message}")

    return jsonify({'message': 'Message received successfully!'})

if __name__ == '__main__':
    app.run(port=8081)
