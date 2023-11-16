import tkinter as tk
import calendar



def show_calendar():
    year = int(year_entry.get())
    month = int(month_entry.get())
    cal = calendar.monthcalendar(year, month)
    weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # New window
    calendar_window = tk.Toplevel(root)
    calendar_window.title('Calendar')
    calendar_window.geometry("380x210")

    # New weekDays tablet
    for i, weekday in enumerate(weeks):
        label = tk.Label(calendar_window, text=weekday)
        label.place(x=(i*50)+20, y=15)
       

    # New daySlots
    for week_num, week in enumerate(cal):
        for day_num, day in enumerate(week):
            label = tk.Label(calendar_window, text=day if day != 0 else '')
            label.place(x=(day_num*50)+20, y=(week_num*30)+35)


# Main window
root = tk.Tk()
root.title('Calendar ')
root.geometry("250x200")

# Inputs
year_label = tk.Label(root, text='Year:')
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

month_label = tk.Label(root, text='Month:')
month_label.pack()
month_entry = tk.Entry(root)
month_entry.pack()

# RED button
show_button = tk.Button(root, text='Press me if you want know', command=show_calendar)
show_button.pack(expand=True)
show_button.pack()

# MainLoop
root.mainloop()