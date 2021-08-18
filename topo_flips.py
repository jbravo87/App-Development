from tkinter import *
import tkinter.messagebox as box

window = Tk()

window.title( 'Topological Flips' )

label = Label( window, text = 'Welcome to Topological Flips' )

label.pack( padx = 200, pady = 50 )

frame = Frame( window )

stunt = StringVar()

radio_1 = Radiobutton( frame, text = 'Rotational Matrix', variable = stunt, value = 'Will print rotational matrix' )
radio_2 = Radiobutton( frame, text = 'Animation: mp4', variable = stunt, value = 'Will render mp4 animation of stunt' )
radio_3 = Radiobutton( frame, text = 'Animation: gif', variable = stunt, value = 'Will render GIF animation of stunt' )

radio_1.select()

def dialog() :
	box.showinfo( 'Selection', 'Your Choice: \n' + stunt.get() )
	
btn = Button( frame, text = 'Choose', command = dialog )

btn.pack( side = RIGHT, padx = 5 )
radio_1.pack( side = LEFT )
radio_2.pack( side = LEFT )
radio_3.pack( side = LEFT )

frame.pack( padx = 50, pady = 30 )

window.mainloop()