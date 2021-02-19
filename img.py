from PIL import Image


for i in range(256):
    img = Image.open('redescuras/rede1_regra_'+str(i)+'.jpg')
    new_img = img.resize((200,200))
    new_img.save("redesResize/rede1_regra_"+str(i)+'.jpg', "JPEG", optimize=False)


