import shutil
import random


image_files = [
'static/images/image1/image2.jpg',
'static/images/image1/image3.jpg',
'static/images/image1/image4.jpg',
'static/images/image1/image5.jpg',
'static/images/image1/image6.jpg',
'static/images/image1/image7.jpg',
'static/images/image1/image8.jpg',
'static/images/image1/image9.jpg',
'static/images/image1/image10.jpg',
'static/images/image1/image11.jpg',
'static/images/image1/image12.jpg',
'static/images/image1/image13.jpg',
'static/images/image1/image14.jpg',
'static/images/image1/image15.jpg',
'static/images/image1/image16.jpg',
'static/images/image1/image17.jpg',
'static/images/image1/image18.jpg',

]
random_image = random.choice(image_files)
print(random_image)


# source_path = 'path/to/source/image.jpg'
destination_path = 'static/images/new_image.png'

shutil.copy(random_image, destination_path)



# print(random_image)
