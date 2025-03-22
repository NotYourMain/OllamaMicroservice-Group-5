# OllamaMicroservice-Group-5
This project allows our microservice to interact with our LLM and respond to queries. We can get our results either on Postman or on a website.

Ollama Chatbot Setup Guide
This guide will walk you through downloading, installing, and running the Ollama chatbot on Windows, Mac, and Linux.
 
1. Install Prerequisites
1.1 Install Python (If Not Already Installed)
Check if Python is installed by running:
python --version
or
python3 --version
If it's not installed, download and install Python 3.9+ from:
🔗 https://www.python.org/downloads/
1.2 Install Ollama (Required for LLM Processing)
Ollama is needed to run the local LLM. Download it from:
🔗 https://ollama.com/download
Once installed, verify by running:
ollama --version
1.3 Download Ollama Mistral
Run the code "ollama pull mistral"
1.4 Run Ollama Server
After installation, start the Ollama server with:
ollama serve
This ensures that Ollama is running in the background.
 
2. Set Up Python Virtual Environment (Optional)
2.1 Create a Virtual Environment
Open a terminal and run:
python -m venv chatbot-env
or (on some systems)
python3 -m venv chatbot-env
2.2 Activate the Virtual Environment
•	Mac/Linux: 
•	source chatbot-env/bin/activate
•	Windows (Command Prompt): 
•	chatbot-env\Scripts\activate
•	Windows (PowerShell): 
•	chatbot-env\Scripts\Activate.ps1
Once activated, the terminal prompt will show (chatbot-env), indicating that the virtual environment is active.
 
3. Download Chatbot Files
Download the chatbot files from GitHub:
GitHub Repository: https://github.com/NotYourMain/OllamaMicroservice-Group-5 
Alternatively, clone the repository using:
git clone https://github.com/NotYourMain/OllamaMicroservice-Group-5
Then navigate into the directory:
cd [your-repo-folder]
 
4. Install Required Python Libraries
Run the following command in the activated virtual environment:
pip install flask requests
(If pip is missing, install it using python -m ensurepip first.)
 
5. Start the Chatbot Server
Run the Flask server:
python server.py
If using Python 3, run:
python3 server.py
The server should now be running at:
http://127.0.0.1:5000/
 
6. Open the Chatbot in a Browser
1.	Open index.html in a web browser.
2.	Type a message and click Send to chat with Ollama!
 
7. Testing via Postman (Optional But Recommended)
For API testing, you can use Postman:
1.	Open Postman
2.	Create a new POST request to: 
3.	http://127.0.0.1:8000/chat
4.	In the Body tab, select raw and set type to JSON, then enter: 
5.	{
6.	    "message": "Hello, how are you?"
7.	}
8.	Click Send, and you should receive a chatbot response.

# Part Two 
Setting Up Consul as the Proxy for Service Discovery

1. Using Binary Installation
Download the Consul binary from the official website:
- https://www.consul.io/downloads
Extract the binary to a directory of your choice:
Move the extracted binary to a directory in your system's PATH:

1.1. Package Manager Installation
Consul can also be installed using package managers like Homebrew (macOS) or apt-get (Ubuntu/Debian):

macOS (Homebrew)

bash
brew tap hashicorp/tap
brew install hashicorp/tap/consul

Ubuntu/Debian (apt-get)

bash
sudo apt-get update
sudo apt-get install consul

Verification
After installation, verify that Consul is running:

bash/cmd
consul --version
You should see the Consul version number.

Starting Consul
To start Consul, run:
bash/cmd
consul agent -dev
This will start Consul in development mode.

For this Setup, we will be using a config file to run Consul though
Transfer the Config.json file to the directory where Consul was installed and make sure to run the command below for running the Consul server:
"consul agent -config-file=config.json"
This will set up that device as the Consul Server.

Repeat the process above for the Consul Agent but instead use the "agentConfig.json" file and run the command on the agent system:
"consul agent -config-file=agentConfig.json"

Make sure to tailor your config files to your devices:
"server" should be checked true if you're hosting the server on that device and false if you're running the Consul agent as a client
"bootstrap" should be checked true if you're the cluster leader and false if not
"bind address" and "advertise address" for your ip address.
"data_dir" is the directory of where Consul was installed, also create an empty folder called "data".

Consul also runs periodic health checks on microservices registered.

# Part Three 
Communication between the devices
Run the "services.py" file with the command "python services.py" on the terminal.
Make sure the "server.py" file is also running on both devices.

Using Postman
Create a new POST request to: http://127.0.0.1:8000/chat
In the Body tab, select raw and set type to JSON, then enter: 
	{
        "user_id": "David" (This can be any name)
	    "prompt": "Hello, how are you?" (The message for the ollama chatbot)
	}
	Click Send, and you should receive a chatbot response to show that Ollama is still running.

Create a new POST request to: http://127.0.0.1:5000/register
In the Body tab, select raw and set type to JSON, then enter: 
	{
        "name": "Dan", (The name of the Microservice to be registered)
        "address": "127.0.0.1", (The address)
        "port": "8500" (The port number)
	}
	Click Send, and you should receive a message confirming that the microservice has been registered.
    Consul also has a UI page that can be opened once the server address is typed on the browser (shown in the video presentation)

Create a new GET request to: http://127.0.0.1:5000/microservices
	Click Send, and you should receive a list of already registered microservices asides seeing them on the Consul UI server.

Create a new POST request to: http://127.0.0.1:5000/request
In the Body tab, select raw and set type to JSON, then enter: 
	{
    "name": "Request1", (Name/ID of request being sent to any microservice registered)
    "data": {
        "user_id": "Dan", (Registered Microservice to be queried)
        "prompt": "Who is patrick star?" (message being queried to the microservice)
    }
}
	Click Send, and you should receive a chatbot message from ollama.

This implementation allows any of the linked devices to run these request on POSTMAN.

Additional Notes
Per the requested video showcasing the microservices talking to one another, we were unable to record a video due to distance.
However, to send a message from one microservice to the other, the other agent device simply has to register a microservice on Consul.
Then we input the name of the microservice on line 80 of the "services.py" file for the "receiver_service_name" variable.

This allows a message to be sent from one microservice to the other and the message is printed on the consule of the terminal.
