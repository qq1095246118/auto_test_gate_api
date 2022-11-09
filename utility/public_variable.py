class PublicVariable(object):
    """
        全局变量
    """

    def __init__(self):
        self.host = ''              # 服务器IP地址
        self.username = ""          # 登陆用户名
        self.password = ""          # 登陆密码
        self. global_dict = {}      # dict全局变量


variable = PublicVariable()
