# import modules
import qrcode
from PIL import Image
 
while True:
    print ("Choix couleur :")
    print ("    a) Bleu sur fond Blanc.")
    print ("    b) Blanc sur fond Bleu.")
    choose_color = input ("[a/b] ? : ")
    if choose_color in ['a', 'b']:
        break
# process the input
if choose_color == "a": 
    Logo_link = 'logo_blanc.png'
    QRcolor = '#052d78'
    QRbackground_color = 'white'
elif choose_color == "b": 
    Logo_link = 'logo_bleu.png'
    QRcolor = 'white'
    QRbackground_color = '#052d78'
    
logo = Image.open(Logo_link)
logo = logo.convert('RGBA')
 
# taking base width
basewidth = 100
 
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
 
# taking url or text
url = input("Entrez l'URL a convertir en QRCODE : ")
 
# adding URL or text to QRcode
QRcode.add_data(url)
 
# generating QR code
QRcode.make()
 
# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color=QRbackground_color).convert('RGBA')
 
# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
 
# save the QR code generated
QRimg.save('qrcode.png')

print('QR code generated!')