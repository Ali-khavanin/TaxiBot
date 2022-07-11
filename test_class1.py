import pandas as pd
import sys
import os
directory_path = os.getcwd()
sys.path.append(directory_path+'/digital_factor/digital_factor_base')
sys.path.append(directory_path+'/digital_factor')
from digital_factor.l_entity_digital_factor import lEntityDigitalFactor

excel_df = pd.read_excel('digital_factor/digital_factor_base/test_data.xlsx')

data = []
#TODO: configure the excel file to be used more conviniently
#TODO: double check the architecture of the software and ease of its use
for index,row in excel_df.iterrows():
    l_entity = lEntityDigitalFactor()
    l_entity.fill_info(
        {
            
        }
    )