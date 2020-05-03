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

class send_cmd:
    def __init__(self):
        self.head1 = 0x55
        self.head2 = 0x55
        self.len1 = 0x00
        self.len2 = 0x00
        self.saddr = 0x01       # 对应c#中的ePtlAddr
        self.taddr = 0x00       # 对应c#中的ePtlAddr
        self.cmd1 = 0x62        # 对应的整体功能
        self.cmd2 = 0x01
        self.data = bytearray(512)
        self.sum = self.cal_sum()
        self.end1 = 0xAA
        self.end2 = 0xAA
        self.setting()

    def cal_sum(self):
        """
           此方法没有进行健壮性分析
           数据校验和
           :return:从数据长度（包括）开始到数据内容结束的所有数据相加取低8位
           """
        print(type(self.len2))
        sum = 0
        sum += self.len1
        sum += self.len2
        sum += self.saddr
        sum += self.taddr
        sum += self.cmd1
        sum += self.cmd2
        return bytes([sum])
    def setting(self):
        """
        进行整个的赋值操作
        :return:
        """

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

Hex_str = bytes.fromhex('55 55 00 00 01 00 62 01')
print(Hex_str)