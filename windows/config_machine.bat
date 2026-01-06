REM sesion-only environment variables
if exist D:\ (
    set HOME=D:
) else (
    set HOME=%HOME%
)

REM try to find existing conda3 installation
set CONDA3_DIR=%HOME%\Users\%USERNAME%\AppData\Local\anaconda3

REM define permanent environment variables
setx HOME %HOME% 
setx DATAROOT %HOME%\.data
setx GITHUB_DIR %HOME%\github
setx PYTHONPATH %HOME%\github\xt_dilbert

REM install mini-conda, if needed
if not exist %CONDA3_DIR%\ (
  REM curl not download file correctly; need to fix...
  ECHO downloading mini-conda...
  curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o %TEMP%\miniconda.exe
  ECHO installing mini-conda
  rd /s /q %CONDA3_DIR%
  %TEMP%\miniconda.exe /InstallationType=JustMe /RegisterPython=0 /S /AddToPath=1 /D=%CONDA3_DIR%      
  
)

REM set CONDA3_DIR
setx CONDA3_DIR %CONDA3_DIR%

REM ensure yaml is installed 
pip install pyyaml

REM add ALIASES macro file (doskey) to start up commands
reg add "HKCU\Software\Microsoft\Command Processor" /v Autorun /d "doskey /macrofile=\"%HOME%\github\repo_tools\windows\aliases.txt\"" /f

REM DOSKEY macros cannot be called from .bat files so copy rt.bat to a dir in the path
call copy %GITHUB_DIR%\repo_tools\windows\rt.bat %CONDA3_DIR%\scripts

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
