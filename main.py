# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Basicosmic
# Date: Dec 05
# Description: This program allow user to manipulations image

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()



# list of system options
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# list of basic operation options
basic = [
            "1: Invert color",
            "2:Flip Horizontally",
            "3:Flip Vertically",
            "4: Switch to Intermeidate Functions",
            "5: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                    "1:Remove Red Channel",
                    "2:Remove Green Channel",
                    "3:Remove Blue Channel",
                    "4:Convert to Greyscale",
                    "5:Apply sepia filter",
                    "6:Decrease brightness",
                    "7:Increase brightness",
                    "8:Switch to basic function",
                    "9:Switch to Advanced function"

                 ]

# list of advanced operation options
advanced = [
                "1:Rotate Left",
                "2:Rotate Right",
                "3:Pixelate",
                "4:Binarize",
                "5: Switch to Basic Functions",
                "6: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic

    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate

    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced

    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet

        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example

            print("Log: Quitting...")

        elif userInput == "O":

            print("Log: Opening image...")

            tkinter.Tk().withdraw()
            #Let the user select a file from their computer and get the file name
            openFilename = tkinter.filedialog.askopenfilename(initialdir="/project/images", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))

            currentImg = cmpt120imageProj.getImage(openFilename)
            #set the lastOpenFilename as the image file name in dictionay
            appStateValues["lastOpenFilename"] = openFilename

            cmpt120imageProj.showInterface(currentImg,"currentImg",generateMenu(appStateValues))
            return currentImg

        elif userInput == "S":

            print("Log: Saving image...")
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()

            cmpt120imageProj.saveImage(img,saveFilename) #save user image file to a selected place
            cmpt120imageProj.showInterface(img,"saved image",generateMenu(appStateValues))



        elif userInput == "R":

            print("Log: Reloading image...") #reload the original image
            openFilename = appStateValues["lastOpenFilename"]
            currentImg = cmpt120imageProj.getImage(openFilename)

            cmpt120imageProj.showInterface(currentImg,"reloaded image",generateMenu(appStateValues))
            return currentImg


    # handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options

        print("Log: Doing manipulation functionalities " + userInput)

        if appStateValues["mode"] == "basic" :

            if userInput=="1":

                print("Log: inverting image...")#invert image

                inverted_img = cmpt120imageManip.invert(img)
                cmpt120imageProj.showInterface(inverted_img,"inverted_img",generateMenu(appStateValues))
                return inverted_img


            elif userInput=="2":

                print("Log: fliping horizontally...")#Flip Horizontal)
                flipped_img = cmpt120imageManip.flipHorizontal(img)
                cmpt120imageProj.showInterface(flipped_img,"flipped_Horizontally_img",generateMenu(appStateValues))

                return flipped_img

            elif userInput=="3":

                print("Log: fliping vertically...") #Flip Vertical)
                flipped_img = cmpt120imageManip.flipVertically(img)
                cmpt120imageProj.showInterface(flipped_img,"flipped_Vertically_img",generateMenu(appStateValues))

                return flipped_img

            elif userInput=="4":

                print("Log: Switch to intermediate Functions...")
                #Switch to intermediate Functions)

                appStateValues["mode"]= "intermediate"
                cmpt120imageProj.showInterface(img,"intermediate mode",generateMenu(appStateValues))

            elif userInput=="5":

                print("Log: Switch to Advanced Functions...")
                #Switch to Advanced Functions)

                appStateValues["mode"]= "advanced"
                cmpt120imageProj.showInterface(img,"Advanced mode",generateMenu(appStateValues))


        elif appStateValues["mode"] == "intermediate" :

            if userInput=="1":

                print("Log: Remove Red Channel...") #Remove Red Channel

                no_red_img = cmpt120imageManip.noRed(img)
                cmpt120imageProj.showInterface(no_red_img,"no_red_img",generateMenu(appStateValues))

                return no_red_img

            elif userInput=="2":

                print("Log: Remove Green Channel...") #Remove Green Channel

                no_Green_img = cmpt120imageManip.noGreen(img)
                cmpt120imageProj.showInterface(no_Green_img,"no_Green_img",generateMenu(appStateValues))

                return no_Green_img

            elif userInput=="3":

                print("Log: Remove Blue Channel...") #Remove Blue Channel

                no_Blue_img = cmpt120imageManip.noBlue(img)
                cmpt120imageProj.showInterface(no_Blue_img,"no_Blue_img",generateMenu(appStateValues))

                return no_Blue_img

            elif userInput=="4":

                print("Log: Convert to Greyscale...") #Convert image to Greyscale

                grey_img = cmpt120imageManip.greyscale(img)
                cmpt120imageProj.showInterface(grey_img,"Greyscale",generateMenu(appStateValues))

                return grey_img

            elif userInput=="5":

                print("Log: Apply sepia filter...") #Apply sepia filter to image

                sepia_img = cmpt120imageManip.sepia(img)
                cmpt120imageProj.showInterface(sepia_img,"Sepia image",generateMenu(appStateValues))

                return sepia_img

            elif userInput=="6":

                print("Log: Decrease brightness...") #Decrease the brightness of image by 10

                decreaseBrightness_img = cmpt120imageManip.decreaseBrightness(img)
                cmpt120imageProj.showInterface(decreaseBrightness_img,"decreaseBrightness_img",generateMenu(appStateValues))

                return decreaseBrightness_img

            elif userInput=="7":

                print("Log: Increase brightness...") #Decrease the brightness of image by 10

                increaseBrightness_img = cmpt120imageManip.increaseBrightness(img)
                cmpt120imageProj.showInterface(increaseBrightness_img,"increaseBrightness_img",generateMenu(appStateValues))

                return increaseBrightness_img

            elif userInput=="8":

                print("Log: Switch to basic function...")
                #Switch to basic Functions

                appStateValues["mode"]= "basic"
                cmpt120imageProj.showInterface(img,"basic mode",generateMenu(appStateValues))

            elif userInput=="9":


                print("Log: Switch to Advanced Functions...")
                #Switch to Advanced Functions

                appStateValues["mode"]= "advanced"
                cmpt120imageProj.showInterface(img,"advanced mode",generateMenu(appStateValues))

        elif appStateValues["mode"] == "advanced" :

            if userInput=="1":

                print("1:Rotate Left")  #Rotate the image 90 degree anti-clockwise

                rotateLeft_img = cmpt120imageManip.rotateLeft(img)
                cmpt120imageProj.showInterface(rotateLeft_img,"rotateLeft_img",generateMenu(appStateValues))

                return rotateLeft_img

            elif userInput=="2":

                print("2:Rotate Right") ##Rotate the image 90 degree clockwise

                rotateRight_img = cmpt120imageManip.rotateRight(img)
                cmpt120imageProj.showInterface(rotateRight_img,"rotateRight_img",generateMenu(appStateValues))

                return rotateRight_img

            elif userInput=="3":

                print("3:Pixelate") #Pixelate the image

                pixelate_img = cmpt120imageManip.pixelate(img)
                cmpt120imageProj.showInterface(pixelate_img,"pixelate_img",generateMenu(appStateValues))

                return pixelate_img

            elif userInput=="4":

                print("4:Binarize") #Create a black and white image based on a threshold value

                binarize_img = cmpt120imageManip.binarize(img)
                cmpt120imageProj.showInterface(binarize_img,"binarize_img",generateMenu(appStateValues))

                return binarize_img


            elif userInput=="5":

                print("5: Switch to Basic Functions")
                #Switch to basic Functions

                appStateValues["mode"]= "basic"
                cmpt120imageProj.showInterface(img,"Basic mode",generateMenu(appStateValues))

            elif userInput=="6":

                print("6: Switch to Intermediate Functions")
                #Switch to intermediate Functions)

                appStateValues["mode"]= "intermediate"
                cmpt120imageProj.showInterface(img,"intermediate mode",generateMenu(appStateValues))



    else: # unrecognized user input

            print("Log: Unrecognized user input: " + userInput)

    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:

    ### use the pygame event handling system ###

    for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                appStateValues["lastUserInput"] = pygame.key.name(event.key)
                # prepare to quit the loop if user inputs "q" or "Q"

                if appStateValues["lastUserInput"].upper() == "Q":

                    keepRunning = False
                # otherwise let the helper function handle the input

                else:
                    currentImg = handleUserInput(appStateValues, currentImg)

            elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton

                keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")