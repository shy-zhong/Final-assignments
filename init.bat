@echo off
echo ���ڼ��Python 3�Ƿ��Ѱ�װ...
python -V | findstr /R "^Python 3\." >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3δ��װ�����Ȱ�װPython 3�����ϰ汾�������д˽ű���
    pause
    exit /b 1
)
echo Python 3�Ѱ�װ�����ڴ������⻷��...
python -m venv venv
echo ���⻷���Ѵ��������ڼ������⻷������װrequirements.txt�еİ�...
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo ����װ��ɣ��ٴμ������⻷��...
call venv\Scripts\activate.bat
echo ���⻷���Ѽ������������ڳ���mainwindow.py...
python -u mainwindow.py
echo ����������ϡ�
pause