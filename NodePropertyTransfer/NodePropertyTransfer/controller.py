# -*- coding: utf-8 -*-

import functools

import sd

from . import app
from . import view


class Controller(object):
    def __init__(self):
        self.__ui = view.View()
        self.current_node_parameter = None
        self.setup_event()

    def setup_event(self):
        self.__ui.gui.get_node.clicked.connect(functools.partial(self.clicked_get_node_button))
        self.__ui.gui.set_node.clicked.connect(functools.partial(self.clicked_set_node_button))

    def clicked_get_node_button(self):
        node_list = app.NodePropertiesCopy.get_selection_node()

        self.current_node_parameter = app.NodePropertiesCopy(node_list[0])
        self.update_text()

    def clicked_set_node_button(self):
        node_list = app.NodePropertiesCopy.get_selection_node()

        for node in node_list:
            self.current_node_parameter.transfer_property_value(node)

    def update_text(self):
        message = self.current_node_parameter.get_current_node_info()
        self.__ui.gui.current_node_detail.setPlainText(message)

    def sho_gui(self):
        self.__ui.show()
