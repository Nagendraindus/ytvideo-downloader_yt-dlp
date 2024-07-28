

# YouTube Media Downloader
![image](https://github.com/user-attachments/assets/95680b3b-2958-4618-bea6-f03683306ec2)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
YouTube Media Downloader is a Python-based application that allows users to download videos and audio from YouTube. Built with `tkinter` for the GUI and `yt-dlp` for downloading media, this tool provides an intuitive and efficient way to save YouTube content locally.

## Features
![image](https://github.com/user-attachments/assets/976e37ce-fbfe-4cb4-9999-e1e24dc5ca25)

- **User-Friendly Interface:** A clean GUI built using `tkinter`.
- **Format Selection:** Fetches and displays available video/audio formats for the user to choose from.
- **Thumbnail Preview:** Displays a preview of the video's thumbnail.
- **Custom Download Path:** Users can select their preferred download directory.
- **Seamless Integration:** Uses `yt-dlp` for downloading and FFmpeg for video/audio conversion.

## Installation
### Prerequisites
- Python 3.7 or higher
- `pip` (Python package installer)
- `yt-dlp`
- `ffmpeg`

### Steps
1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/youtube-media-downloader.git
    cd youtube-media-downloader
    ```

2. **Install required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Download and install FFmpeg:**
    - Download from [FFmpeg.org](https://ffmpeg.org/download.html) and follow the installation instructions for your operating system.
    - Ensure `ffmpeg` is added to your system's PATH.

## Usage
1. **Run the application:**
    ```sh
    python youtube_downloader.py
    ```

2. **Using the GUI:**
    - **Enter URL:** Paste the YouTube URL into the input field.
    - **Get Formats:** Click "Get Available Formats" to fetch and display available options.
    - **Select Format:** Choose your desired format from the dropdown menu.
    - **Select Download Directory:** Choose the folder where you want to save the downloaded files.
    - **Download:** Click "Download" to save the video/audio to your selected directory.

## Technical Details
- **Multithreading:** Ensures the application remains responsive during format fetching and downloading.
- **Post-processing:** Uses FFmpeg to convert the downloaded media into the desired format (e.g., MP4).
- **Error Handling:** Provides user feedback in case of errors during the download process.

## Future Enhancements
- Add support for downloading entire playlists.
- Implement progress bars for download status.
- Enhance the GUI with more customization options.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for their powerful YouTube downloading library.
- [FFmpeg](https://ffmpeg.org/) for media processing.
- [Python](https://www.python.org/) for providing an awesome programming language.


