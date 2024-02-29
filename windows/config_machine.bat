REM define permanent environment variables
setx HOME d:      
setx GITHUB_DIR d:\github
setx CONDA3_DIR C:\Users\rfernand\AppData\Local\anaconda3

REM add ALIASES macro file (doskey) to start up commands
reg add "HKCU\Software\Microsoft\Command Processor" /v Autorun /d "doskey /macrofile=\"d:\github\repo_tools\windows\aliases.txt\"" /f

REM create github, .models, .data directories
mkdir %GITHUB_DIR%
mkdir %HOME%\.models
mkdir %HOME%\.data

REM install git, if needed
REM config git for our credentials

REM install mini-conda, if needed
if not exist %CONDA3_DIR%\ (
  REM curl not download file correctly; need to fix...
  echo installing mini-conda...
  curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o %TEMP%\miniconda.exe
  %TEMP%\miniconda.exe /S /AddToPath=1 /D=%HOME%\miniconda
)

REM install VSCODE
REM curl -L https://code.visualstudio.com/docs/?dv=win64user -o %TEMP%\vscode.exe
REM %TEMP%\vscode.exe

REM install VSCODE extensions