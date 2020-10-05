import requests
from tkinter import *


def sendhttp(event):
    global url_bar,web_page
    url = url_bar.get()
    response = requests.get(url)
    web_page.configure(state="normal")
    web_page.delete("1.0",END)
    web_page.insert(END, response.text)
    web_page.configure(state="disabled")

display = Tk()

display.title("Simple Browser")
display.iconbitmap('browser.ico')
display.geometry("900x500")
url_bar = Entry(master=display)
url_bar.place(x=20, y=20, width="700", height="20")
search = Button(master=display, bg="blue", fg="white", text="Search")
search.place(x=750, y=20, width="100", height="20")
search.bind("<Button-1>", sendhttp)

scrollview = Scrollbar(display)
scrollview.place(x=880,y=50,width="10",height="430")



web_page = Text(master=display, yscrollcommand= scrollview.set, state="normal")
web_page.place(x=20,y=50,height="430", width="860")
scrollview.config(command = web_page.yview)
display.mainloop()