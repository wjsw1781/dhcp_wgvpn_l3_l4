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
            if '\r' not in self.cache:
                return
            
            anvil.server.call("ssh_send", self.ssh_token,  self.cache)
            self.cache = ""
            
        self.term.onKey(_on_key)
        # 4. 启动轮询定时器
        # def _poll_once():
        #     if not self.ssh_token:
        #         return
        #     out = anvil.server.call("ssh_recv", self.ssh_token)
        #     if out:
        #         self.term.write(out)

        # # 在浏览器端开 setInterval，每 150 ms 调一次 _poll_once
        # self.poll_handle = anvil.js.window.setInterval(_poll_once, 150)    
        # # 5. 可写一行欢迎文字



    # 4. 启动异步轮询
        self.polling = True
        self._poll_once()          #

        self.term.write("xterm.js loaded, ssh connecting...\r\n")

# 单次轮询
    def _poll_once(self):
        if not (self.polling and self.ssh_token):
            return

        # 异步调用，不阻塞 UI；返回 Promise/Future
        future = anvil.server.call_s("ssh_recv", self.ssh_token)
    
        # on-done 回调
        def _after(out):
            if out:
                self.term.write(out)
            # 再过 150 ms 调下一次
            if self.polling:
                anvil.js.window.setTimeout(self._poll_once, 150)
    
        future.then(_after)


    
    # 表单关闭时断开 SSH
    def form_hide(self, **e):
        if self.ssh_token:
            anvil.server.call('ssh_close', self.ssh_token)
            self.ssh_token = None
