# === 1. Install library (hanya sekali di awal) ===
!pip install numpy pillow matplotlib

# === 2. Import library ===
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from google.colab import files

# === 3. Upload file gambar ===
uploaded = files.upload()  # Mahasiswa akan diminta memilih file
file_name = list(uploaded.keys())[0]

# === 4. Baca gambar dan konversi ke RGB ===
img = Image.open(file_name).convert("RGB")

# === 5. Ubah ukuran jadi 8x8 agar mudah ditampilkan sebagai matriks ===
img_small = img.resize((8, 8))
img_array_small = np.array(img_small)

print("Ukuran gambar asli:", img.size)
print("Matriks RGB 8x8:\n", img_array_small)

# === 6. Visualisasi gambar + nilai RGB per pixel ===
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(img_array_small)

# Buat grid
ax.set_xticks(np.arange(-0.5, 8, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
ax.grid(which="minor", color="black", linestyle='-', linewidth=1)
ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)

# Tambahkan nilai RGB di setiap sel
for i in range(8):
    for j in range(8):
        r, g, b = img_array_small[i, j]
        ax.text(j, i, f"{r},{g},{b}", ha='center', va='center', fontsize=6, color='black')

plt.title("Matrix Representation of Image Pixels (8x8)")
plt.show()
