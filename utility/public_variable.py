class PublicVariable(object):
    """
        全局变量、此变量一般用于前置方法传参或者存放返回值
        不建议修改，如若需要则需自定义新增即可
    """

    def __init__(self):
        self.host = ''              # 服务器IP地址
        self.username = ""          # 登陆用户名
        self.password = ""          # 登陆密码
        self.userdata = []

variable = PublicVariable()
