import qrcode

# Datos que deseas codificar en el QR
data = "https://menulasglorias.netlify.app/"

# Crear el objeto QR
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño del QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada cuadro del QR
    border=4,  # Tamaño del borde (mínimo es 4)
)

# Agregar los datos al QR
qr.add_data(data)
qr.make(fit=True)

# Crear la imagen del QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen en un archivo
img.save("codigo_qr.png")

print("¡Código QR generado y guardado como 'codigo_qr.png'!")
