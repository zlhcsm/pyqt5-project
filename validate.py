
def adc_range(val):
   """
   生成符合ADC范围的值，1000 <= val <= 2000
   :param val:
   :return:
   """
   return min(2000, max(1000, val))


