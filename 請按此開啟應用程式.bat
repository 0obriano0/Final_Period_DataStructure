@ECHO OFF
SET BINDIR=%~dp0
CD /D "%BINDIR%"
:start
cls
@echo �{���Ұʤ�...
".\Portable python-3.7.3 x64\App\Python\"python UI.py
@echo �{���w���� �{�b�i�������k�W���� X �����{�� �_�h�N��10���۰ʭ��s�Ұ�
@ping 127.0.0.1 -n 10 -w 100 > nul
goto start