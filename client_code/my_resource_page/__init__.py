from ._anvil_designer import my_resource_pageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class my_resource_page(my_resource_pageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def repeating_panel_1_show(self, **event_args):
        """This method is called when the repeating panel is shown on the screen"""
    
        me = anvil.users.get_user()

        data = anvil.server.call('show_resource', me)
        print(data)
        self.repeating_panel_1.items = data

    def data_row_panel_1_show(self, **event_args):
        """This method is called when the data row panel is shown on the screen"""

        me = anvil.users.get_user()
        data = anvil.server.call('show_resource', me)
        print(data)
        self.data_row_panel_1.items = data
        
