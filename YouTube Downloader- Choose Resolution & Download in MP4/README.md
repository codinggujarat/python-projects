# 🎬 YouTube Video Downloader using `yt-dlp`

This is a simple Python-based YouTube video downloader built with the `yt-dlp` library. It allows users to download videos in various resolutions including 4K, 2K, 1080p, and 720p. The script automatically merges the best available video and audio streams into a single MP4 file and saves it with a formatted filename.

---

## 🚀 Features

- Supports resolution choices: 2160p (4K), 1440p (2K), 1080p (Full HD), 720p (HD)
- Merges video and audio into a single `.mp4` file
- Automatically names the file as: `Video Title [Resolution].mp4`
- Skips playlist downloads
- Command-line interface for ease of use

---

## 📦 Requirements

- Python 3.6 or higher
- `yt-dlp` package

---

## 🛠️ How It Works

When you run the script, it prompts you to:

1. Enter a YouTube video URL  
2. Select a resolution option (4K, 2K, 1080p, 720p)  
3. Downloads the video with the best quality available within the selected resolution  

---

## 📂 Output

The downloaded video is saved in the current directory with the format:  
`Video Title [Resolution].mp4`

---

## ⚠️ Notes

- Only supports individual video URLs (not playlists)
- Make sure you comply with YouTube's Terms of Service
- Output is saved in the same directory where the script is run

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
