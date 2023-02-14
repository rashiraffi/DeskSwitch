from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyvda import VirtualDesktop, get_virtual_desktops
import os
import sys

def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(True)

    # Adding an icon
    icon = QIcon("icon.png")

    # Adding item on the menu bar
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    menu = QMenu()

    vDesks = get_virtual_desktops()

    vDeskDict = {}

    # Creating the options
    for d in vDesks:
        print(d.name,":", d.number)
        option = QAction(d.name)
        option.triggered.connect(lambda checked, d=d: VirtualDesktop(d.number).go())
        # menu.addAction(option)
        vDeskDict[d.name] = option

    for k in vDeskDict:
        menu.addAction(vDeskDict[k])

    # To quit the app
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    # Adding options to the System Tray
    tray.setContextMenu(menu)
    tray.setToolTip('Click to show menu')
    tray.activated.connect(lambda reason: menu.exec_(QCursor.pos()))

    app.exec_()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        os.execv(sys.executable)