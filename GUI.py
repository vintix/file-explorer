import tkinter as tk
############## RGB
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb
############## window
window = tk.Tk()
window.geometry("600x200")
bg_color=_from_rgb((36, 90, 125))
window['bg']=bg_color
############## def
LOL = True
spisok = [0,"test.txt","random.txt","text.txt"]
nolik = 0
############## 
def view():
    print("view!")
    view_window = tk.Toplevel()
    w = tk.Label(view_window, text=spisok)
    w.pack()
def add():
    file_name = input("file name - ")
    print(file_name," вы уверены?")
    vot = int(input("1 - Да. 2 - Нет. >>> "))
    if vot == 1:
        with open(file_name, "w") as file:
            file.write("test")
            print("файл был успешно добавлен.")
            spisok.append(file_name)
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   
############## button
############## import image
button_1=tk.PhotoImage(file="button1.png")
button_2=tk.PhotoImage(file="button2.png")
but1 = tk.Button(window,image=button_1,command=view).place(x=0,y=0)
but2 = tk.Button(window,image=button_2, command=add).place(x=150,y=0)
window.mainloop()
