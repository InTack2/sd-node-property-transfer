import sd

from PySide2 import QtWidgets

from . import controller

MENU_NAME = "TackTools.menu"
TOOL_NAME = "NodePropertyTransfer"


def initializeSDPlugin():
    print("NodePropertyTransfer initializeSDPlugin")
    create_menu()


def uninitializeSDPlugin():
    print("NodePropertyTransfer uninitializeSDPlugin")
    delete_menu()


def _exec():
    _controller = controller.Controller()
    _controller.sho_gui()


def create_menu():
    context = sd.getContext()
    app = context.getSDApplication()
    ui_manager = app.getQtForPythonUIMgr()

    tool_menu = ui_manager.findMenuFromObjectName(MENU_NAME)

    if not tool_menu:
        tool_menu = ui_manager.newMenu(menuTitle="TackTools", objectName=MENU_NAME)

    act = QtWidgets.QAction(TOOL_NAME, tool_menu)
    act.triggered.connect(_exec)
    tool_menu.addAction(act)


def delete_menu():
    context = sd.getContext()
    app = context.getSDApplication()
    ui_manager = app.getQtForPythonUIMgr()

    tool_menu = ui_manager.findMenuFromObjectName(MENU_NAME)

    for action in tool_menu.actions():
        if action.text() == TOOL_NAME:
            tool_menu.removeAction(action)

    if tool_menu.actions() == []:
        ui_manager.deleteMenu(MENU_NAME)
