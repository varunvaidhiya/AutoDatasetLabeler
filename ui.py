import tkinter as tk
from tkinter import filedialog, messagebox
import yaml
import os
from main import extract_frames, label_frame, load_config

class LabelingApp:
    def __init__(self, master):
        self.master = master
        master.title("Autonomous Vehicle Data Labeling")

        self.config = load_config()

        self.video_path = tk.StringVar()
        self.video_path.set(self.config['video']['input_path'])

        self.output_folder = tk.StringVar()
        self.output_folder.set(self.config['video']['output_folder'])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Video File:").grid(row=0, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.video_path, width=50).grid(row=0, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_video).grid(row=0, column=2)

        tk.Label(self.master, text="Output Folder:").grid(row=1, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.output_folder, width=50).grid(row=1, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_output).grid(row=1, column=2)

        tk.Button(self.master, text="Start Labeling", command=self.start_labeling).grid(row=2, column=1)

    def browse_video(self):
        filename = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
        if filename:
            self.video_path.set(filename)

    def browse_output(self):
        foldername = filedialog.askdirectory()
        if foldername:
            self.output_folder.set(foldername)

    def start_labeling(self):
        video_path = self.video_path.get()
        output_folder = self.output_folder.get()

        if not os.path.exists(video_path):
            messagebox.showerror("Error", "Video file does not exist.")
            return

        frame_count = extract_frames(video_path, output_folder)
        messagebox.showinfo("Extraction Complete", f"Extracted {frame_count} frames from the video.")

        labeled_data_file = self.config['labeling']['output_file']
        with open(labeled_data_file, "w") as outfile:
            for i in range(frame_count):
                frame_path = os.path.join(output_folder, f"frame_{i:04d}.jpg")
                label = label_frame(frame_path)
                outfile.write(f"Frame {i}:\n{label}\n\n")
                self.master.update()  # Update the UI to prevent freezing

        messagebox.showinfo("Labeling Complete", f"Labeling complete. Results saved to {labeled_data_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LabelingApp(root)
    root.mainloop()
