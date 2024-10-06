@echo off

if exist "myenv\Scripts\activate.bat" (
    call myenv\Scripts\activate.bat
    echo Virtual environment activated.
) else (
    echo Virtual environment not found.
)

