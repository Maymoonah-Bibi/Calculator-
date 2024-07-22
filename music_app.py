from tkinter import Tk, Frame, Button, Listbox, Menu, PhotoImage, filedialog, END, Label
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

#  now we will Initialize root window
root = Tk()
root.title("Music Player")
root.geometry("500x400")
root.configure(bg='#1E1E1E')  
#  now we are going to Set background color

# Initialize song list and state variables
songs = []
current_song = ""
paused = False

# Function to load music from a directory
def load_music():
    global current_song
    root.directory = filedialog.askdirectory()
    songs.clear()
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)
    update_song_list()

# Update the song listbox with loaded songs
def update_song_list():
    songlist.delete(0, END)
    for song in songs:
        songlist.insert(END, song)
    songlist.selection_set(0)
    set_current_song()

# Set the current song based on selection
def set_current_song():
    global current_song
    if songs:
        current_song = songs[songlist.curselection()[0]]

# Play the selected song
def play_music():
    global current_song, paused
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

# Pause the currently playing song
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

# Play the next song in the list
def next_music():
    global current_song, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        set_current_song()
        play_music()
    except:
        pass

# Play the previous song in the list
def previous_music():
    global current_song, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        set_current_song()
        play_music()
    except:
        pass

# i am Creating menu bar
menubar = Menu(root, bg='#2E2E2E', fg='white')
root.config(menu=menubar)

# now i am Creating  menu items
organize_menu = Menu(menubar, tearoff=0, bg='#2E2E2E', fg='white')
organize_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label="File", menu=organize_menu)

#  then i Create a listbox to display songs
songlist = Listbox(root, bg="black", fg="white", width=100, height=15, selectbackground='#555555', selectforeground='white')
songlist.pack(pady=20)

# Load images
def load_image(file_path):
    try:
        return PhotoImage(file=file_path)
    except Exception as e:
        print(f"Error loading image {file_path}: {e}")
        return None

image_path = "D:/university work/python/project/images/"
play_btn_image = load_image(image_path + "play.png")
pause_btn_image = load_image(image_path + "pause.png")
next_btn_image = load_image(image_path + "next.png")
previous_btn_image = load_image(image_path + "previous.png")
root.image_references = [play_btn_image, pause_btn_image, next_btn_image, previous_btn_image]

#  i Created a frame to hold control buttons
control_frame = Frame(root, bg='#1E1E1E')
control_frame.pack()


if all(root.image_references):
    play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music, bg='#1E1E1E')
    pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music, bg='#1E1E1E')
    next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music, bg='#1E1E1E')
    previous_btn = Button(control_frame, image=previous_btn_image, borderwidth=0, command=previous_music, bg='#1E1E1E')

    #  here i gave padding to buttons 
    previous_btn.grid(row=0, column=0, padx=10, pady=10)
    play_btn.grid(row=0, column=1, padx=10, pady=10)
    pause_btn.grid(row=0, column=2, padx=10, pady=10)
    next_btn.grid(row=0, column=3, padx=10, pady=10)
else:
    print("Failed to load all button images. Check image paths.")


label = Label(root, text="Music Player", font=("Arial", 24), bg='#1E1E1E', fg='white')
label.pack(pady=10)

root.mainloop()