import tkinter as tk
from PIL import Image
import glob
import os
import cv2

def main():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(ROOT_DIR, "input/")
    
    pixel_size = 1
    scale = 100
    
    '''input_list = glob.glob(os.path.join(input_dir, "*.jpg"))    
    file = Image.open(input_list[0])
    width, height = file.size'''
    
    input_list = glob.glob(os.path.join(input_dir, "*.mp4"))
    cap = cv2.VideoCapture(input_list[0])
    
    window = tk.Tk()
    
    test = 0
    
    while(1):
        ret, frame = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
            cap.release()
            cv2.destroyAllWindows()
            break
    
        test += 1
        test %= 256
    
        '''file = file.resize((int(width/scale), int(height/scale)))#debug
        width, height = file.size#debug'''
        #pix = file.load()
        
        height = len(frame)
        width = len(frame[0])
        
        
        
        for x in range(width)[::scale]:
            for y in range(1,height)[::scale]:
                #rgb = pix[x,y]
                rgb = [test,test,test]#frame[x][y]

                frame = tk.Frame(
                    master=window,
                    borderwidth=0
                )
                frame.grid(row=y, column=x)
                label = tk.Frame(master=frame, width=pixel_size, height=pixel_size)
                label.configure(bg=f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}')
                label.pack()
        
        print("frame:",test)
        window.mainloop()
        window.destroy()

if __name__ == '__main__':
    main()