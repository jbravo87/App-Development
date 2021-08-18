from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title( 'List of Skateboard Stunts' )

# Create frame to contain widgets.
frame = Frame( window )

# Create a listbox widget offering 10 stunts.
listbox = Listbox( frame )

listbox.insert( 1, 'Kickflip' )
listbox.insert( 2, 'Varial Kickflip' )
listbox.insert( 3, 'Hardflip' )
listbox.insert( 4, 'Frontside Shove-it' )
listbox.insert( 5, 'Heelflip' )
listbox.insert( 6, 'Inward Heelflip' )
listbox.insert( 7, '360 Pop Shove-it' )
listbox.insert( 8, 'Double Kickflip' )
listbox.insert( 9, 'Nightmare Flip' )
listbox.insert( 10, 'Laser Flip' )

# Function to display listbox selection
def dialog() :
	box.showinfo( 'Selection', 'Your Choice:' + listbox.get( listbox.curselection() ) )
	
# Button to call the function when clicked.
btn = Button( frame, text = 'Choose', command = dialog )

# Button and listbox to the frame at set sides.
btn.pack( side = RIGHT, padx = 5 )
listbox.pack( side = LEFT )
frame.pack( padx = 90, pady = 90 )

window.mainloop()