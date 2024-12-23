from PIL import Image


image = Image.open("monroTEST.jpg")
red, green, blue = image.split()
red.save("red.TEST.jpg")
red.save("red.TEST2.jpg")
image1 = Image.open("red.TEST.jpg")                       
image2 = Image.open("red.TEST2.jpg")                     
image1 = image1.crop((100, 0, 696, 522))                    
image2 = image2.crop((50, 0, 646, 522))                 
image2.save("red.TEST2.jpg")
image3 = Image.blend(image1, image2, 0.9)                
image3.save("IMAGE3.jpg")                       # Красный канал сдвинул влево      


#step8

image = Image.open("monro.TEST2 BLUE.JPG")
red, green, blue = image.split()
blue.save("blue.TEST.jpg")
blue.save("blue.TEST2.jpg")
image11 = Image.open("blue.TEST.jpg")                       
image22 = Image.open("blue.TEST2.jpg")
image11 = image11.crop((0, 0, 596, 522)) 
image11.save("blue.TEST.jpg") 
image22 = image22.crop((50, 0, 646, 522))                      
image22.save("blue.TEST2.jpg")
image33 = Image.blend(image11, image22, 0.5)                  
image33.save("IMAGE33.jpg")                       # Синий канал сдвинул вправо 

#step9

image = Image.open("monro.TEST2 GREEN.jpg")
red, green, blue = image.split()
green.save("green.TEST.jpg")
image111 = Image.open("green.TEST.jpg")                       
image111 = image111.crop((50, 0, 646, 522))      # Обрезал зелёный канал слева 50 и справа 50   
image111.save("green.TEST.jpg") 



merlin_end = (image3, image33, image111)
image3 = Image.open("IMAGE3.jpg")
image33 = Image.open("IMAGE33.jpg")
image111 = Image.open("green.TEST.jpg")
red, green, blue = image.split()
merlin_end = Image.merge("RGB", (image3, image33, image111))
merlin_end.save("MERLINMONRO.jpg")
merlin_end = Image.open("MERLINMONRO.jpg") 



# merlin_end = Image.open("MERLINMONRO.jpg")
# print(merlin_end.size)  # Вывелось (800, 1200)
# merlin_end.thumbnail((80, 80  ))  # Картинка теперь размера 400 на 600
# print(merlin_end.size)  # Вывелось (400, 600)
# merlin_end.save("MERLINMONRO.jpg")



















