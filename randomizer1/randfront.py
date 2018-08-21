from tkinter import *
import randback
import random

def randcommand():
    for item in sorted(random.sample(list(range(1,50)),k=6)) :
        list2.insert()


#Ta funkcja pozwala zaznaczać elementy z listy1. Trzeba to tak zmodyfikować, żeby zaznaczała całość, bo to jest do checkboxa print report...
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.printrep(0,END)
    except IndexError:
        pass

#Ta funkcja jest przedłużeniem funkcji powyżej w backendzie. Pewnie też do modyfikacji... :/
def printrep():
    randback.selwindow(selected_tuple[0])

#Muszą być 4 kanały radia i każdy musi logować jeden parametr radiu backendowym.
#taki chuj, bo nie można w ten sposób użyć "in" a przy przycisku nie można uruchomić komendy z parametrem...
def radio_chA():
    randback.radio(1)
def radio_chB():
    randback.radio(2)
def radio_chC():
    randback.radio(3)
def radio_chD():
    randback.radio(4)

window=Tk()

l1=Label(window,text="Wybierz rodzaj gry:")
l1.grid(row=0,column=2)
l2=Label(window,text="Zaznacz pomiary:")
l2.grid(row=2,column=0)
l3=Label(window,text="Od:")
l3.grid(row=2,column=2)
l4=Label(window,text="Całość pomiarów:")
l4.grid(row=3,column=0)
l5=Label(window,text="Do:")
l5.grid(row=3,column=2)
l6=Label(window,text="Generuj statystyki dla wybranego okresu:")
l6.grid(row=4,column=0,columnspan=2)
l7=Label(window,text="Najczęstsza i najrzadsza liczba:")
l7.grid(row=5,column=0)
l8=Label(window,text="Najczęściej padające liczby:")
l8.grid(row=6,column=0)
l9=Label(window,text="Ilość liczb:")
l9.grid(row=6,column=2)
l10=Label(window,text="Średnie wyników losowań:")
l10.grid(row=7,column=0)
l11=Label(window,text="Generuj wykres:")
l11.grid(row=7,column=2)
l12=Label(window,text="Generuj raporty")
l12.grid(row=8,column=0)
l13=Label(window,text="Zapisz raport:")
l13.grid(row=8,column=2)
l14=Label(window,text="Zagraj w wybraną grę:")
l14.grid(row=15,column=0)

startdate_text=StringVar()
e1=Entry(window,textvariable=startdate_text)
e1.grid(row=2,column=3)

enddate_text=StringVar()
e2=Entry(window,textvariable=enddate_text)
e2.grid(row=3,column=3)

enddate_text=StringVar()
e3=Entry(window,textvariable=enddate_text)
e3.grid(row=6,column=3)

list1=Listbox(window, height=6,width=80)
list1.grid(row=9,column=0,rowspan=6,columnspan=4)
list2=Listbox(window, height=1,width=60)
list2.grid(row=16,column=0,columnspan=3)
sb1=Scrollbar(window)
sb1.grid(row=9,column=4, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListBoxSelect>>',get_selected_row)

b1=Button(window,text="Generuj", width=12)
b1.grid(row=8,column=1)
b1=Button(window,text="Zapisz", width=12)
b1.grid(row=8,column=3)
b1=Button(window,text="Losuj", width=12, command=randcommand)
b1.grid(row=15,column=3)
b1=Button(window,text="Zamknij", width=12, command=window.destroy)
b1.grid(row=16,column=3)

var= IntVar()
r1 = Radiobutton(window, text="MultiMulti", variable=var, value=1, command=radio_chA)
r1.grid(row=1,column=0)
r2 = Radiobutton(window, text="Lotto", variable=var, value=2, command=radio_chB)
r2.grid(row=1,column=1)
r3 = Radiobutton(window, text="Mini Lotek", variable=var, value=3, command=radio_chC)
r3.grid(row=1,column=2)
r4 = Radiobutton(window, text="Ekstra Pensja", variable=var, value=4, command=radio_chD)
r4.grid(row=1,column=3)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
c1 = Checkbutton(window, variable = CheckVar1, onvalue = 1, offvalue = 0)
c1.grid(row=3,column=1)
c2 = Checkbutton(window, variable = CheckVar2, onvalue = 1, offvalue = 0)
c2.grid(row=5,column=1)
c3 = Checkbutton(window, variable = CheckVar3, onvalue = 1, offvalue = 0)
c3.grid(row=6,column=1)
c4 = Checkbutton(window, variable = CheckVar4, onvalue = 1, offvalue = 0)
c4.grid(row=7,column=1)
c5 = Checkbutton(window, variable = CheckVar5, onvalue = 1, offvalue = 0)
c5.grid(row=7,column=3)


window.mainloop()
