from tkinter import *

window = Tk()

canvas = Canvas(window, height = 800, width = 800, bg = "white")
canvas.pack()

for i in range(8):
    offset = 0
    if i % 2 == 1:
        offset = 100
        
    for j in range(4):
        canvas.create_rectangle(200*j + offset, i*100, 100 + 200*j + offset, 100 + i * 100, fill = "black")

window.mainloop()

