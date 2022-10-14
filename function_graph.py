import pygame, math

pygame.init()
screen_width, screen_height = 720, 720
surface = pygame.display.set_mode((screen_width, screen_height+500))
font = pygame.font.SysFont("Arial", 30)
COLOR = {
	'R': (255,50,50),
	'G': (50,255,50),
	'B': (50,50,200),
	'W': (255,255,255)
}
# You can replace some of these functions with another one
func_exp, func, func_id = [
	"F(x) = x",
	"F(x) = x^2",
	"F(x) = x^3",
	"F(x) = 1/x",
	"F(x) = √x",
	"F(x) = √x^2",
	"F(x) = tan(x)",
	"F(x) = sin(x)",
	"F(x) = cos(x)",
	"F(x) = cos(x) / tan(x)",
	"F(x) = √x^2 - cos(x)",
	"F(x) = √x × cos(x)",
	"F(x) = √x*-2 × tan(x)",
	"F(x) = 1"
],[
	lambda x: math.cos(x**2*0.0006)*50,
	lambda x: x**2*0.005,
	lambda x: x**3*0.00005,
	lambda x: 1/x*10000,
	lambda x: math.sqrt(x)*10,
	lambda x: math.sqrt(x**2),
	lambda x: math.tan(x*0.05)*50,
	lambda x: math.sin(x*0.05)*50,
	lambda x: math.cos(x*0.05)*50,
	lambda x: math.cos(x*0.05)/math.tan(x*0.05)*50,
	lambda x: math.sqrt(x**2)-math.cos(x*0.1)*50,
	lambda x: (math.sqrt(x)*math.cos(x*0.2))*2,
	lambda x: math.sqrt(x*-2)*math.tan(x),
	lambda x: 50
],0

crd = []
for case in range(len(func_exp)):
	if case  < 7: x, y = 5, screen_height+(100*case)+10
	else: x, y = screen_width//2+5, screen_height+(100*(case-7))+10
	crd.append([x, y])
	
touched = False
mouse_pos = (0, 0)

# =============================


def calc_func(x):
	
	x = x-screen_width//2
	# ---------------------
	try: F_X = func[func_id](x)
	except: F_X = -10000
	# ---------------------
	return -F_X+(screen_height//2)


def draw():
	
	global func_id
	
	pygame.time.delay(1)
	
	rect = [
		pygame.Rect((screen_width//2, 0), (4, screen_height)),
		pygame.Rect((0, screen_height//2), (screen_width, 4)),
		pygame.Rect((0, screen_height), (screen_width, screen_height)),
	]
	
	surface.fill((25,25,30))
	surface.fill(COLOR['R'], rect[0])
	surface.fill(COLOR['G'], rect[1])
	
	coordinates = {}
	
	for x in range(0, screen_width+1):
		coordinates[x] = calc_func(x)
			
	for x,y in coordinates.items():
		surface.fill(COLOR['W'], pygame.Rect((x, y), (2, 4)))
		
	surface.fill((10,10,20), rect[2])
	
	for id in range(len(func_exp)):
		surface.fill((40, 40, 120) if func_id == id else (30, 30, 80), pygame.Rect((crd[id][0], crd[id][1]), (screen_width/2-10, 90)))
		surface.blit(font.render(func_exp[id], 1, COLOR['W']), (crd[id][0]+10, crd[id][1]+20))
		
		if touched and pygame.Rect((crd[id][0], crd[id][1]), (screen_width/2-10, 90)).collidepoint(mouse_pos):
			func_id = id
		
	pygame.display.update()


def run():
	
	global touched, mouse_pos
	
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
		elif ev.type == pygame.MOUSEBUTTONDOWN and not touched:
			touched = True
			mouse_pos = ev.pos
		elif ev.type == pygame.MOUSEBUTTONUP:
			touched = False
			
	draw()


# =============================

if __name__ == "__main__":
	
	while True: run()