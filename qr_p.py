# se necesita instalar  pip install qrcode pillow
import qrcode 

# El link que querés codificar
input_data = 'https://sites.google.com/view/cienciasdedatoseia/contenido/unidad-i'

# Crear el objeto QR, quie se encuenta el tamaño y el borde de la misma
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Agregar la data
qr.add_data(input_data)
qr.make(fit=True)

# Generar la imagen con colores por defecto es negro y blanco
img = qr.make_image(fill_color='black', back_color='white')

# Guardar la imagen con el correspondiente nombre 
img.save('qrtelecapp.png')
