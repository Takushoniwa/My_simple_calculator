import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from tkinter import *
import requests
import smtplib
import tkinter as tk
import webbrowser
import time
import threading
from threading import Timer



root=tk.Tk()
root.geometry("550x300")
root.title("Gamesplanet.uk price tracker")

email_label=Label(root, text="Email address")
email_label.grid(row=2, column=0)
u=Entry(root, text="your email address", width=50)
u.grid(row=2, column=1)

password_label=Label(root, text="Password")
password_label.grid(row=3, column=0)
p=Entry(root, text="password", show="*", width=50)
p.grid(row=3, column=1)

notice=Label(root, text="You first need to allow less secure \n app access on your gmail account")
notice.grid(row=0, column=1)

e=Entry(root, text="Gamesplanet game URL", width=50)
e.grid(row=4, column=1)
url_label=Label(root, text="Gamesplanet game \n URL")
url_label.grid(row=4, column=0, padx=20)

triggerprice =Entry(root, width=2)
triggerprice.grid(row=6, column=1, ipadx=10, pady=0)
triggerpricelabel=Label(root, text="Notify me when price falls below £")
triggerpricelabel.grid(row=5, column=1)


def sendmail():
	server=smtplib.SMTP('smtp.gmail.com' ,587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login(u.get(), p.get())
	subject='Game discount tracker notification'
	body='You favourate game is now on a discount!!!, check the gamesplanet link ' + str(e.get())

	msg= f"Subject:{subject} \n\n {body}"

	server.sendmail(u.get(), u.get(), msg)
	server.quit()

def allowlesssecure():
	webbrowser.open('https://myaccount.google.com/lesssecureapps')

def request():
	uclient=ureq(e.get())
	pagehtml=uclient.read()
	pagesoup=soup(pagehtml, 'html.parser')
	uclient.close()

	title=pagesoup.findAll("span",{"class":"prod-title"})
	gametitle=title[0].text

	price=pagesoup.findAll("span",{"class":"price_current"})
	gameprice=price[0].text
	gameprice=float(gameprice.replace("£", ""))

	filename="Game and price gamesplanet.csv"
	f=open(filename,"w")
	headers="Gametitle, price \n"

	f.write(headers)

	f.write(gametitle + "," + str(gameprice) + "\n")

	f.close()

	if gameprice <= int(triggerprice.get()):
		sendmail()
		success=Label(root, text= gametitle + "\n is now on discount and its price has fallen \n below £" + str(triggerprice.get()) + " to a price of £" + str(gameprice) + "\n An email notification has also been sent to your email")
		success.grid(row=8, column=1)
		print("An email notifying you of the new price has been sent to your email")

	elif gameprice > int(triggerprice.get()):
		print("No discount for this game")
		note=Label(root, text="There is currently no discount for " + "\n" + gametitle + "\n" "The program will continue tracking this game \n in the background and email you when \n the game falls below " + "£" + str(triggerprice.get()))
		note.grid(row=8, column=1)
	
		Timer(43200, request).start()
	   

button1=Button(root, text="Track and notify me via email if there is a discount", command=request)
button1.grid(row=7, column=1)

button2=Button(root, text="Allow", command=allowlesssecure)
button2.grid(row=1, column=1)


root.mainloop()


