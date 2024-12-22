from PIL import Image


image = Image.open("monroTEST.jpg")
print( "ширина" , "высота", image.size)
red, green, blue = image.split()
red.save("red.TEST.jpg")
red.save("red.TEST2.jpg")
image1 = Image.open("red.TEST.jpg")                       
image2 = Image.open("red.TEST2.jpg")                     
image1 = image1.crop((100, 0, 696, 522))                    
image2 = image2.crop((50, 0, 646, 522))                 
image2.save("red.TEST2.jpg")
image3 = Image.blend(image1, image2, 0.5)                
image3.save("IMAGE3.jpg")                       # Красный канал сдвинул влево      


#step8

image = Image.open("monro.TEST2 BLUE.JPG")
print( "ширина" , "высота", image.size)
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
print( "ширина" , "высота", image.size)


#step9

image = Image.open("monro.TEST2 GREEN.jpg")
print( "ширина" , "высота", image.size)
red, green, blue = image.split()
green.save("green.TEST.jpg")
# green.save("green.TEST2.jpg")
image111 = Image.open("green.TEST.jpg")                       
# image222 = Image.open("green.TEST2.jpg")


image111 = image111.crop((50, 0, 646, 522))      # Обрезал зелёный канал слева 50 и справа 50   
image111.save("green.TEST.jpg") 
# image222 = image222.crop((0, 0, 646, 522))
# image222.save("green.TEST2.jpg")
# image333 = Image.blend(image111, image222, 0.5)                  
# image333.save("IMAGE333.jpg")                
# print( "ширина" , "высота", image.size)


#step10

image444 = Image.blend(image3, image33, 0.5)     # Накладываю сначала синий и красный канал друг на друга
image444.save("NEWIMAGE.jpg")                    # Результат 



image555 = Image.blend(image111, image444, 0.5)  # Потом накладываю полученный результат т.е "image444"("NEWIMAGE.jpg") на зелёный канал image111("green.TEST.jpg")
image555.save("THEEND.jpg")                      # Результат  image555("THEEND.jpg")


image3 = Image.open("IMAGE3.jpg")
image33 = Image.open("IMAGE33.jpg")
image111 = Image.open("green.TEST.jpg")
image4444 = Image.blend(image3, image33, 0.5)     # Попытался сложить все 3 канала сразу, но потом удалил 1 канал из за ошибки 
image4444.save("THEEND1111111111.jpg")

image4444 = Image.open("THEEND1111111111.jpg")
image111 = Image.open("green.TEST.jpg")
image999 = Image.blend(image4444, image111, 0.5 )
image999.save("11.jpg")                           # Попытался сделать то же самое  но результат получился не такой
                                                  # Возможно вы забыли сохранить результат одной из операций над каналами.

# Вот схема эффекта ещё раз:

# Обрезаем у красного канала 50 пикселей слева
# Обрезаем у красного канала по 25 пикселей слева и справа
# Склеиваем красные каналы в один
# Обрезаем у синего канала 50 пикселей справа
# Обрезаем у синего канала по 25 пикселей слева и справа
# Склеиваем синие каналы в один
# Обрезаем у зелёного канала 25 пикселей слева и справа
# Собираем картинку из каналов под пунктами 3, 6 и 7 в этой схеме         Так тоже делал .        


# Как мне правильно наложить их друг на друга, в сдвиге думаю проблем нет, так как код работает?











