import os
import webbrowser
import subprocess
import sys

def start_flask_app():
    # Flask uygulamasını başlat
    flask_process = subprocess.Popen(
        [sys.executable, 'app.py'],
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    
    # Tarayıcıyı aç
    webbrowser.open('http://localhost:5000')
    
    # Uygulama kapanana kadar bekle
    try:
        flask_process.wait()
    except KeyboardInterrupt:
        flask_process.terminate()

if __name__ == '__main__':
    start_flask_app()
