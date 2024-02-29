REM install ODBC 17 driver for XT
curl -L -o %TEMP%\ODBC17.msi https://go.microsoft.com/fwlink/?linkid=2249004
%TEMP%\ODBC17.msi 

REM install XT in xt_shared environment
call conda create -n xt_shared python=3.10
call conda activate xt_shared
call pip install xtlib==0.0.326
call conda deactivate

REM add the XT directory to the PATH (as last path entry)