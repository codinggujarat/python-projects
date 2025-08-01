# 🧰 Python & Flask Media Tool Suite

A powerful collection of 5 AI-powered and utility-based media tools built using **Python** and **Flask**, including video generation, background removal, authentication, YouTube downloading, and metadata management.

---

## 📦 Included Projects

### 1. 🎬 AI Text-to-Video Tool with Flask Backend and Image Support

Convert **text and images** into narrated videos using **Flask** and the **ElevenLabs API**.

**Features:**
- Text-to-speech narration
- Upload images as video visuals
- Combines voice and visuals into a video
- Flask backend with frontend UI

**Tech Stack:** Flask, Python, HTML, JS, ElevenLabs API  
**Repo:** [`AI-Text-to-Video-Tool`](./AI-Text-to-Video-Tool-with-Flask-Backend-and-Image-Support)

---

### 2. 🖼️ Background Remover Flask App using Python

Remove image backgrounds with one click using the `rembg` library.

**Features:**
- Upload and preview images
- Removes background using rembg
- Download background-free images

**Tech Stack:** Flask, Python, OpenCV, rembg  
**Repo:** [`Background-Remover`](./Background-Remover-Flask-App-using-Python)

---

### 3. 🔐 FlaskAuth - A Simple Flask Authentication App

A complete user authentication system with login, registration, reset password and a protected dashboard.

**Features:**
- Secure login/signup
- Password reset UI
- Flask-WTF, SQLAlchemy, Flask-Login integration

**Tech Stack:** Flask, Python, WTForms, SQLite  
**Repo:** [`FlaskAuth`](./FlaskAuth-A-Simple-Flask-Authentication-App)

---

### 4. 🎞️ YouTube Video Downloader with Resolution Selector

Download YouTube videos in 4K, 2K, 1080p, or 720p using `yt-dlp` from the command line.

**Features:**
- Choose resolution before download
- Auto-merges best audio/video streams
- Simple CLI prompts

**Tech Stack:** Python, yt-dlp  
**Repo:** [`YouTube Downloader`](./YouTube-Downloader-Choose-Resolution-&-Download-in-MP4)

---

### 5. 🧹 YouTube Metadata Cleaner & Updater

Automatically updates your YouTube video **titles** and **descriptions** using the YouTube Data API.

**Features:**
- OAuth2 login with `client_secret.json`
- Converts titles to UPPERCASE
- Cleans links and appends credits

**Tech Stack:** Python, Google API Client  
**Repo:** [`YouTube Metadata Cleaner`](./YouTube-Metadata-Cleaner-&-Updater)

---

## 💻 Setup Instructions

Each project has its own setup instructions and dependencies. Refer to the `README.md` file inside each project folder for detailed usage.

To get started:
```bash
# Clone this repo
git clone https://github.com/yourusername/media-tool-suite.git
cd media-tool-suite

# Then navigate into each tool's folder and follow its README
cd AI-Text-to-Video-Tool-with-Flask-Backend-and-Image-Support
python app.py
```

---

## 📜 License

All tools in this suite are released under the [MIT License](./LICENSE).

---

## 🙌 Contributions

Feel free to fork this repo and submit PRs for fixes, improvements, or new tools! Suggestions via issues are welcome too.

---

## 📧 Contact

Maintained by [@codinggujarat](https://github.com/codinggujarat)  
For queries, open an [issue](https://github.com/codinggujarat/media-tool-suite/issues)
