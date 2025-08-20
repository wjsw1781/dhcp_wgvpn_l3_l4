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

        self.term = None          # xterm 实例
        self.poll_timer.interval = 0     # 先关闭定时器

    # 点击“打开终端”
    def btn_open_click(self, **e):
        # 1. 等 <script> 标签全部加载
        anvil.js.wait_until_loaded()

        # 2. 拿到全局构造函数
        Terminal      = anvil.js.window.Terminal
        FitAddonClass = anvil.js.window.FitAddon

        # 3. 创建终端并挂到 panel
        self.term = Terminal.new()
        fit = FitAddonClass.new()
        self.term.loadAddon(fit)
        self.term.open(self.terminal_panel.dom_node)
        fit.fit()

        # 4. 绑定 xterm 的键盘事件 → 发到后端
        def on_data(data):
            anvil.server.call('ssh_send', data)  # 单次写入即可，xterm 已做缓冲
        self.term.onData(on_data)

        # 5. 启动服务器端 SSH 会话
        anvil.server.call('ssh_start', 'your_host', 'user', 'password')

        # 6. 开启轮询定时器，实时取回输出
        self.poll_timer.interval = 0.15   # 150 ms 一次

    # Timer 组件，每 0.15 s 拉一次数据
    def poll_timer_tick(self, **e):
        out = anvil.server.call('ssh_recv')
        if out:
            self.term.write(out)

    # 可选：表单关闭时断开
    def form_hide(self, **e):
        self.poll_timer.interval = 0
        anvil.server.call('ssh_close')
