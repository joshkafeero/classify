import pandas as pd 
from config import Utilities 



feature_file = Utilities.features_file2
def features():
    data = pd.read_csv('final_data.csv')
    cols = list(data.columns)
    cols= cols[2:]
    return cols

def features2():
    with open(feature_file)as f:
        contents = f.readlines()
        contents =[i.replace('is_','') for i in contents ] #remove is_
        contents = [i.replace('has_','')for i in contents]#remove has_
        contents =[i.replace('city_','') for i in contents ] #remove city_
        contents = [i.replace('category_code_','')for i in contents]# remove category_code_
        contents = [i.replace('state_code_','')for i in contents]# remove state code
        # contents = cols
    return contents

