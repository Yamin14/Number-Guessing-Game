from tkinter import *
import random
root = Tk()

root.geometry("200x200")
bg = "green"
fg = "yellow"
root.config(background=bg)
mytext = ""
attempt = 1
what = """What is x?
Attempt number 1
"""

def play():
	global mytext, attempt, what
	attempt = 1
	num = random.randint(1, 101)
	prime = True

	for i in range(2,num):
		if num%i == 0:
			prime = False
		
	if prime == False:
		mytext = """x is a number between 1 and 100
x is not a prime number
"""
	if prime == True:
		mytext = """x is a number between 1 and 100
x is a prime number
"""

	lbl = Label(root, text=(mytext+what), bg=bg, fg=fg, font=("Comic Sans MS", 12))
	lbl.place(relx=0.5,rely=0.3,		anchor=CENTER)
	
	def check(num, ans):
		global mytext, attempt, what
		if num == int(ans):
			guessed = True

		elif num != int(ans):
			guessed= False
			attempt += 1

		if guessed == True:
			lbl.destroy()
			entrybox.destroy()
			submit.destroy()
			passed(num)
			
		elif guessed == False and attempt == 2:
			multiple = num * random.randint(2,7)
			mytext = mytext + """{} is a multiple of x
""".format(multiple)
			what = """What is x?
Attempt number 2"""
			lbl['text'] = mytext+what

		elif guessed==False and attempt==3:
			what = """What is x?
Final attempt"""
			for i in range(2,num):
				if num>i and i> num/3:
					great = i
					break
			mytext = mytext + """x is greater than {}
""".format(great)
				
			lbl['text'] = mytext + what
		
		else:
			lbl.destroy()
			entrybox.destroy()
			submit.destroy()
			fail(num)

	entrybox = Entry(root, font=("Comic Sans MS", 20))
	entrybox.place(relx=0.5,rely=0.5,		anchor=CENTER, height=100, width=100)
	
	submit = Button(root, text="Submit", activebackground="sky blue", padx=50, pady=14, bg="cyan", fg="#0000ff", command=lambda: check(num, entrybox.get()))
	submit.place(relx=0.5,rely=0.7,		anchor=CENTER)

def PlayAgain1(lbl1, p1, q):
	lbl1.destroy()
	p1.destroy()
	q.destroy()
	play()

def PlayAgain2(lbl2, p2, q):
	lbl2.destroy()
	p2.destroy()
	q.destroy()
	play()

def Quit():
	root.destroy()

def fail(num):
	lbl1 = Label(root, text='Incorrect! x is equal to {} '.format(num), bg=bg, fg=fg, font=("Comic Sans MS", 15))
	lbl1.place(relx=0.5, rely=0.4, anchor=CENTER)
	quit = Button(root, text='Quit', activebackground="sky blue", padx=50, pady=14, bg="cyan", fg="#0000ff", command = Quit)
	quit.place(relx=0.65, rely=0.6, anchor=CENTER)
	playagain1 = Button(root, text='Play Again', activebackground="sky blue", padx=50, pady=14, bg="cyan", fg="#0000ff", command = lambda: PlayAgain1(lbl1, playagain1, quit))
	playagain1.place(relx=0.35, rely=0.6, anchor=CENTER)
	
def passed(num):
	lbl2 = Label(root, text='Correct! x is equal to {} '.format(num), bg=bg, fg=fg, font=("Comic Sans MS", 15))
	lbl2.place(relx=0.5, rely=0.4, anchor=CENTER)
	quit = Button(root, text='Quit', activebackground="sky blue", padx=50, pady=14, bg="cyan", fg="#0000ff", command = Quit)
	quit.place(relx=0.65, rely=0.6, anchor=CENTER)
	playagain2 = Button(root, text='Play Again', activebackground="sky blue", padx=50, pady=14, bg="cyan", fg="#0000ff", command = lambda: PlayAgain2(lbl2, playagain2, quit))
	playagain2.place(relx=0.35, rely=0.6, anchor=CENTER)
	

play()
root.mainloop()
