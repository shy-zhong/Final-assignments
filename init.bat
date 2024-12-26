@echo off
echo 正在检查Python 3是否已安装...
python -V | findstr /R "^Python 3\." >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3未安装，请先安装Python 3及以上版本后再运行此脚本。
    pause
    exit /b 1
)
echo Python 3已安装，正在创建虚拟环境...
python -m venv venv
echo 虚拟环境已创建，正在激活虚拟环境并安装requirements.txt中的包...
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo 包安装完成，再次激活虚拟环境...
call venv\Scripts\activate.bat
echo 虚拟环境已激活，正在运行入口程序mainwindow.py...
python -u mainwindow.py
echo 程序运行完毕。
pause