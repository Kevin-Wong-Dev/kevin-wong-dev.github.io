import qrcode

# --- Configura tu URL aquí ---
# Asegúrate de que esta URL sea la dirección completa y permanente de tu sitio Netlify.
url_de_tu_sitio = "https://menulasglorias.netlify.app/"  # ¡Cambia esto por tu URL real!

# --- Generar el código QR ---
# Crea una instancia del generador QR
qr = qrcode.QRCode(
    version=1,  # Tamaño del QR (1 es el más pequeño, hasta 40). Autoajustará si es necesario.
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores (L, M, Q, H). L=7% datos perdidos, H=30%
    box_size=10,  # Tamaño de cada "cuadrado" del QR en píxeles
    border=4,  # Grosor del borde blanco alrededor del QR
)

# Añade los datos (tu URL)
qr.add_data(url_de_tu_sitio)
qr.make(fit=True)

# Crea la imagen del código QR
# Puedes especificar los colores aquí
img = qr.make_image(fill_color="black", back_color="white")

# --- Guarda la imagen del QR ---
# Dale un nombre descriptivo a tu archivo
nombre_archivo_qr = "mi_netlify_qr.png"
img.save(nombre_archivo_qr)

print(f"¡Código QR generado con éxito! Se guardó como {nombre_archivo_qr}")
print(f"Apunta a la URL: {url_de_tu_sitio}")
