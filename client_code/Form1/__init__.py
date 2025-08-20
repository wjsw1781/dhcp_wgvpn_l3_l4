from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


import anvil.js

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.Terminal = anvil.js.window.Terminal
        self.ssh_token = None          # 用来保存后端返回的 token
        self.cache = ""
        self.term = None          # xterm 实例
        self.poll_timer={"interval" : 0}     # 先关闭定时器
    
    # 点击“打开终端”
    def btn_open_click(self, **e):
        if self.ssh_token:          # 已经打开过就不再重复
            return
    
        # 1. 创建终端并装载到 panel
        self.term = self.Terminal()
    
        div = anvil.js.get_dom_node(self.terminal_panel)
        self.term.open(div)
        self.term.focus()
    
        # 2. 启动服务器端 SSH 会话，拿到 token
        self.ssh_token = anvil.server.call(
            'ssh_start', '10.244.5.254', 'root', '9293'
        )
    
        # 3. 绑定键盘事件（拿到 token 以后再绑定）
        def _on_key(ev, *_):
            key = ev.key
            self.cache += key
            if '\r\n' not 
            anvil.server.call("ssh_send", self.ssh_token, key)
    
        self.term.onKey(_on_key)
        # 4. 启动轮询定时器
        self.poll_timer['interval'] = 0.15   # 150 ms
    
        # 5. 可写一行欢迎文字
        self.term.write("xterm.js loaded, ssh connecting...\r\n")
    
    # Timer 周期拉取服务器输出
    def poll_timer_tick(self, **e):
        if not self.ssh_token:
            return
        out = anvil.server.call('ssh_recv', self.ssh_token)
        if out:
            self.term.write(out)
    
    # 表单关闭时断开 SSH
    def form_hide(self, **e):
        if self.ssh_token:
            anvil.server.call('ssh_close', self.ssh_token)
            self.ssh_token = None
        self.poll_timer.interval = 0