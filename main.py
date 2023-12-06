#!/usr/bin/env python3
import os
try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

except Exception as e:
    print(e)

from PySide6.QtWidgets import *
from views.mainWindowManager import mainWindow
import sys


def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()



    

