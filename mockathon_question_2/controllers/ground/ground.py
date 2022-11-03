from controller import Display
from controller import Supervisor
from controller import Keyboard

TIME_STEP = 64

# size of the ground in meters.
GROUND_X = 9.9
GROUND_Y = 9.9

super = Supervisor() # Supervisor node used to fetch location of moving robot. 

# Enable Keyboard to use for teleoping the robot
keyboard=Keyboard()
keyboard.enable(TIME_STEP) # Enabled keyboard to provide feedback with time difference equat to timestep.

# First we get a handler to devices
display = super.getDevice("ground_display")

# get the properties of the Display
width = display.getWidth()
height = display.getHeight()

# getting access to robot handle to access its tree.
mybot = super.getFromDef("diff_robot")

# getting translation field of robot to make changes on the ground.
translationField = mybot.getField("translation")

# Loading background from an image. 
background = display.imageLoad("../../worlds/textures/sin.png")
display.imagePaste( background, 0, 0) # adding background to the display node to make changes on the background.

# // set the pen to remove the texture
display.setAlpha( 0.0)

draw = True # Flag to to enable and disable drawing.

while super.step(TIME_STEP) != -1:

  # getting currently pressed key on the keyboard.    
  key=keyboard.getKey()
  print(key , "   ====  Key")
  if (key==80): # If 'p' press enable drawing
    print ('P is pressed')
    draw=True
  elif(key==79): # If 'o' press disable drawing
    print ('O is pressed')
    draw=False

  if draw:  # Condition to draw
    translation = translationField.getSFVec3f()
    x = int(height * (translation[1] + GROUND_X / 2) / GROUND_X) # Mapping robot translation in x axis to pixel value
    y = int(width * (translation[0] + GROUND_Y / 2) / GROUND_Y) # Mapping robot translation in y axis to pixel value
    
    # Remove 10 x 10 pixel at location x,y in the display image plane to see base Women in AI and Robotics logo.
    display.fillOval( x, y, 10, 10)

  pass
