from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image
import requests
import turtle
from turtle import *
import os

def Loading():
	t = turtle.Turtle()
  	
    
	r = -50
	turtle.write('LOADING')
	
	for x in range(3):
		color('white')
		t.circle(r)
		color('white')
		
	url = turtle.textinput('ENTER WEBSITE URL','for ex https://example.com')
	file_name = turtle.textinput('FILE','ENTER FILE NAME for ex: mywebsite')
	running = True
	while running:
		try:
			path = turtle.textinput('PATH','ENTER THE PATH FOR YOUR FILE')
			os.chdir(path)
			break
		except:
			continue
	turtle.clear()
	r = -50
	turtle.write('PROCESSING PLEASE WAIT')
	
	for x in range(3):
		
		t.circle(r)

	file_ext = file_name + ".html"
	html = requests.get(url)
	new_file = open(file_ext,'w')
	new_file.write(html.text)
	new_file.close()
	done = Tk()
	done.title('MyWebScraper')
	done.configure(bg='black')
	done.geometry('500x500')
	Label(done, text='DONE',bg='black',fg='white',pady=50,anchor='center',font=('arial',80,'bold')).pack()
	done.mainloop()

		


root = Tk()
root.geometry('700x700')
root.title('MyWebScraper')
root.configure(bg='black')
Label(root, text='MyScraper',font=('arial',80,'bold'),fg='white',bg='black',pady=50).pack()
Button(root, text='SCRAPE NOW',bg='white',fg='black',padx=20,pady=20,anchor='center',command=Loading).pack()
Button(root, text='RATE APP',bg='white',fg='black',padx=20,pady=20,anchor='center').pack()
Button(root, text='EXIT',bg='white',fg='black',padx=20,pady=20,anchor='center',command=root.destroy).pack()
root.mainloop()
