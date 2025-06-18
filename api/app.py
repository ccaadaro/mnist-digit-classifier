from flask import Flask, request, jsonify
import torch
from model import Net
from PIL import Image
import torchvision.transforms as transforms
import time

app = Flask(__name__)
model = Net()
model.load_state_dict(torch.load("model.pt", map_location=torch.device('cpu')))
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    start = time.time()
    file = request.files['file']
    img = Image.open(file).convert('L')
    img = transforms.ToTensor()(img).unsqueeze(0)
    output = model(img)
    pred = torch.argmax(output, dim=1).item()
    latency = time.time() - start
    app.logger.info(f"Inference latency: {latency:.4f}s")
    return jsonify({'prediction': pred})