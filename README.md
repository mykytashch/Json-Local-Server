# ServerJsonLocal

The server is a minimal implementation written in just 14 lines and 275 characters. It runs on the local host with a simple endpoint '/' (http://127.0.0.1:5000/) that returns a predefined JSON response. This compact server is designed for testing and development purposes, particularly for client applications that rely on JSON-based APIs.

![Screenshot_6](https://github.com/mykytashch/ServerJsonLocal/assets/129088502/c9e61bbb-ed7d-4728-b6d3-f534ecdff0da)

The repository includes a Dockerfile for easy setup and deployment. All dependencies are outlined in the requirements.txt file and will be installed during the Docker image build process, ensuring a clean and isolated environment for your server.

To build and run the Docker container, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/ServerJsonLocal.git`

2. Navigate to the project directory: `cd ServerJsonLocal`

3. Build the Docker image: `docker build -t serverjsonlocal .`

4. Run the Docker container: `docker run -p 5000:5000 serverjsonlocal`

Here is the compact Python code for the server (14 lines, 275 characters):


```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'name': 'Test',
        'message': 'This is a test JSON'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```
`app.py`





To move JSON data to a separate `data.json` file, you can create a JSON file and read its contents into the Flask server code. Here is an example:


```python
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```
`app.py`

```json
{
  "name": "Test",
  "message": "This is a test JSON"
}
```
`data.json`

Feel free to clone, fork, or use this repository as a baseline for your own Flask server projects. Contributions and improvements are always welcome!




