# ServerJsonLocal

The server is set to run on the local host with a simple endpoint '/' (http://127.0.0.1:5000/) that returns a predefined JSON response. This makes it ideal for testing and development purposes, especially for client applications that rely on JSON based APIs.
![Screenshot_6](https://github.com/mykytashch/ServerJsonLocal/assets/129088502/c9e61bbb-ed7d-4728-b6d3-f534ecdff0da)
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

To build and run the Docker container, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/ServerJsonLocal.git`

2. Navigate to the project directory: `cd ServerJsonLocal`

3. Build the Docker image: `docker build -t serverjsonlocal .`

4. Run the Docker container: `docker run -p 5000:5000 serverjsonlocal`

The server should now be accessible at http://127.0.0.1:5000/ from your local machine.

The repository includes a Dockerfile for easy setup and deployment. All dependencies are outlined in the requirements.txt file and will be installed during the Docker image build process, ensuring a clean, isolated environment for your server.

Feel free to clone, fork, or use this repository as a baseline for your own Flask server projects. Contributions and improvements are always welcome!








