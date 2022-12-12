import base64

# Let's get all of our images
# images have letters at the end to represent the state of the button
#  1U = UP
#  1D = DOWN
#  1R = HOVER
#  1G = DISABLED

subdir = "JPG/"
res = "resources/" + subdir
imgs = ["QUIT", "REPORTBUG"]
for img in imgs:
    with open(res+img + "1U.jpg", "rb") as img_file:
        UP = base64.b64encode(img_file.read())
    with open(res+img + "1D.jpg", "rb") as img_file:
        DOWN = base64.b64encode(img_file.read())
    with open(res+img + "1R.jpg", "rb") as img_file:
        HOVER = base64.b64encode(img_file.read())
    with open(res+img + "1G.jpg", "rb") as img_file:
        DISABLED = base64.b64encode(img_file.read())
    print("# Image: ",img) # This is so we can see where the image starts
    print("UP = ", UP)
    print("DOWN = ", DOWN)
    print("HOVER = ", HOVER)
    print("DISABLED = ", DISABLED)
    print("# Image end: ",img) # and where it ends

    '''
     Once converted, you can copy and paste the output into the button class
     you wish to update.

     Please view one of the button classes for an example of where to put the
     base64 encoded images.
    '''