import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pygame
from pygame import mixer

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if filepath:
        try:
            mixer.init()
            mixer.music.load(filepath)
            mixer.music.play()
        except pygame.error:
            messagebox.showerror("Ошибка", "Не удалось загрузить и проиграть файл.")


#потом че нибудь добавлю

def pause_music():
    if mixer.music.get_busy():
        mixer.music.pause()
    else:
        mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def set_volume(volume):
    mixer.music.set_volume(float(volume) / 100)


def create_player_window():
    window = tk.Tk()
    window.title("TEST player by newt")
    window.geometry("600x200")

    btn_open = tk.Button(window, text="Открыть", command=open_file)
    btn_open.pack(pady=10)

    btn_pause = tk.Button(window, text="Пауза / Возобновить", command=pause_music)
    btn_pause.pack(pady=10)

    btn_stop = tk.Button(window, text="Стоп", command=stop_music)
    btn_stop.pack(pady=10)

    volume_scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume)
    volume_scale.set(50)
    volume_scale.pack(pady=10)

    window.mainloop()

if __name__ == '__main__':
    create_player_window()