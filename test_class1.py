import pandas as pd
import sys
import os
directory_path = os.getcwd()
sys.path.append(directory_path+'/digital_factor/digital_factor_base')
sys.path.append(directory_path+'/digital_factor')
from digital_factor.l_entity_digital_factor import lEntityDigitalFactor

df = pd.read_excel('resources/template_data.xlsx')
data = []
for index,row in df.iterrows():
    lEntityDigitalFactor_obj = lEntityDigitalFactor(
        buy_or_sale=row['نوع'],
        company_name=row['نام شرکت'],
        company_code=row['شماره اقتصادی'],
        province=row['استان'],
        city=row['شهر'],
        address = row['آدرس'],
        kala_name=row['نام کالا'],
        price=row['مبلغ'],
        maliat_arzesh_afzoodeh=row['مالیات ارزش افزوده'],
        avarez_arzesh_afzoodeh=row['عوارض ارزش افزوده']

    )
    print(lEntityDigitalFactor_obj.get_info())
    data.append(lEntityDigitalFactor_obj)
#TODO: configure the excel file to be used more conviniently
#TODO: double check the architecture of the software and ease of its use
print(data[1].get_info())