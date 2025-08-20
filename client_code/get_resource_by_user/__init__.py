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
    def __init__(self, resource=None,**properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        while not anvil.users.get_user():
            anvil.users.login_with_form()
            
        if not resource:
            self.rowId.text = None
            return
        
        self.text_box_1.text = resource['yewu_name']
        self.date_picker_1.date = resource['yewu_start_time']
        self.date_picker_2.date = resource['yewu_end_time']
        self.text_box_2.text = resource['yewu_need_proxy_num']
        self.rowId.text = resource.get_id()

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        user = anvil.users.get_user()
        form={
            "yewu_name":self.text_box_1.text,
            "yewu_start_time":self.date_picker_1.date,
            "yewu_end_time":self.date_picker_1.date,
            "yewu_need_proxy_num":self.text_box_2.text,
            "rowId":self.rowId.text,
            "user":user
        }
        anvil.server.call("get_resource_by_user",form)
        open_form('my_resource_page')
        pass

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('my_resource_page')

    def card_1_show(self, **event_args):
        """This method is called when the column panel is shown on the screen"""
        pass



