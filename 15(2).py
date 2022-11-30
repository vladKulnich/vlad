import tkinter as tk 
def action1():     
    a=radokvodu.get()
    s=a.split(",")
    for i in range(0,len(s)):
        s[i]=float(s[i])
    print(s)
    d=sum(s)/len(s)
    d=str(round(d,2))
    clova.config(text="середнє значення "+d)
    button.config(text='Введіть ще раз')
    radokvodu.delete(0, tk.END)
window = tk.Tk()
fr = tk.Frame(master=window,relief=tk.RAISED, borderwidth=10) 
clova = tk.Label(master=fr,text="введіть цифри через кому", foreground='black',background='yellow',width=50,height=5)
radokvodu = tk.Entry(foreground="white", background="blue", width=30)
button = tk.Button(text="Пуск",width=50,height=2,background="brown",foreground="yellow", command=action1 ) 

fr.pack()
clova.pack() 
radokvodu.pack() 
button.pack()
window.mainloop()
