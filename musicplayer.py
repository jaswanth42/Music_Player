import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        root.title("Simple Music Player")
        root.geometry("400x200")

        pygame.init()
        pygame.mixer.init()

        self.playlist = []
        self.current_track = 0

        self.initialize_gui()

    def initialize_gui(self):
        # Create GUI components
        tk.Button(self.root, text="Add Music", command=self.add_music).pack(pady=10)
        tk.Button(self.root, text="Play", command=self.play_music).pack(pady=10)
        tk.Button(self.root, text="Next", command=self.next_track).pack(pady=10)
        tk.Button(self.root, text="Previous", command=self.prev_track).pack(pady=10)
        tk.Button(self.root, text="Create Playlist", command=self.create_playlist).pack(pady=10)
        tk.Button(self.root, text="Load Playlist", command=self.load_playlist).pack(pady=10)

    def add_music(self):
        file_paths = filedialog.askopenfilenames(title="Select MP3 files", filetypes=[("MP3 Files", "*.mp3")])
        if file_paths:
            self.playlist.extend(file_paths)
            tk.Label(self.root, text="Playlist:").pack()
            for index, track in enumerate(self.playlist, start=1):
                tk.Label(self.root, text=f"{index}. {os.path.basename(track)}").pack()

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def next_track(self):
        if self.playlist:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.play_music()

    def prev_track(self):
        if self.playlist:
            self.current_track = (self.current_track - 1) % len(self.playlist)
            self.play_music()

    def create_playlist(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for track in self.playlist:
                    f.write(track + "\n")

    def load_playlist(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                self.playlist = [line.strip() for line in f.readlines()]
                tk.Label(self.root, text="Playlist:").pack()
                for index, track in enumerate(self.playlist, start=1):
                    tk.Label(self.root, text=f"{index}. {os.path.basename(track)}").pack()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
