import sys
from Tkinter import *
from fractal_regex import Fregex
from PIL import Image, ImageTk

# globals
_TEMP_FILE_EXT_="ppm"
_TEMP_FILE_=".temp." + _TEMP_FILE_EXT_
_SIZE_=512

class FregexCanvas(Canvas):
	'''draw images in here'''
	def __init__(self, master):
		Canvas.__init__(self, width=_SIZE_ ** 2, height=_SIZE_ ** 2)
		self.master = master
		self.regex = ""
		try:
			self.img = PhotoImage(file=_TEMP_FILE_)
		except Exception, e:
			self.img = PhotoImage(width=_SIZE_,heigh=_SIZE_)
		self.create_label(self.img)
		self.entry_var = StringVar()
		self.entry = Entry(self, textvariable=self.entry_var)
		self.entry.bind('<Return>', self.fregex)
		self.entry.grid(column=0, row=1)
		self.draw()
	
	def fregex(self, args):
		regex = self.entry_var.get()
		if regex != self.regex:
		 	fregex = Fregex()
			self.img = fregex.fregex(_SIZE_, self.entry_var.get())
			(width, height) = self.img.size
			if width > _SIZE_:
				resized = self.img.resize((_SIZE_, _SIZE_))#, Image.ANTIALIAS)
				resized.save(_TEMP_FILE_, _TEMP_FILE_EXT_)
				self.img = PhotoImage(resized)
			else:
				self.img.save(_TEMP_FILE_, _TEMP_FILE_EXT_)
				self.img = PhotoImage(file=_TEMP_FILE_)
			self.create_label(self.img)
			self.draw()

	def create_label(self, img):
		self.imagepanel = Label(self, text="fregex", borderwidth=2, image=self.img)
		self.imagepanel.grid(column=0, row=0)

	def draw(self):
		self.pack()

class FregexFrame(Frame):
	'''outermost window'''
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.canvas = FregexCanvas(master)
		self.pack()
		master.title('fregex by ceruleancity')

def main():
	'''entry point for this program'''
	root = Tk()
	root.resizable(0, 0)
	app = FregexFrame(master=root)
	app.mainloop()

if __name__ == '__main__':
	sys.exit(main())
