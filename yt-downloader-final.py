import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import yt_dlp
import os
import threading
import requests
from io import BytesIO

# Colors
colors = {
    "kelly_green": "#29bf12",
    "green_yellow": "#abff4f",
    "verdigris": "#08bdbd",
    "red_munsell": "#f21b3f",
    "princeton_orange": "#ff9914"
}

# Function to get available formats
def get_formats():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    def fetch_formats():
        try:
            ydl_opts = {
                'quiet': True,
                'format': 'best',
                'retries': 10,  # Increase the number of retries
                'socket_timeout': 15,  # Increase the socket timeout
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                
                if 'entries' in info_dict:
                    # This is a playlist, get information from the first video
                    first_video = info_dict['entries'][0]
                    formats = first_video.get('formats', [])
                    title = first_video.get('title', 'Unknown Title')
                    thumbnail_url = first_video.get('thumbnail', '')
                else:
                    # This is a single video
                    formats = info_dict.get('formats', [])
                    title = info_dict.get('title', 'Unknown Title')
                    thumbnail_url = info_dict.get('thumbnail', '')

                # Update the title label
                title_label.config(text=f"Title: {title}")

                # Update the thumbnail
                if thumbnail_url:
                    response = requests.get(thumbnail_url)
                    img_data = response.content
                    img = Image.open(BytesIO(img_data))
                    img = img.resize((200, 150), Image.LANCZOS)
                    img_tk = ImageTk.PhotoImage(img)
                    thumbnail_label.config(image=img_tk)
                    thumbnail_label.image = img_tk
                else:
                    thumbnail_label.config(image='')

                available_formats = []
                for f in formats:
                    try:
                        format_option = f"{f['format_id']} - {f['ext']} - {f['format_note']} - {f['resolution']} - {f['fps']}fps"
                        available_formats.append((format_option, f['format_id']))
                    except KeyError:
                        continue

                if available_formats:
                    format_menu['menu'].delete(0, 'end')
                    for option, format_id in available_formats:
                        format_menu['menu'].add_command(label=option, command=tk._setit(selected_format, format_id))
                    selected_format.set(available_formats[0][1])
                else:
                    messagebox.showinfo("Info", "No available formats for this video or playlist.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    threading.Thread(target=fetch_formats).start()

# Function to download the selected format
def download_media():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    format_id = selected_format.get()
    ydl_opts = {
        'format': format_id + "+bestaudio/best",
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': r'C:\ffmpeg',  # Update this path
        'retries': 10,  # Increase the number of retries
        'socket_timeout': 15,  # Increase the socket timeout
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Ensure the final format is mp4
        }],
    }

    def download():
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Success", f"Media downloaded successfully to {download_path}!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    threading.Thread(target=download).start()

# Function to select download directory
def select_download_directory():
    global download_path
    download_path = filedialog.askdirectory()
    if download_path:
        download_path_label.config(text=f"Download Path: {download_path}")

# Initialize main window
root = tk.Tk()
root.title("YouTube Media Downloader")
root.configure(bg=colors["verdigris"])

# URL entry
tk.Label(root, text="YouTube URL:", bg=colors["verdigris"], fg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

# Video title and thumbnail
title_label = tk.Label(root, text="Title: ", bg=colors["verdigris"], fg="white", font=("Arial", 12, "bold"))
title_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
thumbnail_label = tk.Label(root, bg=colors["verdigris"])
thumbnail_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Quality options
tk.Button(root, text="Get Available Formats", command=get_formats, bg=colors["princeton_orange"], fg="white", font=("Arial", 12)).grid(row=3, column=1, pady=10)
selected_format = tk.StringVar()
format_menu = tk.OptionMenu(root, selected_format, "")
format_menu.config(font=("Arial", 12))
format_menu.grid(row=4, column=1, padx=10, pady=10)

# Download directory selection
download_path = os.getcwd()  # Default to current working directory
download_path_label = tk.Label(root, text=f"Download Path: {download_path}", bg=colors["verdigris"], fg="white", font=("Arial", 12, "bold"))
download_path_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
tk.Button(root, text="Select Download Directory", command=select_download_directory, bg=colors["green_yellow"], fg="black", font=("Arial", 12)).grid(row=6, column=1, pady=10)

# Download button
tk.Button(root, text="Download", command=download_media, bg=colors["kelly_green"], fg="white", font=("Arial", 12, "bold")).grid(row=7, column=1, pady=20)

# Run the application
root.mainloop()
