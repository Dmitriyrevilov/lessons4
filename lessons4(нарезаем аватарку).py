from PIL import Image

red_color = Image.open("RED_COLOR.jpg") 
blue_color = Image.open("BLUE_COLOR.jpg")
green_color = Image.open("GREEN_COLOR.jpg") 


merlin_end = (red_color, blue_color, green_color)
merlin_end = Image.merge("RGB", (red_color, green_color, blue_color))
merlin_end.save("MERLINMONRO1.jpg")
merlin_end = Image.open("MERLINMONRO1.jpg") 


merlin_end = Image.open("MERLINMONRO1.jpg")
print(merlin_end.size)  
merlin_end.thumbnail((80, 80 ))  
print(merlin_end.size)  
merlin_end.save("MERLINMONRO.jpg")