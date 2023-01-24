# clock_pane.py
#
# Clock applet to be used with dashboard.py
# accepts a parent frame when called.
#
# https://www.pythonguis.com/tutorials/pyside-qml-animations-transformations/
#
# with only built-in libraries:
# https://www.plus2net.com/python/tkinter-analog-clock-dial.php
#
#
import tkinter as tk
from datetime import datetime

def clock_panel(f:tk.Frame) -> tk.Frame:

    def update_clock():
        """Update the clock every second."""
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        lbllocaltime.configure(text=current_time)
        lblUTCtime.configure(text=current_time)
        f.after(1000,update_clock)


    lblLocal = tk.Label(f,text="Local:")
    lblLocal.grid(row=0,column=0,padx=5,pady=20)
    lbllocaltime = tk.Label(f,text="")
    lbllocaltime.grid(row=0,column=1,padx=5,pady=20)

    lblUTC = tk.Label(f,text="UTC:")
    lblUTC.grid(row=1,column=0,padx=5,pady=20)
    lblUTCtime = tk.Label(f,text="")
    lblUTCtime.grid(row=1,column=1,padx=5,pady=20)


    update_clock()
    return f

