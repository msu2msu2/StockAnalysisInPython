import pandas as pd

krx_list = pd.read_html('상장법인목록.xls')
print(krx_list)
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06}'.format)

print(krx_list[0])
print(len(krx_list))


