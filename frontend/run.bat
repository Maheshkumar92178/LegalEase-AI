@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 (
    echo Python was not found. Install Python or add it to PATH.
    pause
    exit /b 1
)

start "" /b powershell.exe -NoProfile -WindowStyle Hidden -Command ^
 "$url='http://127.0.0.1:8501'; $ready=$false; for($i=0;$i -lt 60;$i++){ $c=New-Object Net.Sockets.TcpClient; try{$c.Connect('127.0.0.1',8501);$c.Close();$ready=$true;break}catch{Start-Sleep -Milliseconds 500} }; if(-not $ready){exit}; $chrome=(Get-Command chrome.exe -ErrorAction SilentlyContinue).Source; if(-not $chrome){$paths=@('$env:ProgramFiles\Google\Chrome\Application\chrome.exe','$env:ProgramFiles(x86)\Google\Chrome\Application\chrome.exe',\"$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe\"); foreach($p in $paths){$p=[Environment]::ExpandEnvironmentVariables($p);if(Test-Path $p){$chrome=$p;break}}}; if($chrome){Start-Process -FilePath $chrome -ArgumentList $url}"

python -m streamlit run frontend/app.py --server.address 127.0.0.1 --server.port 8501

pause