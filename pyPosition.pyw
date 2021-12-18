#pyPosition
#Filip Rokita
#www.filiprokita.com



#import
import tkinter as tk
import pyautogui



#def
def start():
    startB.configure(state=tk.DISABLED)
    while True:
        root.update()
        positionL['text'] = pyautogui.position()



#main
pyautogui.PAUSE = 0

root = tk.Tk()
root.title('pyPosition')
root.geometry('300x100')
root.resizable(False, False)


startB = tk.Button(root, text='Start', command=start); startB.pack()
positionL = tk.Label(root, text='Start Grabbing!'); positionL.pack(pady=10)
authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack()


root.mainloop()