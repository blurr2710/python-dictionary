from tkinter import *
import trie
import dictionary
# Let calc accept the arguments passes by trace_add
global suggestions
def OnClick(event):
	global suggestions
	w=event.widget
	sl=w.curselection()
	if(len(sl)>0):
		#print(len(suggestions))
		e1.delete(0,len(e1.get()))
		e2.delete(0,len(e2.get()))
		mean=dic_object.meaning(suggestions[sl[0]])
		e1.insert(0,suggestions[sl[0]])
		e2.insert(0,mean)
def calc(*args):
    # Get the values from the StringVar objects
    global suggestions
    Lb.delete(0,Lb.size())
    val1 = v1.get()
    Lb.bind("<Button-1>", OnClick)
    #val2 = v2.get()
    #val3 = v3.get()
    #val4 = v4.get()
    res = val1 
    #print(res)
    if(len(res)==0):
    	return
    t=trie.Trie()
    t.initialize(t)
    suggestions=t.prefix_search(res)
    counter=0;
    for i in suggestions:
            Lb.insert(counter,i)
            counter=counter+1
    #print(suggestions)
    # Only change the text of the existing Label
    label2["text"] = res

master = Tk()
master.geometry("600x700")
dic_object=dictionary.Dictionary()
dic_object.initialize()
suggestions=[]
Lb = Listbox(master) 
# make this Label once
label2 = Label(master)
label2.grid(row=4, column=1)

Label(master, text="Enter word").grid(row=0, sticky=E)
#Label(master, text="Second Value").grid(row=1, sticky=E)
#Label(master, text="Third Value").grid(row=2, sticky=E)
#Label(master, text="Fourth Value").grid(row=3, sticky=E)
Label(master, text="meaning").grid(row=20, sticky=E)

#Label(master, text="suggestions").grid(row=2, sticky=E)
# Create StringVars
v1 = StringVar()
v2 = StringVar()
#v3 = StringVar()
#v4 = StringVar()

e1 = Entry(master, textvariable=v1)
e2 = Entry(master, textvariable=v2)
#e3 = Entry(master, textvariable=v3)
#e4 = Entry(mastextvariable=v4)

# Trace when the StringVars are written
v1.trace_add("write", calc)
#v2.trace_add("write", calc)
#v3.trace_add("write", calc)
#v4.trace_add("write", calc)

e1.grid(row=0, column=1)
e2.grid(row=20,column=1)
Lb.grid(row=16,column=1)
#e2.grid(row=1, column=1)
#e3.grid(row=2, column=1)
#e4.grid(row=3, column=1)

master.mainloop()