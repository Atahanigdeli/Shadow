@echo off
echo [InternetShortcut] > "%USERPROFILE%\Desktop\Uygulamayı Başlat.url"
echo URL=pythonw "%~dp0start_flask_app.py" >> "%USERPROFILE%\Desktop\Uygulamayı Başlat.url"
echo IconIndex=0 >> "%USERPROFILE%\Desktop\Uygulamayı Başlat.url"
echo IconFile=C:\Windows\System32\SHELL32.dll,15 >> "%USERPROFILE%\Desktop\Uygulamayı Başlat.url"

echo Kısayol oluşturuldu. Masaüstünden "Uygulamayı Başlat" simgesine çift tıklayın.
