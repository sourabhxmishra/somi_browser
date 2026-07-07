# 🌐 Somi Browser

A lightweight **tabbed** desktop web browser built with **Python + PyQt5** (Chromium via `QtWebEngine`) — a clean toolbar, a smart address bar, and real multi-tab browsing in ~130 lines.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?logo=qt&logoColor=white)
[![Download](https://img.shields.io/badge/%E2%AC%87_Download-Windows_app-2563EB)](https://github.com/sourabhxmishra/somi_browser/releases/latest)
[![Live preview](https://img.shields.io/badge/%F0%9F%96%A5_Live-web_preview-3b82f6)](https://sourabhxmishra.github.io/somi_browser/)

## 🖥️ Try it online
The tabbed UI, smart address bar, and start portal — running live in your browser:

**[Open the Somi Browser web preview →](https://sourabhxmishra.github.io/somi_browser/)**

## ⬇️ Download & run (Windows)
Download **`SomiBrowser-win64.zip`** from the **[latest release](https://github.com/sourabhxmishra/somi_browser/releases/latest)**, unzip it, and run **`SomiBrowser.exe`** — no Python required. It ships with its own globe app icon.

## ✨ Features
- **Tabs** — open (`＋`), close, and reorder multiple pages
- **Start portal** — a built-in home page with a search box and quick-link tiles
- **Smart address bar** — type a full URL, a bare domain (`github.com`), or any text to Google-search it
- **Navigation** — back ◀, forward ▶, reload ⟳, home ⌂
- **Live titles** — each tab shows the page's title

## 🚀 Run from source
```bash
pip install -r requirements.txt      # PyQt5 + PyQtWebEngine
python app.py
```

## 📦 Build the app yourself
```powershell
py -3.12 -m venv .venv ; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt pyinstaller
.\build.ps1          # → dist\SomiBrowser\SomiBrowser.exe
```

## 🛠️ How it works
Each page is rendered by a Chromium `QWebEngineView`; a `QTabWidget` hosts one view per tab. Toolbar `QAction`s drive the *active* view's back / forward / reload, and the address bar normalises whatever you type into either a URL or a Google search. The home button opens a bundled **`home.html`** portal, and assets resolve through a `resource()` helper so they work both from source and inside the packaged `.exe`.
