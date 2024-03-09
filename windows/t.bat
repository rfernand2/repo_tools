REM define permanent environment variables
setx HOME d:      
setx GITHUB_DIR d:\github

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

