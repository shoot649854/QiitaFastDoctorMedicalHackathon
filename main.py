import os
import openai
import pandas as pd
from InfoProcessor import *
from SOAP_converter import *

def main():
    file_path = "./SOAP/"
    file_path = file_path + "2023-category.csv"
    # soap = SOAP_Converter()
    info = InfoProcessor()

    dataframe = pd.read_csv(file_path)
    dataframe = info.create_initial_type(prompt)
    print("CREATE: info.save_file(info.create_initial_type(prompt) ")

    dataframe = info.create_assessment(dataframe['name'], 
                                        dataframe['subjective'],
                                        dataframe['objective'])
    print("CREATE: info.create_assessment() ")
    
    info.save_file(info.create_plan(dataframe['name'], 
                                    dataframe['subjective'],
                                    dataframe['objective'],
                                    dataframe['assessment']),
                                    file_path)
    print("CREATE: info.create_plan() ")

main()