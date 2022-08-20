from math import nan
from digital_factor_base import DigitalFactor
class lEntityDigitalFactor(DigitalFactor): 
    type_of_factor_owner =  "lEntityDigitalFactor"
    buy_or_sale = None #1 is for buy, 0 is for sale
    type_of_movadi =  1 # 1 = مشمول ثبتنام در نظام مالیاتی
    company_name =  None
    company_code = None #شماره اقتصادی
    province = None
    city = None
    address = None
    type_of_kala =   1  # سایر کالا ها
    kala_name = None
    type_of_trade = 1 #ریالی
    price = None#مبلغ کالا
    maliat_arzesh_afzoodeh = None
    avarez_arzesh_afzoodeh = None


    def __init__(self,**kwargs):
            for key,value in kwargs.items():
                if value is not nan :
                    if value is float :
                        self.__dict__[key] = int(value)
                    else :
                        self.__dict__[key] = value

    def fill_info(self, info: dict) :
        for data in info :
            if data in self.required_class_info :
                self.required_class_info[data] = info[data]
            else :
                print("Error: data not found in required_class_info")
                return False
    def get_info(self) :
        return self.__dict__
    