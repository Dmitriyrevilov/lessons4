from PIL import Image


# Здравствуйте, застрял начиная с step 5, шаги после мне тоже непонятны, прошу указать мне на ошибки и показать на моём примере как это все делается, 
#инструкции максимально непонятные для новичка!



# step 1
# image = Image.open("example.jpg")                 # откроет фото
# rotated_image = image.rotate(45)                  # повернёт на 45 градусов
# rotated_image.save("rotated.jpg")                 # сохранит новое перевёрнутое фото

# # step 2
# cmyk_image = image.convert("CMYK")                # Выведет CMYK
# print( "ширина"  , "высота", image.size)          # ширина 2560, высота 1600
# print("Цветовая модель -" , cmyk_image.mode)      # цветовая модель CMYK

 
# step 3
# image = Image.open("lenna.jpg")                   # Откроет файл
# cmyk_image = image.convert("CMYK")
# print( "ширина"  , "высота", image.size) 
# print("Цветовая модель -" , cmyk_image.mode) 
# image = image.convert("RGB")                      # Переведёт в RGB
# print("Цветовая модель -" ,image.mode) 
# print("ширина"  , "высота", image.size)

# step 4
# image = Image.open("monro.jpg")                     # откроет фото 
# red, green, blue = image.split()                    # В переменные запишутся 3 чёрно-белые картинки.
# red.save("red.image.jpg")                           # сохранил красную картинку отдельно
# green.save("green.image.jpg")                       # сохранил зелёную картинку отдельно
# blue.save("blue.image.jpg")                         # сохранил синий картинку отдельно





#Если я удаляю главное фото, происходит ошибка!!!
# #step 5
# red_color = 'red'                                   # переменые
# green_color = 'green'                               # переменые
# blue_color = 'blue'                                 # переменые

# tuple()                                             # создаст кортеж
# merlin_monro = (red_color, green_color, blue_color) # Функция создает кортеж — tuple() поместил в него переменные цветов
# merlin_monro = Image.open("merlin_monro.jpg")
# print(merlin_monro)                                 # red   green   blue
# merlin_monro = Image.merge("RGB", (red, green, blue))  # соберёт картинку из каналов
# merlin_monro.save("merlin_monro.jpg")                  # сохранит картинку с названием merlin_monro
# merlin_monro = Image.open("merlin_monro.jpg")    



# step 7 Нужно наложить красный канал сам на себя.КАК НАЛОЖИТЬ ИХ ДРУГ НА ДРГА??? (видимо я как то неправильно копирую файлы с цветами)
# сохранил 2 разные картинки с названиями red.TEST, red.TEST2.jpg 


image = Image.open("monroTEST.jpg")
red, green, blue = image.split()
red.save("red.TEST.jpg")
red.save("red.TEST2.jpg")
image1 = Image.open("red.TEST.jpg")             #красная картинка1
image2 = Image.open("red.TEST2.jpg")            #красная картинка2
image3 = Image.blend(image1, image2, 0.10)      #Почему они не накладываются друг на друга?
print( "ширина" , "высота", image3.size)
image3 = image1.crop((110, 100, 696, 522))      #обрезает 1 фото 
image3 = image2.crop((456, 288, 696, 522))
image3.save("IMAGE3.jpg")


















