from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Declare the dictionary that will store chat history.
chat_histories = {}

#Flask Endpoint that handles chat requests
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_id = data.get("user_id")
    prompt = data.get("prompt")

#Returns an error message to the client if user_id or prompt is missing
    if not user_id or not prompt:
        return jsonify({"error": "user_id and prompt are required"}), 400

    # Retrieving or initializing chat history
    if user_id not in chat_histories:
        chat_histories[user_id] = []

    # Add user message to chat history
    chat_histories[user_id].append({"role": "user", "content": prompt})

    # Get response from Ollama
    response = ollama.chat(model="mistral", messages=chat_histories[user_id])

    # Extract bot response and update history
    bot_response = response["message"]["content"]
    chat_histories[user_id].append({"role": "assistant", "content": bot_response})

    return jsonify({"response": bot_response, "history": chat_histories[user_id], "user_id": user_id})

#Getting the Chat History for a User
@app.route("/history/<user_id>", methods=["GET"])
def get_chat_history(user_id):
    """Retrieve chat history for a user."""
    return jsonify({"user_id": user_id, "history": chat_histories.get(user_id, [])})

#Deleting the Chat History for a User
@app.route("/history/<user_id>", methods=["DELETE"])
def delete_chat_history(user_id):
    """Clear chat history for a user."""
    if user_id in chat_histories:
        del chat_histories[user_id]
    return jsonify({"message": "Chat history cleared", "user_id": user_id})

#Python idiom to check that the current script is being run directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

