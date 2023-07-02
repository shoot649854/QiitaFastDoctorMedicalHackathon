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
    soap = SOAP_Converter()

    subjective = soap.get_subjective(prompt)
    print("CREATE: soap.get_subjective(prompt) ")
    objective = soap.get_objective(prompt)
    print("CREATE: soap.get_objective(prompt) ")

    assessment = soap.get_assessment(subjective, objective)
    print("CREATE: soap.get_assessment(subjective, objective) ")

    info.save_file(info.create_plan("patient-1", 
                                    subjective, 
                                    objective,
                                    assessment),
                                    file_path)
    print("CREATE: info.create_plan() ")

main()