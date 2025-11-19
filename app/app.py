from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # Returns the hostname (Container ID) so you know which node served the request
    return f"Response from Container: {socket.gethostname()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
