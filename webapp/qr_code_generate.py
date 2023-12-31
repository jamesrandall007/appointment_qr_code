# https://pypi.org/project/qrcode/
# pip install "qrcode[pil]"
import PIL.Image
import qrcode
from PIL import Image
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")


# use the Class for more features
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")
img.show()

img.save("newestQR.png", kind="png")


# with open("savedk_qr_code.png", "wb+") as file_qr:
#     file_qr.write(img)
#     print("SAVED as savedqrcode")