from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    # Python Program to Get IP Address
    
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    #print("Your Computer Name is:" + hostname)
    #print("Your Computer IP Address is:" + IPAddr)

    return IPAddr

if __name__=="__main__":
    app.run(host="0.0.0.0")
