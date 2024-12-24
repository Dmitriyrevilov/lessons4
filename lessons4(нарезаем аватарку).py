from PIL import Image


image = Image.open("monro.jpg")
red, green, blue = image.split()
red_color1 = red
red_color2 = red
red_color1 = red_color1.crop((100, 0, 696, 522))
red_color2 = red_color2.crop((50, 0, 646, 522))
red_color = Image.blend(red_color1, red_color2, 0.5)


blue_color1 = blue
blue_color2 = blue
blue_color1 = blue_color1.crop((0, 0, 596, 522))
blue_color2 = blue_color2.crop((50, 0, 646, 522))
blue_color = Image.blend(blue_color1, blue_color2, 0.5)


green_color = green
green_color = green_color.crop((50, 0, 646, 522))      


merlin_monro = (red_color, blue_color, green_color)
merlin_monro = Image.merge("RGB", (red_color, green_color, blue_color))
merlin_monro.thumbnail((80, 80))
merlin_monro.save("MERLINMONRO.jpg")
