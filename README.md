# 🧠 MNIST Digit Classifier — End-to-End ML Deployment

This project demonstrates a complete machine learning pipeline, from training to deployment, using the classic MNIST digit classification problem.

It includes:

- 🏋️ **Model Training**: Train a simple neural network with PyTorch on the MNIST dataset  
- 🌐 **REST API**: Host the trained model using a Flask server with `/predict` endpoint  
- 💻 **Web App**: Simple HTML form to upload images and display predictions  
- 📊 **Monitoring**: Prometheus + Grafana setup to monitor inference latency and request rates  
- ☁️ **Cloud Ready**: Dockerized and ready to deploy on any cloud platform (Render, AWS, etc.)

---

## 🔧 Tech Stack

- PyTorch  
- Flask  
- HTML/CSS  
- Prometheus & Grafana  
- Docker  
- Python 3.10

---

## 🚀 Quick Start

1. Train model:
```bash
cd training
python train.py
```

2. Run API:
```bash
cd api
python app.py
```

3. Run Web App:
```bash
cd webapp
python app.py
```

4. Visit: `http://localhost:8000`

---

Perfect as a learning project or template for production ML workflows.

Feel free to modify and deploy!
