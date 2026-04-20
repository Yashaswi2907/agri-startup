import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Replace filenames exactly as yours
red = rasterio.open("T43QCV_20260225T053811_B04_10m.jp2")
nir = rasterio.open("TT43QCV_20260225T053811_B08_10m.jp2")

red_band = red.read(1).astype(float)
nir_band = nir.read(1).astype(float)

ndvi = (nir_band - red_band) / (nir_band + red_band + 1e-10)

plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar()
plt.title("Real NDVI Map")
plt.savefig("real_ndvi.png")
plt.show()

print("Real NDVI generated")