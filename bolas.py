#!/usr/bin/env python3 
from PIL import Image as Img
import os
#os.chdir(r'\Users\tjj\Desktop\unhas')
cuadro = Img.new('RGB', (300,300))
pinta = cuadro.load()
class Board(object):
	'''All objects in play'''
	fams = [[(71,1), (74,3), (76,7), (79,4), (72,4), (78,6), (73,10), (75,9), (73,5)], [(11,1), (11,3), (11,5), (12,2), (12,4), (12,6), (13,1), (13,3), (13,5)], [(51,1), (51,3), (51,5), (52,2), (52,4), (52,6), (53,1), (53,3), (53,5)]]
	works = [(29,99), (20,73), (30,65), (20,82), (30,74), (40,66), (1,81), (50,73), (40,65),(10,81), (20,73), (30,65), (20,82), (30,74), (40,66), (1,81), (50,73), (40,65)]
	suerte = [(0,0), (99,99), (22,22), (0,44), (88,22), (77,99), (11,66), (44,11), (99,44), (30,65), (73,3), (12,2), (51,3), (66,11)]
	bolas = []
	time = 0
	tempxy = []
	res = []
	def __init__(self):
		self,board = (300,300)
	def famPos(self):
		''' generator returns 1 position of fam each time'''
		multifam = 250 * self.fams[self.fam]
		it = 0
		while it<2400:
			yield multifam[it]
			it += 1

	def workPos(self):
		''' generator returns 1 position of work each time'''
		multiwork = 250 * self.works
		it = 0
		while it<2400:
			yield multiwork[it]
			it += 1

	def ranPos(self):
		''' generator returns 1 position of rand each time'''
		it = 0
		randlist = self.suerte * 10
		multirand = 250 * randlist
		while it<2400:
			yield multirand[it]
			it += 1
	def boardMove():

		print(' \n ', Board.time)

		for item in Board.bolas:
			Board.time += 1
			item.pintame()
			item.bolMove()
			Board.res.append(item.xy)

class Bola(Board):
	def __init__(self, fam, xy):
		self.vir = False
		self.xy = xy
		self.fam = fam
		self.pos = 0
		self.wgen = Board.workPos(self)
		self.hgen = Board.famPos(self)
		self.rgen = Board.ranPos(self)
		self.path = self.mkPath()
		self.xy = self.path[self.pos]
		self.pos += 1
		self.bolas.append(self)	

	def bolMove(self):
		if self.pos == 119:
			self.pos = 1
			self.path = self.mkPath()
		else:
			self.pos += 1
		self.xy = self.path[self.pos]
		return
	def mkPath(self):
		if self.pos == 0:
			return list(Bola.intermediates(self.xy, next(self.wgen)))
		self.pos = 0
		if self.time > 2000:
			return list(Bola.intermediates(self.xy, next(self.hgen)))
		else:
			if self.xy not in self.works:
				return list(Bola.intermediates(self.xy, next(self.wgen)))
			else:
				return list(Bola.intermediates(self.xy, next(self.rgen)))
	def pintame(self):
		pinta[tuple(self.xy)] = (255,0,0)

	def intermediates(p1, p2, nb_points=120):
		""""Return a list of nb_points equally spaced points
		between p1 and p2"""
		# If we have 8 intermediate points, we have 8+1=9 spaces
		# between p1 and p2
		x_spacing = (p2[0] - p1[0]) / (nb_points + 1)
		y_spacing = (p2[1] - p1[1]) / (nb_points + 1)

		return [[int(p1[0] + i * x_spacing), int(p1[1] +  i * y_spacing)] 
				for i in range(1, nb_points+1)]

Bola(0, (16,16))
Bola(1, (69,69))
for i in range(5200):
	Board.boardMove()
print (Board.res)
cuadro.show()

