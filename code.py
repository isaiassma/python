#Abra a pasta e instale a biblioteca
#pip install qrcode[pil]
import qrcode

#entrada dp usuário
link=input("Link ou Texto para QrCode: ")

#Criando o Qr Code
qr = qrcode.QrCode(
    version=1, #tamanho do qrcode
    error_correction=qrcode.constantes.ERROR_CORRECT_L,
    box size=10 #tamanho de cada quadradinho 
    border=4, #espessura da borda 
)

qr.add_data(link)
qr.make(fit=True)

#criar a imagem
img = qr.make_image(fill_color="black", back_color="White")

#salvar o arquivo
img.save("qrcode.png")

print("QR Code gerado: 'qrcode.png'")
