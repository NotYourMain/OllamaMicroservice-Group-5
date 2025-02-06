# OllamaMicroservice-Group-3
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
1.3 Run Ollama Server
After installation, start the Ollama server with:
ollama serve
This ensures that Ollama is running in the background.
 
2. Set Up Python Virtual Environment
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
📌 GitHub Repository: https://github.com/NotYourMain/OllamaMicroservice-Group-3 
Alternatively, clone the repository using:
git clone https://github.com/NotYourMain/OllamaMicroservice-Group-3
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
📍 http://127.0.0.1:5000/
 
6. Open the Chatbot in a Browser
1.	Open index.html in a web browser.
2.	Type a message and click Send to chat with Ollama!
 
7. Testing via Postman (Optional)
For API testing, you can use Postman:
1.	Open Postman
2.	Create a new POST request to: 
3.	http://127.0.0.1:5000/chat
4.	In the Body tab, select raw and set type to JSON, then enter: 
5.	{
6.	    "message": "Hello, how are you?"
7.	}
8.	Click Send, and you should receive a chatbot response.
 
8. Troubleshooting
8.1 Flask Errors (Module Not Found)
If you get a ModuleNotFoundError, ensure the virtual environment is activated and rerun:
pip install flask requests
8.2 Ollama Not Responding
If the chatbot doesn't work, make sure Ollama is running by opening a terminal and running:
ollama serve
8.3 Virtual Environment Not Found
If your terminal says "command not found" for python, try using python3.

![image](https://github.com/user-attachments/assets/7a2f5fd1-930c-477e-bb43-29f41acff1fe)
