@echo off
setlocal EnableDelayedExpansion

REM -----------------------------
REM count_lines.bat <folder>
REM -----------------------------

if "%~1"=="" (
    echo Usage: count_lines.bat ^<folder^>
    exit /b 1
)

if not exist "%~1" (
    echo Error: Folder "%~1" does not exist.
    exit /b 1
)

set total=0

REM Recursively process all files
for /r "%~1" %%f in (*) do (
    for /f %%l in ('type "%%f" ^| find /c /v ""') do (
        set /a total+=%%l
    )
)

echo.
echo Total lines in "%~1": %total%
echo.

endlocal
