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
