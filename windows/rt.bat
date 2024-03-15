@echo off
%CONDA3_DIR%\python %GITHUB_DIR%\repo_tools\repo\repo.py $* && call %GITHUB_DIR%\repo_commands.bat
