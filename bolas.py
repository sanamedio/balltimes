'''loaded a gif file for balls to see something moving, and call the balls back to a family path'''
import tkinter as tk
import os
import random
os.chdir(r'../files')

class Board(object):
	nbols = 101
	
	bolas = []
	time = 0
		
	def boardMove():
		Board.time += 1
		if Board.time > 10000:
			Board.time = 0
		for item in Board.bolas:
			item.bolMove()

class Bola(Board):
	def __init__(self, fam, xy):
		self.vir = False
		self.xy = xy
		self.fam = fam
		self.pos = 0
		self.path = self.mkPath()
		self.bolas.append(self)
	
	def crFams(nbols):
		fam1, fam2, fam3, fam4 = [],[],[],[]
		k = 0
		for b in range(int(nbols/4)):
			fam1 +=[(int(20 + random.random()*20), int(20 + random.random()*20))]
			exec(f'bola{k} = Bola(0, fam1[-1])')
			k+=1
		for b in range(int(nbols/4)):
			fam2 += [(int(760 + random.random()*20), int(760 + random.random()*20))]
			exec(f'bola{k} = Bola(1,  fam2[-1])')
			k+=1
		for b in range(int(nbols/4)):
			fam3 += [(int(20 + random.random()*20), int(760 + random.random()*20))]
			exec(f'bola{k} = Bola(2,  fam3[-1])')
			k+=1
		for b in range(int(nbols/4)):
			fam4 += [(int(760 + random.random()*20), int(20 + random.random()*20))]
			exec(f'bola{k} = Bola(3,  fam4[-1])')
			k+=1
		return [fam1, fam2, fam3, fam4]
	
	def bolMove(self):
		''' update bol.xy and bol.path when it runs to the last pos'''
		if self.pos == 248:
			self.pos = 1
			self.path = self.mkPath()
		else:
			self.pos += 1
		self.xy = self.path[self.pos]
		return
	def mkPath(self):
		'''after some time make path to fam cords'''
		if self.pos == 0:
			print(self.xy)
			return list(self.intermediates(self.xy, (int(random.random()*800), int(random.random()*800))))
		if self.time > 1080:
			return list(self.intermediates(self.xy, tuple(random.choice(Board.fams[1]))))
		else:
			return list(self.intermediates(self.xy,(int(random.random()*800), int(random.random()*800))))
	
	def intermediates(self, p1, p2, nb_points=250):
		""""Return a list of nb_points equally spaced points
		between p1 and p2"""
		# If we have 8 intermediate points, we have 8+1=9 spaces
		# between p1 and p2
		x_spacing = (p2[0] - p1[0]) / (nb_points + 1)
		y_spacing = (p2[1] - p1[1]) / (nb_points + 1)
	
		return [[int(p1[0] + i * x_spacing), int(p1[1] + i * y_spacing)]
				for i in range(1, nb_points+1)]
Board.fams = Bola.crFams(Board.nbols)
	
# Create the window with the Tk class
root = tk.Tk()
# Create the canvas and make it visible with pack()
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack() # this makes it visible
# Loads and create image (put the image in the folder)
azulgif = tk.PhotoImage(file="azul.gif")
rojogif = tk.PhotoImage(file="rojo.gif")
amagif = tk.PhotoImage(file="amarillo.gif")
# outrashow = canvas.create_image(550, 550, anchor=tk.NW, image=rojogif)
# azulshow = canvas.create_image(150, 150, anchor=tk.NW, image=azulgif)
# azul = Bola(0, (150,150))
# outra = Bola(1, (550,550))
imgbolas = []
for k in range(100):
	item = Board.bolas[k]
	#imgbolas.append(exec(f'imgbola{k} = 0'))    # = canvas.create_image(i, 50, anchor=tk.NW, image=amagif)'))
	exec(f'imgbola{k} = canvas.create_image(item.xy[0], item.xy[1], anchor=tk.NW, image=rojogif)')
	print(k)

# def move(event):
# 	'''Move the sprite image with a d w and s when click them'''
# 	Board.boardMove()
# 	canvas.moveto(azulshow, azul.xy[0], azul.xy[1])
# 	canvas.moveto(outrashow, outra.xy[0], outra.xy[1])
# This bind window to keys so that move is called when you press a key
# root.bind("<Key>", move)
while True:
	Board.boardMove()
	# canvas.moveto(azulshow, azul.xy[0], azul.xy[1])
	# canvas.moveto(outrashow, outra.xy[0], outra.xy[1])
	for k in range(100):
		item = Board.bolas[k]
		exec(f'canvas.moveto(imgbola{k}, item.xy[0], item.xy[1])')
	
	root.update_idletasks()
	root.update()
	# this creates the loop that makes the window stay 'active'
#root.mainloop()