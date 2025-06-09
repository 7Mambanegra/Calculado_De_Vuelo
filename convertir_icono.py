from PIL import Image

img = Image.open("logo.png")  # Cambia "logo.png" si tu imagen tiene otro nombre
img.save("icono.ico", format="ICO", sizes=[(64, 64)])
