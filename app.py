"""Somi Browser — a lightweight tabbed desktop web browser built with PyQt5.

Features:
  • multiple tabs (new / close / reorder)
  • a smart address bar — type a URL, a bare domain, or a Google search
  • back / forward / reload / home navigation
  • per-tab titles taken from the page

Run:  python app.py        (needs PyQt5 + PyQtWebEngine — see requirements.txt)
"""
import os
import sys
from urllib.parse import quote

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLineEdit,
    QMainWindow,
    QTabWidget,
    QToolBar,
)


def resource(name):
    """Find a bundled asset whether running from source or a PyInstaller .exe."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


ICON = resource(os.path.join("assets", "icon.ico"))
HOME_URL = QUrl.fromLocalFile(resource("home.html")).toString()


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Somi Browser")
        self.setWindowIcon(QIcon(ICON))

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.sync_url_bar)
        self.setCentralWidget(self.tabs)

        nav = QToolBar("Navigation")
        self.addToolBar(nav)
        for label, tip, handler in [
            ("◀", "Back", lambda: self.current().back()),
            ("▶", "Forward", lambda: self.current().forward()),
            ("⟳", "Reload", lambda: self.current().reload()),
            ("⌂", "Home", self.go_home),
        ]:
            action = QAction(label, self)
            action.setToolTip(tip)
            action.triggered.connect(handler)
            nav.addAction(action)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Search Google or type a URL")
        self.url_bar.returnPressed.connect(self.navigate)
        nav.addWidget(self.url_bar)

        new_tab = QAction("＋", self)
        new_tab.setToolTip("New tab")
        new_tab.triggered.connect(lambda: self.add_tab())
        nav.addAction(new_tab)

        self.add_tab(HOME_URL)

    # ---- tabs -------------------------------------------------------------
    def add_tab(self, url=HOME_URL):
        view = QWebEngineView()
        view.setUrl(QUrl(url))
        index = self.tabs.addTab(view, "New Tab")
        self.tabs.setCurrentIndex(index)
        view.urlChanged.connect(lambda q, v=view: self._on_url(q, v))
        view.titleChanged.connect(lambda t, v=view: self._on_title(t, v))
        return view

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.current().setUrl(QUrl(HOME_URL))

    def current(self) -> QWebEngineView:
        return self.tabs.currentWidget()

    # ---- navigation -------------------------------------------------------
    def go_home(self):
        self.current().setUrl(QUrl(HOME_URL))

    def navigate(self):
        text = self.url_bar.text().strip()
        if text:
            self.current().setUrl(QUrl(self.to_url(text)))

    @staticmethod
    def to_url(text: str) -> str:
        if text.startswith(("http://", "https://")):
            return text
        if " " not in text and "." in text:      # looks like a domain
            return "https://" + text
        return "https://www.google.com/search?q=" + quote(text)

    # ---- keep the UI in sync with the active tab --------------------------
    def sync_url_bar(self, _index):
        view = self.current()
        if view is not None:
            self._show_url(view.url().toString())

    def _show_url(self, url):
        self.url_bar.setText("" if url == HOME_URL else url)
        self.url_bar.setCursorPosition(0)

    def _on_url(self, q, view):
        if view is self.current():
            self._show_url(q.toString())

    def _on_title(self, title, view):
        index = self.tabs.indexOf(view)
        if index != -1:
            self.tabs.setTabText(index, (title[:18] + "…") if len(title) > 18 else (title or "New Tab"))
        if view is self.current() and title:
            self.setWindowTitle(f"{title} — Somi Browser")


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Somi Browser")
    app.setWindowIcon(QIcon(ICON))
    window = Browser()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
