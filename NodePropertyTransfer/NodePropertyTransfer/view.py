# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QDialog
import sd

from .ui import NodePropertyTransferUI


class View(QDialog):
    def __init__(self, *args, **kwargs):
        app = sd.getContext().getSDApplication()
        uiMgr = app.getQtForPythonUIMgr()
        super(View, self).__init__(parent=uiMgr.getMainWindow(), *args, **kwargs)

        self.gui = NodePropertyTransferUI.Ui_Dialog()
        self.gui.setupUi(self)
