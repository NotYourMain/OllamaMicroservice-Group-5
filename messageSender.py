from flask import Flask, jsonify
import consul
import requests

app = Flask(__name__)

# Create a Consul client
consul_client = consul.Consul()

# Service name of the receiver microservice
receiver_service_name = "receiver-service"

@app.route('/send_message', methods=['POST'])
def send_message():
    # Find the receiver microservice instance
    receiver_instance = consul_client.agent.service(receiver_service_name)

    # Get the receiver microservice URL
    receiver_url = f"http://{receiver_instance['Address']}:{receiver_instance['Port']}"

    # Send a message to the receiver microservice
    message = {"message": "Hello from sender!"}
    response = requests.post(f"{receiver_url}/receive_message", json=message)

    return jsonify({'message': 'Message sent successfully!'})

if __name__ == '__main__':
    app.run(port=8080)

