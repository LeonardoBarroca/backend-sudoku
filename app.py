from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

message_count = 0

@app.route('/api/texto', methods=['GET'])
def get_text():
    return make_response(jsonify("Funcionou!"))


@app.route('/api/message', methods=['GET', 'POST'])
def manage_message():
    global message_count
    if request.method == 'POST':
        data = request.get_json()
        message = data.get('message')
        message_count += 1
        return jsonify({'message': f'Backend recebeu: {message}, Total de mensagens: {message_count}'})
    else:
        return jsonify({'message': f'Olá do backend, Total de mensagens: {message_count}'})

if __name__ == '__main__':
    app.run()