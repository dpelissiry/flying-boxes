import random
add_library('peasycam')

class Box():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0
        #self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.roty = random.uniform(0,2)
        self.rotz = random.uniform(0,2)
        self.rotx = random.uniform(0,2)
        self.rotxdelt = random.uniform(0,.5)
        self.xdelt = random.uniform(-15,15)
        self.ydelt = random.uniform(-10,10)
    def display(self):
        pushMatrix()
        noStroke()
        translate(self.x, self.y, self.z)
        rotateX(self.rotx)
        rotateY(self.roty)
        rotateZ(self.rotz)
        fill(255, 0, 0, 150)
        rectMode(CENTER)
        box(self.w)
        popMatrix()
        
    def move(self):
        self.w+= map(self.rotxdelt, 0, .5, 0, .1)
        self.z += self.rotxdelt*4
        self.x += self.xdelt
        self.y += self.ydelt
        self.rotx += self.rotxdelt
    def getY(self):
        return self.y
    def getX(self):
        return self.x
        
boxes = []
def setup():
    
    size(2000, 1000, P3D)
    #cam = PeasyCam(this, 500)
    #lights()
    #camera(1000, 0, 200, width/2, height/2, 0, 0, 1, 0)
    for i in range(1000):
        boxes.append(Box(width/2, height/2, 0))
    
    
def draw():
    background(0)
    for bx in boxes:
        bx.display()
        bx.move()
        if bx.getY() > height or bx.getY() < 0 or bx.getX() > width or bx.getX() < 0:
            boxes.remove(bx)
            boxes.append(Box(width/2, height/2, 0))
