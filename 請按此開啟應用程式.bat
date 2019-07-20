@ECHO OFF
SET BINDIR=%~dp0
CD /D "%BINDIR%"
:start
cls
@echo 程式啟動中...
".\Portable python-3.7.3 x64\App\Python\"python UI.py
@echo 程式已結束 現在可按視窗右上角的 X 關閉程式 否則將於10秒後自動重新啟動
@ping 127.0.0.1 -n 10 -w 100 > nul
goto start