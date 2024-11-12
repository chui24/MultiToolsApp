import qrcode
from PIL import Image

def generar_qr_url(url):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

def generar_qr_imagen(image_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(image_path)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img