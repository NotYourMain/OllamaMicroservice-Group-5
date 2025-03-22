import consul
import json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Consul configuration
consul_client = consul.Consul(host='localhost', port=8500)

# Register a service with Consul
def register_service(name, address, port):
    consul_client.agent.service.register(
        name=name,
        address=address,
        port=port,
        tags=["microservice"]
    )

# Deregister a service with Consul
def deregister_service(name):
    consul_client.agent.service.deregister(name)

# Register a microservice with the service registry
@app.route('/register', methods=['POST'])
def register_microservice():
    try:
        data = request.json
        name = data.get('name')
        address = data.get('address')
        port = int(data.get('port'))
        if not name or not address or not port:
            return jsonify({'error': 'Name, address, and port required'}), 400
        register_service(name, address, port)
        return jsonify({'message': 'Microservice registered'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get a list of registered microservices
@app.route('/microservices', methods=['GET'])
def get_microservices():
    services = consul_client.agent.services()
    microservices = []
    for service_id, service in services.items():
        if "microservice" in service["Tags"]:
            microservices.append({
                "name": service["Service"],
                "address": service["Address"],
                "port": service["Port"]
            })
    return jsonify({"microservices": microservices})

# Send a request to another microservice
@app.route('/request', methods=['POST'])
def send_request():
    try:
        data = request.json
        name = data.get('name')
        request_data = data.get('data')
        if not name or not request_data:
            return jsonify({'error': 'Name and data required'}), 400
        url = "http://localhost:8000/chat" #The URL of the microservice to which the request will be sent
        if not url:
            return jsonify({'error': 'Microservice not found'}), 404
        try:
            response = requests.post(url, json=request_data)
            response.raise_for_status()
            return jsonify({'response': response.json()}), response.status_code
        except requests.exceptions.RequestException as e:
            return jsonify({'error': str(e)}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Send a message to another microservice


# Service name of the receiver microservice
receiver_service_name = "receiver-service" # Replace with the actual service name once registered on consul with other device

@app.route('/send_message', methods=['POST'])
def send_message():
    # Find the receiver microservice instance
    receiver_instance = consul_client.agent.service(receiver_service_name)

    # Get the receiver microservice URL
    receiver_url = f"http://{receiver_instance['Address']}:{receiver_instance['Port']}"

    # Send a message to the receiver microservice
    message = {"message": "Hi, Can you see this message?!"} #Message to be sent
    response = requests.post(f"{receiver_url}/receive_message", json=message)

    return jsonify({'message': 'Message sent successfully!'})

# Receive a message from another microservice
@app.route('/receive_message', methods=['POST'])
def receive_message():
    message = request.get_json()
    print(f"Received message: {message}")

    return jsonify({'message': 'Message received successfully!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
