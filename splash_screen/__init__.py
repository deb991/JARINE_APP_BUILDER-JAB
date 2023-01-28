from tkinter import *


def splash_window():
    # Create an instance of tkinter frame
    splash_win = Tk()
    # Set the title of the window
    splash_win.title("Splash Screen Example")
    # Define the size of the window or frame
    # splash_win.geometry("700X200")

    #Remove border of the splash Window

    splash_win.overrideredirect(True)
    # Define the label of the window
    splash_label = Label(splash_win, text= "Hello World!", fg= "green",
                        font= ('Times New Roman', 40)).pack(pady=20)

    splash_win.withdraw()
    splash_win.update_idletasks()  # Update "requested size" from geometry manager

    x = (splash_win.winfo_screenwidth() - splash_win    .winfo_reqwidth()) / 2
    y = (splash_win.winfo_screenheight() - splash_win.winfo_reqheight()) / 2
    splash_win.geometry("+%d+%d" % (x, y))
    splash_win.deiconify()

    return splash_win


def mainWin():
    splash_win.destroy()
    win = Tk()
    win.title("Main Window")
    win.geometry("700x200")
    win_label= Label(win, text= "Main Window", font= ('Helvetica', 25), fg= "red").pack(pady=20)


def static_call(splash_win):
    # splash_win = splash_window()
    splash_win.after(5000, mainWin)
    mainloop()


if __name__ == '__main__':
    """Splash Window is a generic call for generating Slpash Window for any APP.
    Only need to call "splash_win.after(time, app_main function)" for initiate SPLASH Service"""
    splash_win = splash_window()
    static_call(splash_win)
    # splash_win.after(5000, mainWin)
    # mainloop()

