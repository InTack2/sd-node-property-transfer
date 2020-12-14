import sd
from sd.api.sdproperty import SDPropertyCategory
from sd.api.sdvalueserializer import SDValueSerializer


class NodePropertiesCopy(object):
    CATEGORIES = [
        SDPropertyCategory.Annotation,
        SDPropertyCategory.Input,
        SDPropertyCategory.Output
    ]

    def __init__(self, node):
        self.node = node
        self.definition = node.getDefinition()
        self.node_name = self.definition.getLabel()
        self.property_value_dict = self.create_node_property_and_value()

    def create_node_property_and_value(self):
        """Generate the property of a node and its value.
        """
        properties_dict = {}
        for category in self.CATEGORIES:
            property_list = self.definition.getProperties(category)

            for property in property_list:
                properties_dict[property.getLabel()] = [property, self.node.getPropertyValue(property)]

        return properties_dict

    def transfer_property_value(self, node):
        """Transfer property values.

        Args:
            node (sd.api.sdnode.SDNode): Selected Node.
        """
        definition = node.getDefinition()
        name = definition.getLabel()

        if self.node_name == name:
            for key, value in self.property_value_dict.items():

                if value[1] is None:
                    continue

                if value[0].isFunctionOnly() or value[0].isReadOnly():
                    continue

                node.setPropertyValue(value[0], value[1])

    def get_current_node_info(self):
        """Get information about the selected node.

        Returns:
            string: Text for display.
        """
        info_message = "Node Name : {}\n".format(self.node_name)

        for key, value in self.property_value_dict.items():
            if value[1] is None:
                continue

            if value[0].isFunctionOnly() or value[0].isReadOnly():
                continue

            value = self.node.getPropertyValue(value[0])
            info_message += "{} : {}\n".format(key, SDValueSerializer.sToString(value))

        return info_message

    @classmethod
    def get_selection_node(cls):
        context = sd.getContext()
        sd_app = context.getSDApplication()
        ui_manager = sd_app.getQtForPythonUIMgr()

        node_list = ui_manager.getCurrentGraphSelection()
        return node_list
