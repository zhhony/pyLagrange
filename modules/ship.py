from modules import *
import pandas


class Ship():
    def __init__(self, shipName) -> None:
        self.shipName = shipName

        self.shipData = ShipData()
        self.shipData.load()

    @property
    def shipID(self):
        return self.shipData.getValue(self.shipName, 'ship_id', 'ship_basic_inf')

    @property
    def shipType(self):
        return self.shipData.getValue(self.shipName, 'ship_type', 'ship_basic_inf')

    @property
    def commandValue(self):
        return self.shipData.getValue(self.shipName, 'command_value', 'ship_basic_inf')

    @property
    def commandValue(self):
        return self.shipData.getValue(self.shipName, 'command_value', 'ship_basic_inf')


class ShipData():
    '''ship_basic_inf 舰船基本信息 \nship_weapon_data 舰船武器信息 \ninf_ship_armoured_data 舰船装甲信息 \ndictionary 字典 \n'''

    pandas.set_option('display.unicode.east_asian_width', True)
    pandas.set_option('display.colheader_justify', 'right')

    def __init__(self) -> None:
        self.dataFile = './data/ship'

    def getTablesAll(self, tableName: str) -> list:
        '''载入指定表格'''
        with Conn(self.dataFile) as cur:
            sql = f'select * from main.{tableName}'
            cur.execute(sql)

            data = cur.fetchall()
            columns = [col[0] for col in cur.description]

            return pandas.DataFrame(data=data, columns=columns)

    def load(self):
        '''获取数据库存储的所有内容'''
        self.ship_basic_inf = self.getTablesAll('inf_ship_basic_information')
        self.ship_weapon_data = self.getTablesAll('inf_ship_weapon_data')
        self.ship_armoured_data = self.getTablesAll('inf_ship_armoured_data')

    def getValue(self, shipName, property, modules: str):
        if modules == 'ship_basic_inf':
            df = self.ship_basic_inf
            return df.loc[df.loc[:, 'ship_name'] == shipName, property][0]


class ShipWeapon():
    def __init__(self, shipID) -> None:
        self.shipID = shipID


s = Ship('阋神星一级')
s.shipType
s.commandValue
