import pandas as pd
import os
import glob
import shutil
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from SOAP_converter import *
soap = SOAP_Converter()

class InfoProcessor:
    def __init__(self):
        self.year = 2023

    def create_initial_type(self, prompt):
        data = {
            'name': ["patient-1"], 
            'subjective': [soap.get_subjective(prompt)], 
            'objective': [soap.get_objective(prompt)]
        }
        return pd.DataFrame(data)
    
    def create_assessment(self, name, subjective, objective):
        data = {
            'name': ["patient-1"], 
            'subjective': [subjective], 
            'objective': [objective],
            'assessment': [soap.get_assessment(subjective, objective)], 
        }
        return pd.DataFrame(data)
    
    def create_plan(self, name, subjective, objective, assessment):
        data = {
            'name': ["patient-1"], 
            'subjective': [subjective], 
            'objective': [objective],
            'assessment': [assessment], 
            'Plan': [soap.get_plan(assessment)]
        }
        return pd.DataFrame(data)
    
    def save_file(self, df, file_path):
        # if not os.path.exists(file_path):
        #     os.makedirs(file_path)
        df.to_csv(file_path, index=False)