# 📥 YouTube Downloader (Python + yt-dlp + FFmpeg)

A simple command-line YouTube downloader built using **Python**, **yt-dlp**, and **FFmpeg**.

This project allows users to:

- 🎬 Download videos in best quality (MP4)
- 🎵 Download audio as MP3
- Automatically merge audio + video using FFmpeg
- Convert audio using FFmpeg post-processing

---

## 🚀 Features

- Simple CLI interface
- High-quality video download
- MP3 audio extraction
- Automatic FFmpeg integration
- Clean project structure
- Easy to extend

---

## 🛠 Tech Stack

- Python 3.x
- yt-dlp
- FFmpeg

---

# 📂 Project Structure

```
project-folder/
│
├── main.py
├── downloader.py
├── utils.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Guide

Follow these steps to run the project on your system.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, create one with:

```
yt-dlp
```

Then run:

```bash
pip install yt-dlp
```

---

## 4️⃣ Install FFmpeg (System Requirement)

This project requires **FFmpeg installed on your system**.

### Windows:
1. Download FFmpeg from:
   https://www.gyan.dev/ffmpeg/builds/
2. Extract it to:
   ```
   C:\ffmpeg
   ```
3. Add:
   ```
   C:\ffmpeg\bin
   ```
   to your System PATH
4. Restart terminal and verify:

```bash
ffmpeg -version
```

If version shows → you're good to go.

---

# ▶️ How to Run the Project

After setup:

```bash
python main.py
```

You will see:

```
1. Download Video
2. Download Audio
```

- Choose `1` for Video (MP4)
- Choose `2` for Audio (MP3)

Paste the YouTube URL and the file will download to the project folder.

---

# 🧪 Testing

You can test using the official yt-dlp test video:

```
https://www.youtube.com/watch?v=BaW_jenozKc
```

---

# 🤝 Contributing

Contributions are welcome! 🚀

Anyone can contribute to improve this project.

## How to Contribute

1. Fork the repository
2. Create a new branch:

```bash
git checkout -b feature-name
```

3. Make your changes
4. Commit:

```bash
git commit -m "Added new feature"
```

5. Push:

```bash
git push origin feature-name
```

6. Open a Pull Request

---

## 💡 Contribution Ideas

- Add download progress bar
- Add GUI (Tkinter / PyQt)
- Add playlist support
- Add download folder selection
- Improve error handling
- Add logging
- Add filename cleaner utility

---

# 📜 License

This project is open-source and free to use for educational purposes.

---

# ⭐ Support

If you found this project helpful:

- ⭐ Star the repository
- 🍴 Fork it
- 📢 Share it
