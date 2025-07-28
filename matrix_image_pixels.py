import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# === 1. Minta pengguna memilih file gambar ===
root = Tk()
root.withdraw()  # Jangan tampilkan jendela utama Tkinter
file_path = askopenfilename(title="Pilih file gambar", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

if file_path:
    # === 2. Baca gambar ===
    img = Image.open(file_path).convert("RGB")

    # === 3. Perkecil gambar agar matriks terlihat jelas ===
    img_small = img.resize((8, 8))
    img_array_small = np.array(img_small)

    print("Ukuran gambar asli:", img.size)
    print("Matriks RGB 8x8:\n", img_array_small)

    # === 4. Tampilkan visualisasi matriks ===
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(img_array_small)
    ax.set_xticks(np.arange(-0.5, 8, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
    ax.grid(which="minor", color="black", linewidth=1)
    ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)

    # === 5. Tambahkan nilai RGB di setiap sel ===
    for i in range(8):
        for j in range(8):
            r, g, b = img_array_small[i, j]
            ax.text(j, i, f"{r},{g},{b}", ha='center', va='center', fontsize=6, color='black')

    plt.title("Matrix Representation of Image Pixels")
    plt.show()

else:
    print("Tidak ada file yang dipilih.")
