<div align="center">

# 🌾 AgroVision AI

### AI-Powered Crop Health Analysis System

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-agri--startup.onrender.com-22c55e?style=for-the-badge)](https://agri-startup.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)

> Upload a crop field image → AgroVision instantly analyzes it and tells you whether your crop is **healthy or unhealthy** using computer vision and machine learning.

</div>

---

## 🚀 Live Demo

🔗 **[https://agri-startup.onrender.com/](https://agri-startup.onrender.com/)**

> Try it yourself — upload any crop/leaf image and get an instant AI-powered health analysis!

---

## 📸 Preview

![AgroVision Dashboard](static/screenshot.png)

> *AI Crop Dashboard — Upload image, select field coordinates, and analyze instantly*

---

## ✨ Features

- 📷 **Image Upload** — Upload any crop or leaf image directly from your device
- 🎯 **Field Selection** — Specify exact field coordinates for targeted analysis
- 🤖 **Instant AI Analysis** — ML model processes the image and returns health status in seconds
- ✅ **Healthy / Unhealthy Classification** — Clear binary output to help farmers act fast
- 🌙 **Clean Dark UI** — Minimal, easy-to-use interface built for accessibility
- ☁️ **Fully Deployed** — Live on Render, accessible from anywhere

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **ML / AI** | Python, TensorFlow, Scikit-Learn |
| **Image Processing** | OpenCV, NumPy |
| **Backend** | Python (Flask / app.py) |
| **Frontend** | HTML, CSS, JavaScript |
| **Deployment** | Render |

---

## ⚙️ How It Works

```
1. User uploads a crop/leaf image
        ↓
2. OpenCV preprocesses the image
   (resize, normalize, feature extraction)
        ↓
3. ML model runs inference on the image
        ↓
4. Model returns: HEALTHY ✅ or UNHEALTHY ❌
        ↓
5. Result displayed instantly on the dashboard
```

---

## 🏃 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Yashaswi2907/Crop-Health-Prediction.git
cd Crop-Health-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open in browser
http://localhost:5000
```

---

## 📁 Project Structure

```
Crop-Health-Prediction/
├── app.py                  # Main Flask application
├── ndvi.py                 # NDVI vegetation index processing
├── requirements.txt        # Python dependencies
├── templates/              # HTML frontend templates
├── static/                 # CSS, JS, images
└── README.md
```

---

## 🌱 Future Improvements

- [ ] Multi-class disease detection (not just healthy/unhealthy)
- [ ] Confidence score display with prediction probability
- [ ] Support for real-time camera input
- [ ] Crop type selection for specialized models
- [ ] Historical analysis dashboard for farmers

---

## 👨‍💻 Author

**Yashaswi Singh**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yashaswi2907/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Yashaswi2907)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:yashaswis545@gmail.com)

---

<div align="center">

*Built with ❤️ to help farmers make smarter decisions using AI*

⭐ Star this repo if you found it useful!

</div>
