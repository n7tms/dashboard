# dashboard.py
#
# main dashboard screen

import tkinter as tk
import clock_pane as cp

dashboard = tk.Tk()
dashboard.title("Dashboard")

# pi = tk.PhotoImage(file='phone_icon.png')
dashboard.iconphoto(False,tk.PhotoImage(file='phone_icon.png'))
# dashboard.tk.call('wm','iconphoto',dashboard._w, tk.PhotoImage(file='dashboard_logo.png'))



frame = tk.Frame(dashboard)
frame.pack()

# Clock
frmClock = tk.LabelFrame(frame,text="Clock")
frmClock.grid(row=0,column=0,padx=20,pady=20)
cp.clock_panel(frame)

# Weather


# Calendar


dashboard.mainloop()