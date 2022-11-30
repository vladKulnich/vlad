import tkinter as tk 
import json
def action1():     
    q=radokvodu.get()
    if q in a:
        clova.config(text=a[q])
        button.config(text='Введіть новий елемент')
    else:
        clova.config(text='не може розпізнати,попробуйте ще раз')
with open('менделєєв.json', 'r') as jsonfile: 
    a=json.load(jsonfile)
    print(a)

window = tk.Tk()
window.geometry("410x380")
window["bg"]="olive drab"
clova = tk.Label(text="введіть елемент", foreground='black',background='yellow',width=50,height=5)
radokvodu = tk.Entry(foreground="white", background="blue", width=30)
button = tk.Button(text="Пуск",width=50,height=2,background="brown",foreground="yellow",command=action1 ) 
clova.pack() 
radokvodu.pack() 
button.pack()
window.mainloop()