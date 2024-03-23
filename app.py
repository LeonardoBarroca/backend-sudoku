from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

message_count = 0

@app.route('/api/texto', methods=['GET'])
def get_texto():
    return make_response(jsonify("Este é um exemplo de texto retornado pela API em Flask."))


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