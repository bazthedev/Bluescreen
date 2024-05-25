try:
            import tkinter as tk
            import keyboard
            from tkinter import messagebox
            import threading
except Exception:
            messagebox.showerror("Fatal Error Detected", "Unable to import crucial packages")
            stopcode = "Crucial Package Missing"
root = tk.Tk()
root.withdraw()
c = tk.Canvas(root, width = root.winfo_screenwidth(),
height = root.winfo_screenheight(), bg= "#1c00b0", highlightthickness=0)
root.configure(background="#1c00b0")
c.pack()
root.deiconify()
root.title("Bluescreen of Death Simulator - Windows 95")
root.wm_attributes('-fullscreen','true')
root.lift()
root.attributes("-topmost", True)
try:
            from PIL import ImageTk, Image
except Exception:
            messagebox.showwarning("Error", "Unable to import image library")
try:
        ico = Image.open('./Etc/logo.png')
        photo = ImageTk.PhotoImage(ico)
        root.wm_iconphoto(False, photo)
except Exception:
        pass
c.create_rectangle(875, 400, 1050, 370, fill="#a8a8a8", outline="")
c.create_text(900, 390, anchor="w", fill="#1c00b0", font=("Lucida Console", 20), text="Windows")
c.create_text(600, 450, anchor="w", fill="white", font=("Lucida Console", 15), text="An error occured. To continue:")
c.create_text(600, 500, anchor="w", fill="white", font=("Lucida Console", 15), text="Press Enter to return to Windows or,")
c.create_text(600, 550, anchor="w", fill="white", font=("Lucida Console", 15), text="Press CTRL+ALT+DELETE to restart your computer. If you do this, ")
c.create_text(600, 575, anchor="w", fill="white", font=("Lucida Console", 15), text="you will lose any unsaved information in all open applications")
c.create_text(600, 625, anchor="w", fill="white", font=("Lucida Console", 15), text="Error: OE: 016F: BFF9B3D4")
def check():
        while True:
            if keyboard.is_pressed("enter"):
                root.destroy()
                break
            
threading.Thread(target=check).start()
root.mainloop()