from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Send a GET request to /submit/<name>/<email>'}), 200

@app.route('/submit/<name>/<email>', methods=['GET'])
def submit(name, email):
    return jsonify({
        'message': 'Data received successfully',
        'name': name,
        'email': email
    }), 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'error': 'Invalid URL',
        'message': "Send a GET request to /submit/<name>/<email>"
    }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000) 