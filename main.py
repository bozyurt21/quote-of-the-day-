import requests
from tkinter import *
from datetime import *
import textwrap

FONT_NAME="Bebas-neue"


def show_the_quote():
    request = requests.get("https://favqs.com/api/qotd")
    request.raise_for_status()
    data = request.json()
    quote=data['quote']['body']
    # line break
    formatted_text = textwrap.fill(quote,width=30)
    quote_text.config(text=f"{formatted_text}")
    name_of_the_author.config(text=f"{data['quote']['author']}")
current_day=datetime.now()
formatted_date=current_day.strftime("%d.%m.%Y")
#tkinter Window
window=Tk()
window.title("Quote Of the Day")
window.config(bg="black",pady=50,padx=50,width=450,height=300)
#image of the button
button_image=PhotoImage(file="./img/book.png")
# Quote of the day text
text=Label(text="QUOTE OF THE DAY", font=(FONT_NAME,64,"bold"),bg="black",fg="white",highlightthickness=0)
text.grid(column=1,columnspan=3,row=1)
text.config(pady=50)
#Quote comes from API which will change when we click the button
quote_text=Label(text="", font=(FONT_NAME,32,"normal"),bg="black",fg="white",highlightthickness=0)
quote_text.grid(column=2,row=2)

#author name
name_of_the_author=Label(text="", font=(FONT_NAME,15,"normal"),bg="black",fg="white",highlightthickness=0)
name_of_the_author.grid(column=2,row=3)
#date of the day
date_text=Label(text=f"{formatted_date}",font=(FONT_NAME,12,"bold"),bg="black",fg="white",highlightthickness=0)
date_text.config(pady=50) #too close to the button
date_text.grid(column=2, row=4)


quote_button=Button(image=button_image,highlightthickness=0,width=70,height=70,command=show_the_quote)
quote_button.grid(column=2,row=5)





window.mainloop()