import numpy as np
import matplotlib.pyplot as plt

from sentinelhub import (
    SHConfig,
    DataCollection,
    SentinelHubRequest,
    MimeType,
    CRS,
    Geometry,
    BBox
)

# ================================
# 🔐 Sentinel Hub Credentials
# ================================

config = SHConfig()
config.sh_client_id = "sh-7792b774-d974-4790-a40e-7b14a866ca2c"
config.sh_client_secret = "MCZKsMh8ITSRNWgkI09ZEKU28VX2RCqR"

# ================================
# 🌾 Padosi ka Khet Polygon
# ================================

polygon_coords = [
    (78.15152377539766, 27.54903331415268),
    (78.1515584045582, 27.54884397964547),
    (78.15162931898075, 27.54863930751353),
    (78.15167942029298, 27.54845440112139),
    (78.15177186307707, 27.54839094384752),
    (78.1525125854921, 27.54922920187282),
    (78.15210834641614, 27.54951595254428),
    (78.15191509130422, 27.54948199478841),
    (78.1516943399152, 27.549555381878),
    (78.1515863459545, 27.54947665315025),
    (78.15150112175145, 27.54940246952944),
    (78.15153863486191, 27.54931653936226),
    (78.15149119154503, 27.54918843440739),
    (78.15152377539766, 27.54903331415268)
]

geometry = Geometry(
    {"type": "Polygon", "coordinates": [polygon_coords]},
    crs=CRS.WGS84
)

# ================================
# 🛰 Use Bounding Box (Stable)
# ================================

bbox = geometry.bbox

# ================================
# 🌿 NDVI Evalscript
# ================================

evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["B04", "B08"],
    output: {
      bands: 1,
      sampleType: "FLOAT32"
    }
  };
}

function evaluatePixel(sample) {
  let ndvi = (sample.B08 - sample.B04) / (sample.B08 + sample.B04);
  return [ndvi];
}
"""

# ================================
# 📡 Request Satellite Data
# ================================

request = SentinelHubRequest(
    evalscript=evalscript,
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L2A,
            time_interval=("2026-02-15", "2026-03-04"),
        )
    ],
    responses=[
        SentinelHubRequest.output_response("default", MimeType.TIFF)
    ],
    bbox=bbox,
    size=(512, 512),   # Important for proper resolution
    config=config
)

# ================================
# 📥 Download Data
# ================================

print("Fetching satellite data...")
response = request.get_data()
ndvi = response[0]

# ================================
# 📊 NDVI Stats
# ================================

print("Minimum NDVI:", np.min(ndvi))
print("Maximum NDVI:", np.max(ndvi))
print("Average NDVI:", np.mean(ndvi))

# ================================
# 🖼 Show NDVI Map
# ================================

plt.figure(figsize=(6, 6))
plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
plt.colorbar(label="NDVI")
plt.title("NDVI - Padosi ka Khet")
plt.savefig("static/output.png")