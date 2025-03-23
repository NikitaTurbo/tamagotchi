import os
import json
import datetime

from threading import Thread
from playsound import playsound

script_dir = os.path.dirname(os.path.abspath(__file__))
media_path = os.path.join(script_dir, "Media")
hamster_json_path = os.path.join(script_dir, "hamster.json")

def music():
	playsound(os.path.join(media_path, "music.mp3"))

Thread(target=music, daemon=True).start()

from PIL import Image, ImageTk

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


window = tk.Tk()
window.title("Hamster 🐹")
window.configure(background="#FFF")

pet_frame = tk.Frame(window)
pet_frame.pack()

states = [
	ImageTk.PhotoImage(Image.open(os.path.join(media_path, "1.jpeg"))),
	ImageTk.PhotoImage(Image.open(os.path.join(media_path, "2.jpeg"))),
	ImageTk.PhotoImage(Image.open(os.path.join(media_path, "3.jpeg"))),
	ImageTk.PhotoImage(Image.open(os.path.join(media_path, "4.jpeg")))
]


if not os.path.exists(hamster_json_path):
    initial_data = {
        "state": "0",
        "life": "100",
        "play": "100",
        "time": ""
    }

    with open(hamster_json_path, 'w') as f:
        json.dump(initial_data, f, indent=2)

with open(hamster_json_path, 'r') as f:
    data = json.load(f)

state = int(data["state"])
state_life = int(data["life"])
state_play = int(data["play"])

if (data["time"] != ""):
	h, m, s = map(float, data["time"].split(':'))
	used = str(datetime.datetime.now() - datetime.timedelta(hours=h, minutes=m, seconds=s)).split()[-1].split(':')
	used[2] = used[2].split('.')[0]
	used_seconds = (int(used[0]) * 60 + int(used[1])) * 60 + int(used[2])
	state_life -= used_seconds // 1
	state_play -= used_seconds // 10
	

data["state"] = str(state)
data["time"] = str(datetime.datetime.now().time())

with open(hamster_json_path, 'w') as f:
    json.dump(data, f, indent=2)

pet = tk.Label(pet_frame, image=states[state])
pet.pack()

settings_frame = tk.Frame(window)
settings_frame.configure(background="#FFF");
settings_frame.pack()

style = ttk.Style(settings_frame)

LIFE_TROUGH_COLOR = "#CCC"
LIFE_BAR_COLOR = "#00FF00"
style.configure("life.bar.Horizontal.TProgressbar", 
				troughcolor=LIFE_TROUGH_COLOR, 
                bordercolor=LIFE_TROUGH_COLOR,
                background=LIFE_BAR_COLOR,
                lightcolor=LIFE_BAR_COLOR, 
                darkcolor=LIFE_BAR_COLOR,
                foreground=LIFE_TROUGH_COLOR
)

PLAY_TROUGH_COLOR = "#CCC"
PLAY_BAR_COLOR = "#FF8000"
style.configure("play.bar.Horizontal.TProgressbar", 
				troughcolor=PLAY_TROUGH_COLOR, 
				bordercolor=PLAY_TROUGH_COLOR,
				background=PLAY_BAR_COLOR,
				lightcolor=PLAY_BAR_COLOR, 
				darkcolor=PLAY_BAR_COLOR,
				foreground=PLAY_TROUGH_COLOR
)

life_progress = ttk.Progressbar(settings_frame, value=state_life, maximum=100, length=200, style="life.bar.Horizontal.TProgressbar")
life_progress.grid(row=0, column=0, padx=25, pady=10)

play_progress = ttk.Progressbar(settings_frame, value=state_play, maximum=100, length=200, style="play.bar.Horizontal.TProgressbar")
play_progress.grid(row=0, column=1, padx=25, pady=10)

def check_life():
	global state
	global states
	global state_life

	state_life -= 1
	life_progress["value"] = state_life
    
	if state_life <= 75:
		state = 1
	if state_life <= 50:
		state = 2
	if state_life <= 25:
		state = 3
		
	with open(hamster_json_path, 'r') as f:
		data = json.load(f)
	
	data["state"] = str(state)
	data["life"] = str(state_life)
	data["time"] = str(datetime.datetime.now().time())
	with open(hamster_json_path, 'w') as f:
		json.dump(data, f, indent=2)

	pet.config(image=states[state])
    
	if state_life <= 1:
		messagebox.showerror(title="Вы проиграли!", message="Зверек умер... :(")
		with open(hamster_json_path, 'r') as f:
			data = json.load(f)
		
		data["time"] = ""
		data["state"] = "0"
		data["play"] = "100"
		data["life"] = "100"
		with open(hamster_json_path, 'w') as f:
			json.dump(data, f, indent=2)

		quit()
	else:
		window.after(1_000, check_life)

def feed():
	global states
	global states
	global state_life

	state = 0
	pet.config(image=states[state])

	state_life = 100
	life_progress["value"] = state_life
	
	with open(hamster_json_path, 'r') as f:
		data = json.load(f)
	
	data["state"] = str(state)
	data["life"] = str(state_life)
	data["time"] = str(datetime.datetime.now().time())
	with open(hamster_json_path, 'w') as f:
		json.dump(data, f, indent=2)

feed_img = ImageTk.PhotoImage(Image.open(os.path.join(media_path, "feed.png")))
feed_btn = tk.Button(settings_frame, image=feed_img, width=152, command=feed)
feed_btn.configure(background="#FFF", borderwidth=0, border=0)
feed_btn.grid(row=1, column=0, padx=25, pady=6)

def check_play():
	global state
	global states
	global state_play

	state_play -= 1
	play_progress["value"] = state_play
	
	if state_play <= 75:
		state = 1
	if state_play <= 50:
		state = 2
	if state_play <= 25:
		state = 3
		
	with open(hamster_json_path, 'r') as f:
		data = json.load(f)
	
	data["state"] = str(state)
	data["play"] = str(state_play)
	data["time"] = str(datetime.datetime.now().time())
	with open(hamster_json_path, 'w') as f:
		json.dump(data, f, indent=2)

	if state_play <= 1:
		messagebox.showerror(title="Вы проиграли!", message="Зверек умер... :(")
		with open(hamster_json_path, 'r') as f:
			data = json.load(f)
		
		data["time"] = ""
		data["state"] = "0"
		data["play"] = "100"
		data["life"] = "100"
		with open(hamster_json_path, 'w') as f:
			json.dump(data, f, indent=2)

		quit()
	else:
		window.after(10_000, check_play)

def play():
	global state
	global states
	global state_play
    
	state = 0
	pet.config(image=states[state])

	state_play = 100
	play_progress["value"] = state_play
	
	with open(hamster_json_path, 'r') as f:
		data = json.load(f)
	
	data["state"] = str(state)
	data["play"] = str(state_play)
	data["time"] = str(datetime.datetime.now().time())
	with open(hamster_json_path, 'w') as f:
		json.dump(data, f, indent=2)

play_img = ImageTk.PhotoImage(Image.open(os.path.join(media_path, "play.png")))
play_btn = tk.Button(settings_frame, image=play_img, width=152, command=play)
play_btn.configure(background="#FFF", borderwidth=0, border=0)
play_btn.grid(row=1, column=1, padx=25, pady=6)

window.after(10_000, check_play)
window.after(1_000, check_life)
window.mainloop()
