# 🌐 Somi Browser

A lightweight **tabbed** desktop web browser built with **Python + PyQt5** (Chromium via `QtWebEngine`) — a clean toolbar, a smart address bar, and real multi-tab browsing in ~130 lines.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?logo=qt&logoColor=white)

## ✨ Features
- **Tabs** — open (`＋`), close, and reorder multiple pages
- **Smart address bar** — type a full URL, a bare domain (`github.com`), or any text to Google-search it
- **Navigation** — back ◀, forward ▶, reload ⟳, home ⌂
- **Live titles** — each tab shows the page's title

## 🚀 Run it
```bash
pip install -r requirements.txt      # PyQt5 + PyQtWebEngine
python app.py
```

## 🛠️ How it works
Each page is rendered by a Chromium `QWebEngineView`; a `QTabWidget` hosts one view per tab. Toolbar `QAction`s drive the *active* view's back / forward / reload, and the address bar normalises whatever you type into either a URL or a Google search before loading it.
