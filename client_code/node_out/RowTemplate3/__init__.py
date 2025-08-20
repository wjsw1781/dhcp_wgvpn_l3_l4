from ._anvil_designer import RowTemplate3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...ssh import ssh


class RowTemplate3(RowTemplate3Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        anvil.server.call('del_wg_vpn_node',self.item)
        self.remove_from_parent()
        pass

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        popup = ssh()                     # 实例化要弹出的表单
        anvil.alert(popup,                # 显示为弹窗
                    large=True,           # True/False 控制大小
                    title="SSH 设置",      # 弹窗标题（可选）
                    buttons=[])   


