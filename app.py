from flask import Flask, jsonify, request, make_response, send_file
from flask_cors import CORS
from PIL import Image
import io
import cv2

app = Flask(__name__)
CORS(app)

message_count = 0

@app.route('/api/texto', methods=['GET'])
def get_text():
    return make_response(jsonify("Funcionou!"))

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhuma imagem encontrada'}), 400

    image = request.files['image']
    # Processar a imagem aqui (por exemplo, salvar em disco, processamento de imagem, etc.)

    image_bytes = image.read()  # Lê os bytes da imagem
    #processed_image_bytes = process_image(image_bytes)  # Função fictícia para processar a imagem
    processed_image = io.BytesIO(image_bytes)  # Convertendo bytes em um objeto BytesIO

    # Retornando a imagem processada como um arquivo binário
    return send_file(
        processed_image,
        mimetype='image/jpeg'  # Especifique o mimetype correto para o tipo de imagem
    )


if __name__ == '__main__':
    app.run()