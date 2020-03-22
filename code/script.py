from tkinter import *
import subprocess
import os



root = Tk()
root.title('Solver')

Error_label = Label(text = "Invalid Values")
Unsolvable_label = Label(text = "Given values are unsolvable for sudoku")
needclearance = False

# Unsolvable_label.grid_forget()

def error():
	Error_label.grid(row = 10, column = 1, columnspan= 7)

def unsolvable():
	Unsolvable_label.grid(row = 11, column = 1, columnspan = 9)

def clear():
	Error_label.grid_forget()
	Unsolvable_label.grid_forget()

	# Error_label = Label(text = "Invalid Values")
	# Unsolvable_label = Label(text = "Given values are unsolvable for sudoku")
	needclearance = False


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
	global needclearance

	print(needclearance)

	if(needclearance):
		clear()

	input_string = ""
	for x in range(0,9):
		for y in range(0,9):
			val = Entrylist[x][y].get()
			if val=="":
				val = "0"
			
			if len(val)>1 :
				error()
				needclearance = True
				
			if not (val[0] >= "0" and val[0]<= "9"):
				error()
				needclearance = True
				

			input_string = input_string+val
		input_string = input_string + '\n'
	
	print(input_string)

	output_string = solver(input_string)

	print(output_string)

	if output_string[0] == '-':
		unsolvable()
		needclearance = True
		return

	for x in range(0,9):
		for y in range(0,9):
			Entrylist[x][y].delete(0,END)
			Entrylist[x][y].insert(0 , output_string[x*9 + y + x])

	return



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
