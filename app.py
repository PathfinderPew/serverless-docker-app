from flask import Flask
import os

app = Flask(__name__)

@app.route('/dev/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    # Get the port from the environment variable PORT, defaulting to 3000 if not set
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
