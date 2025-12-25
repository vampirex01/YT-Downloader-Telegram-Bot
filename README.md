# 🎬 YouTube Downloader Telegram Bot

A powerful Telegram bot that downloads YouTube videos in the best quality and uploads them directly to Telegram. Built with Pyrogram and yt-dlp.

## ✨ Features

- 📥 Download YouTube videos in best quality (video + audio merged)
- 🎬 Automatic video and audio merging with FFmpeg
- 📤 Direct upload to Telegram with streaming support
- 📝 Support for single YouTube links or batch downloads via `.txt` files
- 🖼️ Automatic thumbnail generation and optimization
- 🗑️ Automatic cleanup of downloaded files
- 🍪 Cookie support for age-restricted and private videos
- 🌐 Cross-platform (Windows & Linux)

## 📋 Prerequisites

### Common Requirements
- **Python 3.8 or higher**
- **FFmpeg** installed on your system
- **Telegram Bot Token** - Get from [@BotFather](https://t.me/BotFather)
- **Telegram API credentials** - Get from [my.telegram.org](https://my.telegram.org)
  - API ID
  - API Hash

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/vampirex01/YT-Downloader-Telegram-Bot.git
cd YT-Downloader-Telegram-Bot
```

---

## 🪟 Windows Setup

### 1. Install FFmpeg

**Option A: Using Winget (Recommended)**
```powershell
winget install Gyan.FFmpeg
```

**Option B: Manual Installation**
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract the archive to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to system PATH:
   - Press `Win + X` → System → Advanced system settings
   - Click "Environment Variables"
   - Under "System variables", find `Path` and click Edit
   - Click "New" and add `C:\ffmpeg\bin`
   - Click OK on all windows

**Verify Installation:**
```powershell
ffmpeg -version
```

### 2. Set Up Python Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure YouTube Cookies (Optional but Recommended)

YouTube may require sign-in for some videos. To bypass this:

1. Install [Cookie Editor](https://cookie-editor.com/) browser extension
2. Go to [YouTube](https://youtube.com) and sign in to your account
3. Click the Cookie Editor extension icon
4. Click "Export" → Choose "Netscape" format
5. Save the exported cookies as `cookies.txt` in the bot directory

### 4. Configure the Bot

Edit `bot.py` and replace these values:

```python
API_ID = YOUR_API_ID  # From my.telegram.org
API_HASH = "YOUR_API_HASH"  # From my.telegram.org
BOT_TOKEN = "YOUR_BOT_TOKEN"  # From @BotFather
```

### 5. Run the Bot

```powershell
# Make sure virtual environment is activated
.\venv\Scripts\Activate.ps1

# Run the bot
python bot.py
```

---

## 🐧 Linux Setup

### 1. Install FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg -y
```

**Fedora:**
```bash
sudo dnf install ffmpeg -y
```

**Arch Linux:**
```bash
sudo pacman -S ffmpeg
```

**Verify Installation:**
```bash
ffmpeg -version
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure YouTube Cookies (Optional but Recommended)

YouTube may require sign-in for some videos. To bypass this:

1. Install [Cookie Editor](https://cookie-editor.com/) browser extension
2. Go to [YouTube](https://youtube.com) and sign in to your account
3. Click the Cookie Editor extension icon
4. Click "Export" → Choose "Netscape" format
5. Save the exported cookies as `cookies.txt` in the bot directory

### 4. Configure the Bot

Edit `config.py` and replace these values:

```python
API_ID = YOUR_API_ID  # From my.telegram.org
API_HASH = "YOUR_API_HASH"  # From my.telegram.org
BOT_TOKEN = "YOUR_BOT_TOKEN"  # From @BotFather
```

### 5. Run the Bot

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run the bot
python3 bot.py
```

---

## 📖 Usage

### Basic Usage

1. **Start the bot** - Send `/start` to your bot on Telegram
2. **Single video download** - Send a YouTube link directly
3. **Batch download** - Send a `.txt` file with multiple YouTube links (one per line)

### Example

**Single video:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

**Batch download (.txt file):**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=jNQXAC9IVRw
https://youtu.be/9bZkp7q19f0
```

The bot will:
- ✅ Download the video in best quality (video + audio merged)
- ✅ Generate and optimize thumbnail
- ✅ Upload to Telegram with streaming support
- ✅ Automatically cleanup downloaded files

---

## 🎯 How to Get Telegram Credentials

### Get API ID and API Hash

1. Go to [my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Click on "API Development Tools"
4. Fill in the application details (any name works)
5. Copy your `API ID` and `API Hash`

### Get Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the prompts to create your bot
4. Copy the bot token provided

---

## 🍪 Cookie Configuration (For Age-Restricted Videos)

Some YouTube videos require sign-in or are age-restricted. Use cookies to bypass this:

### Using Cookie Editor Extension

1. **Install Extension:**
   - Chrome/Edge: [Cookie Editor Chrome Store](https://cookie-editor.com/)
   - Firefox: [Cookie Editor Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)

2. **Export Cookies:**
   - Go to [YouTube](https://youtube.com) and **sign in** to your account
   - Click the **Cookie Editor** extension icon
   - Click **"Export"** button
   - Select **"Netscape"** format
   - Copy the exported text

3. **Save Cookies:**
   - Create a file named `cookies.txt` in your bot directory
   - Paste the exported cookies
   - Save the file

The bot will automatically use `cookies.txt` if it exists.

---

## 🚀 Deployment

### Running in Background (Linux)

#### Option 1: Using `screen`

```bash
# Install screen
sudo apt install screen -y

# Create new screen session
screen -S ytbot

# Activate environment and run bot
source venv/bin/activate
python3 bot.py

# Detach from screen: Ctrl+A then D
# Reattach: screen -r ytbot
# List sessions: screen -ls
```


## 📁 Project Structure

```
YT-Downloader-Telegram-Bot/
├── bot.py                    # Main bot script
├── requirements.txt          # Python dependencies
├── cookies.txt              # YouTube cookies (optional)
├── README.md                # Documentation
├── venv/                    # Virtual environment (created during setup)
└── *.session                # Pyrogram session files (auto-generated)
```

---

## 🔧 Troubleshooting

### Windows Issues

**Execution Policy Error:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**FFmpeg not found:**
- Verify FFmpeg is in PATH: `ffmpeg -version`
- Restart terminal after adding to PATH

### Linux Issues

**Permission Denied:**
```bash
chmod +x bot.py
```

**Python not found:**
```bash
sudo apt install python3 python3-pip python3-venv -y
```

### Common Issues

**"Sign in to confirm your age" error:**
- Add `cookies.txt` file with your YouTube cookies (see Cookie Configuration section)

**Import errors:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Bot not responding:**
- Check bot token is correct
- Verify API credentials
- Check internet connection
- Review terminal output for errors

---

## 📝 Requirements

```
pyrogram
TgCrypto
yt-dlp
requests
Pillow
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is open source and available for personal and educational use.

---

## 👤 Developer

**Vampire**
- Telegram: [@Vampirex01](https://t.me/Vampirex01)
- GitHub: [@vampirex01](https://github.com/vampirex01)

---

## ⚠️ Disclaimer

This bot is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws. Download only videos you have permission to download.

---

## 🌟 Support

If you find this project helpful, please give it a ⭐ on GitHub!
