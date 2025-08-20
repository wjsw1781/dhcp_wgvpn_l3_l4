from ._anvil_designer import ItemTemplate5Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate5(ItemTemplate5Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.label_1.text = self.item['yewu_name']

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        # open_form('get_resource_by_user',self.item)
        # anvil.get_open_form('get_resource_by_user',self.item)
        anvil.open_form('get_resource_by_user',resource=self.item)

    def button_3_click(self, **event_args):
        """This method is called when the button is clicked"""
        rowId = self.item.get_id()
        anvil.server.call('delete_resource',rowId)
        self.remove_from_parent()

        pass


