from ._anvil_designer import get_resource_by_userTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class get_resource_by_user(get_resource_by_userTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        while not anvil.users.get_user():
            anvil.users.login_with_form()

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        print(self.card_1.)
        pass


