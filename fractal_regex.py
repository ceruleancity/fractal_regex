import re
from PIL import Image
import sys


class Fregex():
	def fregex(self, size, regex):
		bitmap = [['~']]
		while len(bitmap) < size:
			tempbitmap = []
			for lst in bitmap:
				temprow = []
				for item in lst:
					temprow += [item] + [item]
				# copy the row object
				tempbitmap.append(list(temprow))
				# a reference here fucks all this up
				tempbitmap.append(list(temprow)) 
			bitmap = list(tempbitmap)
			for x in range(len(bitmap)):
				for y in range(len(bitmap)):
					if x % 2 == 1 and y % 2 == 0:
						bitmap[x][y] += "1"
					elif x % 2 == 0 and y % 2 == 1:
						bitmap[x][y] += "4"
					elif x % 2 == 1 and y % 2 == 1:
						bitmap[x][y] += "3"
					else:
						bitmap[x][y] += "2"
		img = Image.new('RGB', (size, size))
		rex = re.compile(regex)
		for x in range(len(bitmap)):
			for y in range(len(bitmap)):
				if rex.match(bitmap[x][y][1:]):
					img.putpixel((x,y), (0,0,0))
				else:
					img.putpixel((x,y), (255,255,255))
		return img
