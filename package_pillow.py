from PIL import Image, ImageDraw

"""Operasi dasar gamabr"""
# Pastikan ada gambar untuk demo
print("=== IMAGE PROCESSING DEMO ===")

# Buat gambar baru
img = Image.new("RGB", (400, 300), color="lightblue")

# Tambahkan teks
draw = ImageDraw.Draw(img)
draw.text((50, 50), "Hello, PIL!", fill="black")
draw.rectangle([50, 100, 350, 200], outline="red", width=3)
draw.ellipse([100, 150, 300, 250], fill="yellow")

# Simpan gambar
img.save("demo_image.png")
print("✅ Demo image created: demo_image.png")