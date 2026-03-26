pyinstaller --onefile --hidden-import=numpy --hidden-import=parselmouth --icon icon.ico --noconsole --collect-all numpy --collect-all parselmouth chromatic_gen.py

with console if you want to see if there is errors:

pyinstaller --onefile --hidden-import=numpy --hidden-import=parselmouth --icon icon.ico --collect-all numpy --collect-all parselmouth chromatic_gen.py
