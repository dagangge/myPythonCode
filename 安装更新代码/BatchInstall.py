import os
libs={"beautifulsoup4","Django","ipython","jiaba","jupyter","matplotlib","notebook","numpy","paho-mqtt","pandas","pillow","protobuf","pyecharts","pyinstaller","pymssql","pyodbc","pyserial","requests","selenium","sqlacodegen","SQLAlchemy","watchdog","wordcloud",}
try:
    for x in libs:
        os.system("pip install "+x)
    print("Successful")
except :
    print("Failed Somehow")
