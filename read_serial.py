# coding:utf-8
import serial
import serial.tools.list_ports

cmd1_config = 0x62      # 配置CMD1的信息，表示TOCO配置信息

class TocoCmd2Config:
    """
    定义了一个CMD2的配置，里边主要是相对应功能的十六进制表示
    """
    def __init__(self):
        self.DAC = 0x01         # 查询、设置DAC值
        self.Cal = 0x02         # 查询、设置ADC校准值 250克变化的ADC值
        self.Base = 0x03        # 查询、设置TOCO基线值
        self.Gain = 0x04        # 查询、设置增益值
        self.ADC = 0x05         # 查询当前ADC值
        self.TOCO = 0x06        # 查询当前TOCO值
        self.Zero = 0x07        # 宫压调零
        self.Sample = 0x08      # 采样数据上传
        self.Demo = 0x09        # 工程模式

class PltConst:
    def __init__(self):
        self.pltCmdHead = 0x55  # 协议头数值
        self.pltCmdEnd = 0xAA   # 协议尾数值
        # self.

class PltCmd:
    def __init__(self):
        self.head1 = 0x22

class Ser(object):
    def __init__(self):
        # 打开端口
        self.port = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=2)

    # 发送指令的完整流程
    def send_cmd(self, cmd):
        self.port.write(cmd)
        response = self.port.readall()
        response = self.convert_hex(response)
        return response

    # 转成16进制的函数
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        print(result)
        return result

to = TocoCmd2Config()
print(to)
