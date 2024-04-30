REM define permanent environment variables
setx HOME d:      
setx GITHUB_DIR d:\github
setx PYTHONPATH d:\github\xt_dilbert

REM try to find existing conda3 installation
set CONDA3_TMP=C:\Users\%USERNAME%\AppData\Local\anaconda3

if not exist %CONDA3_TMP%\ (
    set CONDA3_TMP=%HOME%\Users\%USERNAME%\AppData\Local\anaconda3
)

REM install mini-conda, if needed
if not exist %CONDA3_TMP%\ (
  REM curl not download file correctly; need to fix...
  echo installing mini-conda...
  curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o %TEMP%\miniconda.exe
  %TEMP%\miniconda.exe /S /AddToPath=1 /D=%CONDA3_TMP%
)

REM set CONDA3_DIR
setx CONDA3_DIR %CONDA3_TMP%

REM add ALIASES macro file (doskey) to start up commands
reg add "HKCU\Software\Microsoft\Command Processor" /v Autorun /d "doskey /macrofile=\"d:\github\repo_tools\windows\aliases.txt\"" /f

REM DOSKEY macros cannot be called from .bat files so copy rt.bat and xt.bat to a dir in the path
call copy %GITHUB_DIR%\repo_tools\windows\rt.bat %CONDA3_DIR%\scripts
call copy %GITHUB_DIR%\repo_tools\windows\xt.bat %CONDA3_DIR%\scripts

REM create github, .models, .data directories
mkdir %GITHUB_DIR%
mkdir %HOME%\.models
mkdir %HOME%\.data

REM install git, if needed
REM config git for our credentials

REM install VSCODE
REM curl -L https://code.visualstudio.com/docs/?dv=win64user -o %TEMP%\vscode.exe
REM %TEMP%\vscode.exe

REM install VSCODE extensions
