from tkinter import *
from PIL import ImageTk,Image
import subprocess
import os

def solver(input_string):
	# Parameters : ---> The sudoku in the form of an input string, each row separated by a newline, no spaces
	# Return value : ---> The output string, either the solved sudoku or -1 reporting no answer

	data, temp = os.pipe()  
	os.write(temp, bytes(input_string, "utf-8")); 
	os.close(temp)

	s = subprocess.check_output("g++ solution.cpp ;./a.out",stdin = data, shell = True) 
	output_string = (s.decode("utf-8"))

	return output_string


def Button_press(Entrylist):
	#convert to string
	input_string = ""
	for x in range(0,9):
		for y in range(0,9):
			val = Entrylist[x][y].get()
			input_string = input_string+val
		input_string = input_string + '\n'
	
	print(input_string)

	output_string = solver(input_string)

	print(output_string)

	if(output_string[0] == '-'):
		return

	for x in range(0,9):
		for y in range(0,9):
			Entrylist[x][y].delete(0,END)
			Entrylist[x][y].insert(0 , output_string[x*9 + y + x])

	return


root = Tk()
root.title('Solver')

#List of lists
Entrylist = []

for x in range(0,9):
	Rowlist = []
	for y in range(0,9):
		Rowlist.append(Entry(root,width = 5))
	Entrylist.append(Rowlist)

for x in range(0,9):
	for y in range(0,9):
		Entrylist[x][y].grid(row = x, column = y)

solve_button = Button(root, text = "Solve!" , command = lambda : Button_press(Entrylist))
solve_button.grid(row = 9, column = 3, columnspan = 3)

root.mainloop()
