REM install git, if needed
REM config git for our credentials

REM install mini-conda, if needed
IF "%CONDA_PYTHON_EXE%"!="" GOTO :SKIP_MINICONDA
curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o %TEMP%\miniconda.exe
%TEMP%\miniconda.exe /S /AddToPath=1 /D=%HOME%\miniconda

:SKIP_MINICONDA
REM create github, .models, .data directories
mkdir %HOME%\github
mkdir %HOME%\.models
mkdir %HOME%\.data

REM install VSCODE
curl -L https://code.visualstudio.com/docs/?dv=win64user -o %TEMP%\vscode.exe
%TEMP%\vscode.exe

REM install VSCODE extensions

