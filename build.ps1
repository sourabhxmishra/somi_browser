# Build the Somi Browser desktop app (folder build — reliable for QtWebEngine).
# Prereqs (once):  py -3.12 -m venv .venv ; .\.venv\Scripts\Activate.ps1 ; pip install -r requirements.txt pyinstaller
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

python -m PyInstaller --noconfirm --clean --windowed `
  --name "SomiBrowser" `
  --icon "assets/icon.ico" `
  --add-data "home.html;." `
  --add-data "assets/icon.png;assets" `
  --add-data "assets/icon.ico;assets" `
  app.py

Write-Host "`nBuilt: $(Join-Path $PSScriptRoot 'dist\SomiBrowser\SomiBrowser.exe')" -ForegroundColor Green
