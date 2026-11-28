# cutie-pie-pinyin
Qt UI wrapped around the existing `pinyin-tone-converter`.

## Run

Install the dependencies and launch the desktop app:

```powershell
python -m pip install -r requirements.txt
python main.py
```

Enter numbered pinyin and press Enter to convert it. The result is selectable
in the output field; use **Copy** to copy it to the clipboard.

## Create executable
With console window for debugging:
```
python -m PyInstaller --onefile main.py
```

Without console window, simply add `--windowed`:
```
python -m PyInstaller --onefile --windowed main.py
```
