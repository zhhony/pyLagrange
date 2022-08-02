import json


class Conf():
    '''获取配置文件内存储的所有内容'''

    def __init__(self) -> None:
        self.confFile = './config/conf'

    def load(self):
        with open(self.confFile) as f:
            self.conf = json.load(f)
