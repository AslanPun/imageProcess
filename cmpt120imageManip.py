# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Basicosmic
# Date: Dec 05
# Description: Functions that manipulate image

import numpy
import cmpt120imageProj


#Function to invert the colors of the image by subtracting 255 from RGB values
def invert(img):

    width = len(img)
    height = len(img[0])

    for i in range(width):
        for j in range(height):
            pixels = img[i][j]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]
            r = 255 - r
            g = 255 - g
            b = 255 - b
            new_pixels = [r, g, b]
            img[i][j] = new_pixels

    return img



#Function to Flip image horizontally along the vertical axis in the middle
def flipHorizontal(img):

    width = len(img)
    height = len(img[0])

    for i in range(width//2):
        for j in range(height):
            left_pixels = img[i][j]
            right_pixels = img [width -1-i][j]
            img[width -1-i][j] = left_pixels
            img[i][j] = right_pixels

    return img



#Function to flip the image along the horizontal axis in the middle
def flipVertically(img):

    width = len(img)
    height = len(img[0])

    for i in range(width):
        for j in range(height//2):
            top_pixels = img[i][j]
            bot_pixels = img[i][height-1-j]
            img[i][height-1-j] = top_pixels
            img[i][j] = bot_pixels

    return img

#Function that sets all the Red values in all pixels to zero
def noRed(img):

    width = len(img)
    height = len(img[0])

    for i in range(width):
        for j in range(height):
            pixels = img[i][j]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]
            r = 0
            g = g
            b = b
            new_pixels = [r, g, b]
            img[i][j] = new_pixels

    return img

#Function that sets all the Green values in all pixels to zero
def noGreen(img):

    width = len(img)
    height = len(img[0])

    for i in range(width):
        for j in range(height):
            pixels = img[i][j]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]
            r = r
            g = 0
            b = b
            new_pixels = [r, g, b]
            img[i][j] = new_pixels

    return img

#Function that sets all blue values in all pixels to zero
def noBlue(img):

    width = len(img)
    height = len(img[0])

    for i in range(width):
        for j in range(height):
            pixels = img[i][j]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]
            r = r
            g = g
            b = 0
            new_pixels = [r, g, b]
            img[i][j] = new_pixels

    return img

#Function to replace all colors with a shade of gray. 
def greyscale(img):

    width = len(img)
    height = len(img[0])

    for i in range(width):
        for j in range(height):
            pixels = img[i][j]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]
            avg = int((r+g+b)/3)
            r = avg
            g = avg
            b = avg
            new_pixels = [r, g, b]
            img[i][j] = new_pixels

    return img

#Function to Apply Sepia Filter using a predefined formula with set values
def sepia(img):

    width = len(img)
    height = len(img[0])

    for i in range(width):
        for j in range(height):
            pixels = img[i][j]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]

            r = int((r *.393) + (g *.769) + (b * .189))
            g = int( (r * .349) + (g *.686) + (b * .168))
            b = int( (r * .272) + (g *.534) + (b * .131))
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255

            new_pixels = [r, g, b]
            img[i][j] = new_pixels

    return img

#Function to decrease Brightness of each pixel by 10 each time 
def decreaseBrightness(img):

    width = len(img)
    height = len(img[0])

    for i in range(width):
        for j in range(height):
            pixels = img[i][j]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]
            r = r - 10
            g = g - 10
            b = b - 10
            #Checks to ensure values don't go below 0
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            new_pixels = [r, g, b]
            img[i][j] = new_pixels

    return img

#Function to increase brightness of each pixel by 10 each time
def increaseBrightness(img):

    width = len(img)
    height = len(img[0])

    for i in range(width):
        for j in range(height):
            pixels = img[i][j]
            r = pixels[0]
            g = pixels[1]
            b = pixels[2]
            r = r + 10
            g = g + 10
            b = b + 10
            #Checks to ensure values don't go above 255
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            new_pixels = [r, g, b]
            img[i][j] = new_pixels

    return img

#Function to rotate image counter-clockwise by 90 Degrees
def rotateLeft(img):

    width = len(img)
    height = len(img[0])
    #Creating a new image with inverted axis interchanging width and height values
    rotated_img_canvas = cmpt120imageProj.createBlackImage(height,width)

    for i in range(width):
        for j in range(height):
            rotated_img_canvas[j][-i]= img[i][j]


    return rotated_img_canvas

#Function to Rotate image clock wise by 90 degress
def rotateRight(img):

    width = len(img)
    height = len(img[0])
    #creating a new image with inverted axis interchanging width and height values
    rotated_img_canvas = cmpt120imageProj.createBlackImage(height,width)

    for i in range(width):
        for j in range(height):
            rotated_img_canvas[-j][i]= img[i][j]


    return rotated_img_canvas

#Function to pixelate an image by taking an average of all pixel values in a 4x4 block
def pixelate(img):

    width = len(img)
    height = len(img[0])

    for i in range(0,width,4):
        for j in range(0,height,4):
            total_r = 0
            total_g = 0
            total_b = 0
            for x in range(0,4):
                for y in range(0,4):
                    pixels = img[x+i][y+j]
                    total_r += pixels[0]
                    total_g += pixels[1]
                    total_b += pixels[2]
            for x in range(0,4):
                for y in range(0,4):
                    img[x+i][y+j][0] = int(total_r/16)
                    img[x+i][y+j][1] = int(total_g/16)
                    img[x+i][y+j][2] = int(total_b/16)
    return img





#Function to binarize the Image - Create a black and white image based on the threshold Value.
def binarize(img):
    #Convert the image into grayscale
    grey_img = greyscale(img)
    width = len(img)
    height = len(img[0])

    #Calculate the initial threshold value as average of one of the pixel colour channel of the image
    total_value_of_red_channel = 0
    for i in range(width):
        for j in range(height):
            color = grey_img[i][j][0]
            total_value_of_red_channel += color

    initial_threshold = int(total_value_of_red_channel / (width*height))

    #Creating a While loop if the new_threshold - initial_threshold  >= 10 

    new_threshold = initial_threshold
    breakcase = True
    while breakcase == True:


      #Create two images, one is the background where only the pixels with values less
      #than or equal to the threshold will be copied over; the other is the foreground
      #where only the pixels with values more than the threshold will be copied over.
      
      initial_threshold = new_threshold

      background = cmpt120imageProj.createBlackImage(width,height)
      foreground = cmpt120imageProj.createBlackImage(width,height)


      for i in range(width):
          for j in range(height):
              pixels = img[i][j]
              r = pixels[0]
              if r < initial_threshold:
                  pixels = background[i][j]
                  pixels[0] = r
                  pixels[1] = r
                  pixels[2] = r


              elif r > initial_threshold:
                  pixels = foreground[i][j]
                  pixels[0] = r
                  pixels[1] = r
                  pixels[2] = r

      #Calculate the average of one of the pixel colour channel of the background image,
      #do the same for the foreground image

      total_background_img_grey_value = 0
      for i in range(width):
          for j in range(height):
              color = background[i][j][0]
              total_background_img_grey_value += color

      background_threshold = int(total_background_img_grey_value / (width*height))

      total_foreground_img_grey_value = 0
      for i in range(width):
          for j in range(height):
              color = foreground[i][j][0]

              total_foreground_img_grey_value += color

      foregound_threshold = int(total_foreground_img_grey_value / (width*height))

      new_threshold = int((background_threshold+foregound_threshold)/2)
      if abs(new_threshold - initial_threshold) <= 10:
          #keeping the new threshold 
          breakcase = False
    # Using defined threshold to assign either white or black values       
    for i in range(width):
        for j in range(height):
            pixels = img[i][j]
            r = pixels[0]
            if r < new_threshold:
                img[i][j] = [0,0,0]
            elif r > new_threshold:
                img[i][j] = [255,255,255]

    return img