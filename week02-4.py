def setup():
    size(500,500)
	
def draw():
    if mosePressed:
        line(mouseX,mouseY,pmouseX,PmouseY)