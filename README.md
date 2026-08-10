<div align="center">

<img src="https://i.ibb.co/Z6kGcfM7/image.jpg" alt="Vibe Music" width="400"/>

# 🎵 Vibe X Music

### A Modern Telegram Music Bot for High-Quality Voice Chat Streaming

An open-source Telegram music bot built with **Python**, **Pyrogram**, **PyTgCalls**, and **FFmpeg**, delivering fast, reliable, and high-quality audio streaming directly to Telegram voice chats.

<br>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/namandeep0045-bit/Vibemusicvibesbot?style=for-the-badge)](https://github.com/namandeep0045-bit/Vibemusicvibesbot/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/namandeep0045-bit/Vibemusicvibesbot?style=for-the-badge)](https://github.com/namandeep0045-bit/Vibemusicvibesbot/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/namandeep0045-bit/Vibemusicvibesbot?style=for-the-badge)](https://github.com/namandeep0045-bit/Vibemusicvibesbot/issues)

[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Vibesxmusic)
[![Telegram Support](https://img.shields.io/badge/Telegram-Support-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Vibexmusicbots)

</div>

---

## 📖 About

**Vibe X Music** is a powerful and modern Telegram music bot built for seamless voice chat streaming. It enables users to play music directly in Telegram voice chats using YouTube, live radio, and more.

Designed with performance, stability, and simplicity in mind, the project combines modern asynchronous technologies to provide a fast, reliable, and highly customizable music streaming experience.

---

# 📑 Table of Contents

- [📖 About](#-about)
- [⭐ Why Vibe Music?](#-why-vibe-music)
- [✨ Features](#-features)
- [🏗 Tech Stack](#-tech-stack)
- [📋 Requirements](#-requirements)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Environment Variables](#️-environment-variables)
- [🛠 Installation](#️-installation)
- [📖 Commands](#-commands)
- [📞 Support](#-support)
- [📄 License](#-license)

---

# ⭐ Why Vibe Music?

Choosing the right Telegram music bot shouldn't mean sacrificing performance, reliability, or ease of deployment. Vibe Music is designed with developers and communities in mind, providing a clean, modular, and production-ready solution.

### Highlights

- 🚀 Fast and lightweight architecture
- 🎵 High-quality voice chat streaming
- 🎧 YouTube search and direct URL playback
- 📻 Built-in live radio support
- 📝 Smart queue management
- 🛡 Powerful administrator controls
- 👥 User authorization system
- 🔄 Automatic voice chat cleanup
- 🐳 Docker and Docker Compose support
- ⚙️ Environment-based configuration
- 📂 Modular and maintainable codebase
- ❤️ Open-source under the GPL-3.0 License

---

# ✨ Features

### 🎵 High-Quality Audio Streaming

Experience smooth and crystal-clear music playback optimized for Telegram voice chats using the Opus codec and FFmpeg.

### 🎧 YouTube Integration

Play music instantly from:

- YouTube links
- Search queries
- Supported playlists

### 📻 Live Radio Streaming

Access and stream a collection of online radio stations directly within Telegram voice chats.

### 📝 Smart Queue Management

Manage playlists effortlessly with a built-in queue system.

- Add songs
- View queue
- Skip tracks
- Clear queue

### ⚡ Optimized Performance

Built with asynchronous libraries for efficient resource usage and responsive performance.

### 🎛 Playback Controls

Complete playback management with support for:

- Play
- Pause
- Resume
- Skip
- Stop
- Seek

### 👥 Authorization System

Restrict playback controls to:

- Chat administrators
- Authorized users
- Bot owner
- Sudo users

### 🔄 Automatic Voice Chat Cleanup

Automatically detects inactive voice chats and leaves them to conserve server resources.

### 🐳 Docker Ready

Deploy effortlessly using Docker or Docker Compose for a consistent production environment.

### 🔧 Easy Configuration

Configure the bot entirely through environment variables without modifying the source code.

---

# 🏗 Tech Stack

| Category | Technology |
|-----------|----------|
| Language | Python 3.10+ |
| Telegram Framework | Pyrogram |
| Voice Chat | PyTgCalls |
| Database | MongoDB |
| Media Processing | FFmpeg |
| Containerization | Docker & Docker Compose |
| Version Control | Git |

---

# 📋 Requirements

Before deploying **Vibe X Music**, ensure your system meets the following requirements.

| Software | Version |
|-----------|----------|
| Python | 3.10 or higher |
| FFmpeg | Latest |
| MongoDB | Atlas or Self-hosted |
| Git | Latest |

---

# 🚀 Quick Start

Clone the repository.

```bash
git clone https://github.com/namandeep0045-bit/Vibemusicvibesbot.git
```

Move into the project directory.

```bash
cd Vibemusicvibesbot
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

Start the bot.

```bash
python -m VibeMusicBot
```

---

# ⚙️ Environment Variables

Create a `.env` file in the project's root directory with your credentials.

```env
API_ID=36784100
API_HASH=341f36a62f6078561e906a331e630c95
BOT_TOKEN=8662000369:AAELXvJCONwITbOk26mrsYiCv42r5-ItuKk
OWNER_ID=8556429856
LOGGER_ID=-1004450412752
STRING_SESSION=YOUR_STRING_SESSION_HERE
MONGO_DB_URI=your_mongodb_uri
```

| Variable | Description |
|-----------|----------|
| `API_ID` | Telegram API ID from **my.telegram.org** |
| `API_HASH` | Telegram API Hash |
| `BOT_TOKEN` | Bot Token from **@BotFather** |
| `OWNER_ID` | Your Telegram User ID |
| `LOGGER_ID` | Logger Group/Channel ID |
| `STRING_SESSION` | Pyrogram String Session |
| `MONGO_DB_URI` | MongoDB connection URI |

---

# 📖 Commands

## 👤 User Commands

| Command | Description |
|---------|----------|
| `/play <song/url>` | Play a song from YouTube |
| `/radio` | Browse radio stations |
| `/queue` | Show current queue |
| `/ping` | Check bot status |
| `/help` | Show help menu |

---

## 🛡 Admin Commands

| Command | Description |
|---------|----------|
| `/pause` | Pause playback |
| `/resume` | Resume playback |
| `/skip` | Skip current track |
| `/stop` | Stop playback |
| `/end` | Stop and clear queue |

---

# 📞 Support

Need help? Join our communities:

- 📢 **Telegram Channel**: https://t.me/Vibesxmusic
- 💬 **Telegram Support**: https://t.me/Vibexmusicbots
- 💻 **GitHub**: https://github.com/namandeep0045-bit/Vibemusicvibesbot

---

# 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

---

<div align="center">

## ⭐ Support the Project

If you find **Vibe X Music** useful, give this repository a ⭐ on GitHub!

**Made with ❤️ by Vibe Music Team**

</div>
