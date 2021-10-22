import tkinter as tk
from PIL import Image
import glob
import os

def main():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(ROOT_DIR, "input/")
    input_list = glob.glob(os.path.join(input_dir, "input.*"))
    pixel_size = 1
    scale = 30
    
    file = Image.open(input_list[0])
    width, height = file.size
    
    file = file.resize((int(width/scale), int(height/scale)))#debug
    width, height = file.size#debug'''
    pix = file.load()

    
    
    window = tk.Tk()
    
    for x in range(width):
        for y in range(height):
            rgb = pix[x,y]
            frame = tk.Frame(
                master=window,
                borderwidth=0
            )
            frame.grid(row=y, column=x)
            label = tk.Frame(master=frame, width=pixel_size, height=pixel_size)
            label.configure(bg=f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}')
            label.pack()
    
    window.mainloop()

if __name__ == '__main__':
    main()