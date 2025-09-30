import qrcode

# Dit link
link = "https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1"

# Lav QR-koden
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)

# Gem som billede
img = qr.make_image(fill_color="black", back_color="white")
img.save("youtube_qrkode.png")

print("QR-kode gemt som youtube_qrkode.png")
