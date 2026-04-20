import matplotlib
matplotlib.use('Agg')

from flask import Flask, render_template, request
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # crop values
    x = int(request.form.get("x", 0))
    y = int(request.form.get("y", 0))
    w = int(request.form.get("w", 300))
    h = int(request.form.get("h", 300))

    img = cv2.imread(filepath)

    if img is None:
        return "Image not loaded"

    # safe crop
    h_img, w_img = img.shape[:2]
    crop = img[y:min(y+h, h_img), x:min(x+w, w_img)]

    # channels
    B, G, R = cv2.split(crop)

    R = R.astype(float)
    G = G.astype(float)

    # NDVI approx
    ndvi = (G - R) / (G + R + 1e-5)

    mean_ndvi = float(np.mean(ndvi))

    # health
    if mean_ndvi > 0.5:
        health = "Healthy 🌱"
        suggestion = "Crop is healthy. Maintain irrigation."
    elif mean_ndvi > 0.2:
        health = "Moderate ⚠️"
        suggestion = "Add fertilizers and monitor crop."
    else:
        health = "Poor ❌"
        suggestion = "Immediate attention required. Improve soil & irrigation."

    # save NDVI image
    plt.figure(figsize=(4, 4))
    plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
    plt.colorbar()
    plt.axis('off')

    output_path = f"static/output_{file.filename}.png"
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()

    # histogram graph
    plt.figure()
    plt.hist(ndvi.flatten(), bins=50)
    plt.title("NDVI Distribution")

    graph_path = f"static/ndvi_graph_{file.filename}.png"
    plt.savefig(graph_path)
    plt.close()

    return render_template(
        "index.html",
        image=output_path,
        graph=graph_path,
        mean_ndvi=round(mean_ndvi, 3),
        health=health,
        suggestion=suggestion,
        filename=file.filename
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
