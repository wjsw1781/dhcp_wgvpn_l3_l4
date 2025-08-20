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
        list_columns_all = app_tables.wg_vpn_node.list_columns()
        list_columns=[]

        # wg_id 逻辑由后端维护 前端只要安卓
        for item in list_columns_all:
            if item["name"] =="wg_id":
                continue
            list_columns.append(item)
            
        import json
        cols = [c["name"] for c in list_columns]
        header = ",".join(cols) + "\n"
        sample = []
        for c in list_columns:
            sample.append(json.dumps({"key": "value"}) if c["type"] == "simpleObject" else "")
        example_line = ",".join(sample) + "\n"
        csv_text = header + example_line
        blob = BlobMedia("text/csv", csv_text.encode("utf-8"),name="wg_vpn_node_template.csv")
        anvil.media.download(blob)

    def file_loader_1_change(self, file, **event_args):
        if not file:
            return
    
        try:
            # 把文件 Media 传到后端
            anvil.server.call('import_csv_to_wg_vpn_node', file)
        
            # 如果页面上有 DataGrid 已做 data-binding，刷新一下即可看到新数据
            self.refresh_data_bindings()
    
        except Exception as e:
            alert(e)
