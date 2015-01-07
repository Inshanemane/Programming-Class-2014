#feelin it
import random
import simplegui

# Load images and save to a list
image_list = []

#BOY
IBOY = simplegui.load_image('https://pbs.twimg.com/profile_images/462240009374801920/4D8Njtdg.jpeg')
#Winning
IWIN = simplegui.load_image('http://hellogiggles.com/wp-content/uploads/2013/08/23/breaking-bad-aaron-paul-donuts.jpg')
#RICK
IRICK = simplegui.load_image('http://i.cdn.turner.com/asfix/repository//8a250ba13f865824013fc9db8b6b0400/thumbnail_8673142583457162986.jpg')
#MONT
IMONT = simplegui.load_image('http://upload.wikimedia.org/wikipedia/commons/e/e4/Bernard_Law_Montgomery.jpg')
#50 CENT
I50 = simplegui.load_image('http://thumbs.hh.ulximg.com/public/img/avatar/500_1392934648_50_cent_11_87.jpg')
#MOTOR VEHICLE
ICAR = simplegui.load_image('http://4.bp.blogspot.com/-Jb0tgFtBByM/UvpGPMC8psI/AAAAAAAAAPE/ByAbeJWQBZM/s1600/auto+clipart+2.png')
#ROCK
IROCK = simplegui.load_image('http://newsdesk.si.edu/sites/default/files/imagecache/snapshot_image/PlymouthRockPiece.jpg')
#KATE BUSH
IBUSH = simplegui.load_image('http://images.musictimes.com/data/images/full/4166/kate-bush.png')

# Save image widths as a list and image heights as another 
img_width = [IBOY.get_width(),IWIN.get_width(),IRICK.get_width(),
              IMONT.get_width(),I50.get_width(),ICAR.get_width(),
              IROCK.get_width(),IBUSH.get_width()]

img_height = [IBOY.get_height(),IWIN.get_height(),IRICK.get_height(),
              IMONT.get_height(),I50.get_height(),ICAR.get_height(),
              IROCK.get_height(),IBUSH.get_height()]

# Create a dictionary that links images to their width
# and height.
IMG_SIZE = {IBOY:(img_width[0],img_height[0]), IWIN:(img_width[1],img_height[1]),
           IRICK:(img_width[2],img_height[2]), IMONT:(img_width[3],img_height[3]),
           I50:(img_width[4],img_height[4]),ICAR:(img_width[5],img_height[5]),
           IROCK:(img_width[6],img_height[6]),IBUSH: (img_width[7],img_height[7])}


# Define global variables (constants should be in all caps)

# Definition of a Tile class
class Tile:
    
    # Definition of intializer
    def __init__(self, image, exposed):
        self.image = image 
        self.exposed = exposed
        self.location = location
        
    # Definition of getter for image
    def get_image(self):
        return self.image
    
    # Check whether tile is exposed
    def is_exposed(self):
        return self.exposed 
    
    # Expose the tile
    def set_expose_tile(self, exposed):
        self.exposed = exposed
    
    def get_tilewidth(self):
        self.image = image
        image.get_width()
    
    def get_tileheight(self):
        self.image = image
        image.get_height()
        
    # Hide the tile       
    def hide_tile(self):
        pass
        
    # Draw method for tiles.
    # Draws the image if the tile is exposed and a 
    # colored rectangle otherwise.
    def draw_tile(self, canvas):
        pass
    
    # Selection method for tiles.
    # Returns True if the position of mouse click was 
    # anywhere within the boundary of the tile and False
    # otherwise.
    def is_selected(self, position):
        pass


# Define helper function to initialize globals. Function
# should create an image list with two of each image, 
# then use random.shuffle to change the order. Each image
# should then be initialized as a new Tile object with
# its own position on the canvas. These tiles should be 
# saved into a global list of tiles.

    
def new_game():     
	fiftycent = Tile(I50, False)

	tiles = [fiftycent, bush]
        
        
        
# Define mouse click event handler
# Handler should check wether two tiles have be clicked 
# on previously. If they don't match, they should be 
# hidden.  If the current tile is the second one exposed, 
# the number of turns should be updated.  The state
# variable can be used to determine whether it's the 
# first tile of a pair or the second.
def mouse_click(position):
    pass

# Start button handler
def start_button():
    pass
    
# Draw handler.
# Calls the tile's draw_tile method for each tile.
def draw_handler(canvas):
        
    #BOY
    canvas.draw_image(IBOY, (img_width[0]/2,img_height[0]/2), (IMG_SIZE.get(IBOY)), (100, 100), (200, 200))
    canvas.draw_image(IBOY, (img_width[0]/2,img_height[0]/2), (IMG_SIZE.get(IBOY)), (300, 500), (200, 200))
    
    #AARON
    canvas.draw_image(IWIN, (img_width[1]/2,img_height[1]/2), (IMG_SIZE.get(IWIN)), (300, 300), (200, 200))
    canvas.draw_image(IWIN, (img_width[1]/2,img_height[1]/2), (IMG_SIZE.get(IWIN)), (300, 700), (200, 200))
    
    #RICK
    canvas.draw_image(IRICK, (img_width[2]/2,img_height[2]/2), (IMG_SIZE.get(IRICK)), (300, 100), (200, 200))
    canvas.draw_image(IRICK, (img_width[2]/2,img_height[2]/2), (IMG_SIZE.get(IRICK)), (500, 300), (200, 200))
    
    #MONT
    canvas.draw_image(IMONT, (img_width[3]/2,img_height[3]/2), (IMG_SIZE.get(IMONT)), (500, 100), (200, 200))
    canvas.draw_image(IMONT, (img_width[3]/2,img_height[3]/2), (IMG_SIZE.get(IMONT)), (500, 500), (200, 200))
    
    #50 CENT
    canvas.draw_image(I50, (img_width[4]/2,img_height[4]/2), (IMG_SIZE.get(I50)), (100, 500), (200, 200))
    canvas.draw_image(I50, (img_width[4]/2,img_height[4]/2), (IMG_SIZE.get(I50)), (100, 300), (200, 200))
    
    #ICAR
    canvas.draw_image(ICAR, (img_width[5]/2,img_height[5]/2), (IMG_SIZE.get(ICAR)), (700, 100), (200, 200))
    canvas.draw_image(ICAR, (img_width[5]/2,img_height[5]/2), (IMG_SIZE.get(ICAR)), (700, 500), (200, 200))
    
    #IROCK
    canvas.draw_image(IROCK, (img_width[6]/2,img_height[6]/2), (IMG_SIZE.get(IROCK)), (700, 700), (200, 200))
    canvas.draw_image(IROCK, (img_width[6]/2,img_height[6]/2), (IMG_SIZE.get(IROCK)), (100, 700), (200, 200))
    
    #IBUSH
    canvas.draw_image(IBUSH, (img_width[7]/2,img_height[7]/2), (IMG_SIZE.get(IBUSH)), (500, 700), (200, 200))
    canvas.draw_image(IBUSH, (img_width[7]/2,img_height[7]/2), (IMG_SIZE.get(IBUSH)), (700, 300), (200, 200))
    
# Create frame and add a button and label for turns
frame = simplegui.create_frame('MEMORY', 800, 800)


# Set callbacks to handler functions

# Initialize 2 dummy tiles to be used in mouse click 
# handler to keep track of the current 2 tiles.


# Start frame
new_game()
frame.set_draw_handler(draw_handler)
frame.start()
