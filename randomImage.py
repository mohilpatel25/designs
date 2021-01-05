import os
import random
images = []
for root, dirs, files in os.walk("."):
   for name in files:
      if(name.endswith('.png')):
        images.append(os.path.join(root, name))
final_img = []
while len(final_img) < 9:
  choice = random.choice(images)
  if choice not in final_img:
    final_img.append(choice)
with open('README.md','w') as f:
  f.close()
f = open('README.md','a')
f.write("# Designs\n")
f.write("This repository contains my Designs made using Illustrator.<br>\n") 
f.write("Some of them:<br>\n")
f.write('<table>\n') 
f.write('<tr><td><img src="'+final_img[0]+'"></td><td><img src="'+final_img[1]+'"></td><td><img src="'+final_img[2]+'"></td></tr>\n')
f.write('<tr><td><img src="'+final_img[3]+'"></td><td><img src="'+final_img[4]+'"></td><td><img src="'+final_img[5]+'"></td></tr>\n')
f.write('<tr><td><img src="'+final_img[6]+'"></td><td><img src="'+final_img[7]+'"></td><td><img src="'+final_img[8]+'"></td></tr>\n')
f.write('</table>\n')
f.close()
