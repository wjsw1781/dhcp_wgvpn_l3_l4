from ._anvil_designer import node_outTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class node_out(node_outTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""

        print(app_tables.wg_vpn_node.list_columns())
        data = (
            "wg_host,wg_port,wg_id,wg_account,wg_password,wg_ex_json\n"
            "1.1.1.1,51820,1,test_user,123456,{\"dns\":\"8.8.8.8\"}\n"
        ).encode('utf-8')
        return BlobMedia("text/csv", data, name="wg_vpn_node_template.csv")

