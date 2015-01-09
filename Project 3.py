#feelin it
import random
import simplegui

# Load images and save to a list


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

image_list = [IBOY,IWIN,IRICK,IMONT,I50,ICAR,IROCK,IBUSH]
images = image_list + image_list
newtiles = []

# Save image widths as a list and image heights as another 
img_width = [IBOY.get_width(),IWIN.get_width(),IRICK.get_width(),
              IMONT.get_width(),I50.get_width(),ICAR.get_width(),
              IROCK.get_width(),IBUSH.get_width()]

img_height = [IBOY.get_height(),IWIN.get_height(),IRICK.get_height(),
              IMONT.get_height(),I50.get_height(),ICAR.get_height(),
              IROCK.get_height(),IBUSH.get_height()]

# Create a dictionary that links images to their width
# and height.
IMAGE_SIZE = {IBOY:(img_width[0],img_height[0]), IWIN:(img_width[1],img_height[1]),
           IRICK:(img_width[2],img_height[2]), IMONT:(img_width[3],img_height[3]),
           I50:(img_width[4],img_height[4]),ICAR:(img_width[5],img_height[5]),
           IROCK:(img_width[6],img_height[6]),IBUSH: (img_width[7],img_height[7])}


# Define global variables (constants should be in all caps)
TILE_WIDTH  = 200
TILE_HEIGHT = 200

# Definition of a Tile class
class Tile:
    
    # Definition of intializer
    def __init__(self, image, exposed, location):
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
    def expose_tile(self):
        self.exposed = True
        
    # Hide the tile       
    def hide_tile(self):
        self.exposed = False
        
    # Draw method for tiles.
    # Draws the image if the tile is exposed and a 
    # colored rectangle otherwise.
    def draw_tile(self, canvas):
        canvas.draw_image(self.image, (IMAGE_SIZE[self.image][0]/2,IMAGE_SIZE[self.image][1]/2), IMAGE_SIZE[self.image],self.location,(TILE_WIDTH,TILE_HEIGHT))
    # Selection method for tiles.
    # Returns True if the position of mouse click was 
    # anywhere within the boundary of the tile and False
    # otherwise.
    def is_selected(self, position):
        top = self.location[1] - TILE_HEIGHT/2
        bot = self.location[1] + TILE_HEIGHT/2
        right = self.location[0] + TILE_WIDTH/2
        left = self.location[0] - TILE_WIDTH/2
        return left < postition[0] < right and top < positition[1] < bot
        
# Define helper function to initialize globals. Function
# should create an image list with two of each image, 
# then use random.shuffle to change the order. Each image
# should then be initialized as a new Tile object with
# its own position on the canvas. These tiles should be 
# saved into a global list of tiles.

    
def new_game():     
    global TILE_WIDTH, TILE_HEIGHT
    random.shuffle(images)
    i = 0
    for image in images:
        row = i//4
        col = i%4
        x = TILE_WIDTH/2 + TILE_WIDTH * col
        y = TILE_HEIGHT/2 + TILE_HEIGHT * row
        newtiles.append(Tile(image,False,(x,y)))
        i+=1                  
        
# Define mouse click event handler
# Handler should check wether two tiles have be clicked 
# on previously. If they don't match, they should be 
# hidden.  If the current tile is the second one exposed, 
# the number of turns should be updated.  The state
# variable can be used to determine whether it's the 
# first tile of a pair or the second.
def mouse_click(position):
    if state == 1:
        if tile1.get_image() != tile2.get_image():
            tile1.hide_tile()
            tile2.hide_tile()
        for tile in tiles:
            if tile.is_selected(position):
                tile1 = tile 
                tile1.expose_tile()
                state = 2
    else:
        for tile in tiles:
            if tile.is_selected(position):
                tile2 = tile 
                tile2.expose_tile()
                state = 1
                
# Start button handler
def start_button():
    new_game()
    
# Draw handler.
# Calls the tile's draw_tile method for each tile.
def draw_handler(canvas):
    for tile in newtiles:
        tile.draw_tile(canvas)
    
    
    
# Create frame and add a button and label for turns
frame = simplegui.create_frame('MEMORY', 800, 800)


# Set callbacks to handler functions

# Initialize 2 dummy tiles to be used in mouse click 
# handler to keep track of the current 2 tiles.
tile1 = Tile(IBOY,False,(20,20))
tile2 = Tile(IBOY,False,(20,20))
# Start frame
new_game()
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_click)
frame
frame.start()
