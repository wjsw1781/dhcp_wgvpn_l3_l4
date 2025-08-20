from ._anvil_designer import aaaTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class aaa(aaaTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.


    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('node_out')

    def link_2_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('get_resource_by_user')

    def link_3_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('my_resource_page')


