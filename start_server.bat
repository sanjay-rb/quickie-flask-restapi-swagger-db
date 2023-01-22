CALL venv\Scripts\activate.bat
set FLASK_APP=%1
set FLASK_DEBUG=True
flask run --host=0.0.0.0