from flask import Flask, jsonify, request, make_response, send_file
from flask_cors import CORS
from PIL import Image
import io
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhuma imagem encontrada'}), 400

    image = request.files['image']
    red = int(request.form.get('red', 0))
    green = int(request.form.get('green', 0))
    blue = int(request.form.get('blue', 0))


    image_bytes = image.read()
    processed_image_bytes = process_image(image_bytes, red, green, blue)
    processed_image = io.BytesIO(processed_image_bytes)  # Convertendo bytes em um objeto BytesIO

    # Retornando a imagem processada como um arquivo binário
    return send_file(
        processed_image,
        mimetype='image/jpeg'  # Especifique o mimetype correto para o tipo de imagem
    )

def process_image(image_bytes, red, green, blue):
    # Carrega a imagem em um array numpy usando OpenCV
    image_array = np.frombuffer(image_bytes, np.uint8)
    image_cv2 = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Aplica os valores RGB na imagem
    image_cv2[:, :, 0] += blue
    image_cv2[:, :, 1] += green
    image_cv2[:, :, 2] += red

    # Converte a imagem de volta para bytes
    _, processed_image_bytes = cv2.imencode('.jpg', image_cv2)

    return processed_image_bytes.tobytes()

if __name__ == '__main__':
    app.run()
