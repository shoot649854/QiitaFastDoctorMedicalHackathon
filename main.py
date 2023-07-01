import os
import openai
import pandas as pd
from InfoProcessor import *
from SOAP_converter import *
file_path = "./SOAP/"

def main():
    soap = SOAP_Converter()
    print(soap.get_objective(prompt))
    print("GET: soap.get_objective() ")

    info = InfoProcessor()
    info.save_file(info.create_initial_type(prompt), file_path)
    print("CREATE: info.save_file(info.create_initial_type(prompt) ")

    file_path = file_path + "2023-category.csv"
    dataframe = pd.read_csv(file_path)
    print(dataframe.head())

main()