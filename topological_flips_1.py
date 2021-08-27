import tkinter as tk

gui = tk.Tk()

gui.title( 'Topological Flips' )

label = tk.Label( gui, text = "Welcome to Topological Flips", height = 5, bg = 'light slate blue', fg = 'OliveDrab1' )
label.pack( fill = tk.X )

# Create frame to contain widgets.
frame = tk.Frame( gui )

# Create a listbox widget offering 10 stunts.
listbox = tk.Listbox( frame )

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
btn = tk.Button( frame, text = 'Choose', command = dialog )

# Button and listbox to the frame at set sides.
#btn.pack( side = BOTTOM, padx = 5 )
btn.pack( side = tk.RIGHT, padx = 15 )
#listbox.pack( side = LEFT )
listbox.pack( fill = tk.X )
#frame.pack( padx = 90, pady = 90 )

stunt = tk.StringVar()

radio_1 = tk.Radiobutton( frame, text = 'Rotational Matrix', variable = stunt, value = 'Will print rotational matrix' )
radio_2 = tk.Radiobutton( frame, text = 'Animation: mp4', variable = stunt, value = 'Will render mp4 animation of stunt' )
radio_3 = tk.Radiobutton( frame, text = 'Animation: gif', variable = stunt, value = 'Will render GIF animation of stunt' )

radio_1.select()

#def dialog() :
#	box.showinfo( 'Selection', 'Your Choice: \n' + stunt.get() )
	
#btn = Button( frame, text = 'Choose', command = dialog )


radio_1.pack( side = tk.LEFT )
radio_2.pack( side = tk.LEFT )
radio_3.pack( side = tk.LEFT )

#frame.pack( side = RIGHT )
frame.pack( fill = tk.X )

gui.mainloop()