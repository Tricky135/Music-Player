import os
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import Toplevel, Label, Button
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

PATH = "C:/Users/PREDATOR/Music"

def addSongs():
    temp_song = filedialog.askopenfilenames(initialdir="Songs/", title="Choose a song",
                                            filetypes=(("mp3 Files", "*.mp3"),))
    if not temp_song:
        return

    for s in temp_song:
        song_name = os.path.basename(s)
        songs_list.insert(END, song_name)

    if songs_list.size() > 0:
        songs_list.select_set(0)
        songs_list.event_generate("<<ListboxSelect>>")

def deleteSong():
    curr_song = songs_list.curselection()
    if curr_song:
        songs_list.delete(curr_song[0])
    else:
        show_alert("No song selected to delete")

def play():
    if songs_list.size() == 0:
        show_alert("No songs in the playlist")
        return
    song = songs_list.get(ACTIVE)
    if not song:
        show_alert("No song selected")
        return
    song_path = os.path.join("E:/Music Player/Songs/", song)
    mixer.music.load(song_path)
    mixer.music.play()
    updatePlayPauseButton()

def pause():
    mixer.music.pause()
    updatePlayPauseButton()

def stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)
    updatePlayPauseButton()

def resume():
    mixer.music.unpause()
    updatePlayPauseButton()

def previous():
    prev = songs_list.curselection()
    if prev:
        previous_one = (prev[0] - 1) % songs_list.size()
        temp2 = songs_list.get(previous_one)
        temp2 = f'E:/Music Player/Songs/{temp2}'
        mixer.music.load(temp2)
        mixer.music.play()
        songs_list.selection_clear(0, END)
        songs_list.activate(previous_one)
        songs_list.selection_set(previous_one)
        updatePlayPauseButton()

def next():
    next_one = songs_list.curselection()
    if next_one:
        next_one = (next_one[0] + 1) % songs_list.size()
        temp = songs_list.get(next_one)
        temp = f'E:/Music Player/Songs/{temp}'
        mixer.music.load(temp)
        mixer.music.play()
        songs_list.selection_clear(0, END)
        songs_list.activate(next_one)
        songs_list.selection_set(next_one)
        updatePlayPauseButton()

def updatePlayPauseButton():
    if mixer.music.get_busy():
        play_pause_button.config(image=pause_icon)
    else:
        play_pause_button.config(image=play_icon)

def togglePlayPause():
    if mixer.music.get_busy():
        pause()
    else:
        play()


def show_alert(message, title="Alert"):
    alert = Toplevel(root)
    alert.title(title)
    alert.geometry("300x150")
    alert.resizable(False, False)

    # Make the alert modal (user must interact with it before returning to the main window)
    alert.grab_set()

    # Calculate position for the center of the main window
    x = root.winfo_x() + root.winfo_width() // 2 - 150
    y = root.winfo_y() + root.winfo_height() // 2 - 75
    alert.geometry(f"+{x}+{y}")

    # Message
    Label(alert, text=message, wraplength=250, pady=20).pack()

    # OK button
    Button(alert, text="OK", command=alert.destroy, width=10).pack(pady=10)

    # Keep the alert on top of the main window
    alert.transient(root)
    alert.wait_window()

root = Tk()
root.title('Enhanced Music Player')
root.geometry("800x600")
root.minsize(800, 600)

# Configure grid to make it responsive
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Initialize mixer
mixer.init()

# Create a style
style = ttk.Style()
style.theme_use('clam')

# Create a frame for the playlist
playlist_frame = ttk.Frame(root, padding="10")
playlist_frame.grid(row=1, column=0, sticky=(N, S, E, W))
playlist_frame.grid_columnconfigure(0, weight=1)
playlist_frame.grid_rowconfigure(0, weight=1)

# Create the listbox to contain songs
songs_list = Listbox(playlist_frame, selectmode=SINGLE, bg="#2c3e50", fg="white", font=('Helvetica', 12),
                     selectbackground="#34495e", selectforeground="white")
songs_list.grid(row=0, column=0, sticky=(N, S, E, W))

# Add scrollbar to the playlist
scrollbar = ttk.Scrollbar(playlist_frame, orient=VERTICAL, command=songs_list.yview)
scrollbar.grid(row=0, column=1, sticky=(N, S))
songs_list.configure(yscrollcommand=scrollbar.set)

# Create a frame for control buttons
control_frame = ttk.Frame(root, padding="10")
control_frame.grid(row=2, column=0, sticky=(E, W))

# Load button icons
play_icon = ImageTk.PhotoImage(Image.open("play_icon.png").resize((32, 32)))
pause_icon = ImageTk.PhotoImage(Image.open("pause_icon.png").resize((32, 32)))
stop_icon = ImageTk.PhotoImage(Image.open("stop_icon.png").resize((32, 32)))
prev_icon = ImageTk.PhotoImage(Image.open("prev_icon.png").resize((32, 32)))
next_icon = ImageTk.PhotoImage(Image.open("next_icon.png").resize((32, 32)))

# Control buttons
play_pause_button = ttk.Button(control_frame, image=play_icon, command=togglePlayPause)
stop_button = ttk.Button(control_frame, image=stop_icon, command=stop)
previous_button = ttk.Button(control_frame, image=prev_icon, command=previous)
next_button = ttk.Button(control_frame, image=next_icon, command=next)

play_pause_button.grid(row=0, column=1, padx=5)
stop_button.grid(row=0, column=2, padx=5)
previous_button.grid(row=0, column=0, padx=5)
next_button.grid(row=0, column=3, padx=5)

# Menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add Songs", command=addSongs)
file_menu.add_command(label="Delete Song", command=deleteSong)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()