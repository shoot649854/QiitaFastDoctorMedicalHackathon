import os
import openai
from InfoProcessor import *

# os.environ['YOUR_ORG_ID'] = 'org-oiM21elw8g8djxaJXJPJj2rT'
# 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
os.environ['OPENAI_API_KEY'] = 'API KEY'
openai.api_key = os.environ['OPENAI_API_KEY']
openai.Model.list()

txt = open('./text/patient-1.txt', 'r')
prompt = txt.read()

class SOAP_Converter:
    def __init__(self) -> None:
        pass

    def get_subjective(self, prompt):
        prompt = """
Subjective information in medical records includes patient's physical findings, 
test results, and various examinations like auscultation, palpation, and imaging tests:
        
""" 

        prompt = "find subjective information within 30 words:" + prompt
        res = openai.Completion.create(
            model = "text-davinci-003",
            prompt = prompt,
            max_tokens = 2048,
            temperature = 0
        )
        return res.choices[0].text
    
    def get_objective(self, prompt):
        prompt = """
Objective assessment should include the process of reaching a diagnosis, providing a clear understanding and potential 
basis for appeal in case of medical malpractice accusations:
"""
        prompt = "find Objective information within 30 words:" + prompt
        res = openai.Completion.create(
            model = "text-davinci-003",
            prompt = prompt,
            max_tokens = 2048,
            temperature = 0
        )
        return res.choices[0].text
    
    def get_assessment(self, subjective, objective):
        prompt = """
Objective information in medical records includes physical findings, test results, 
and diagnostic procedures like auscultation, palpation, visual examination, blood tests, and imaging tests.
        
subjective: """ + str(subjective) + """

objective: """ + str(objective)
        prompt = "find Assessment within 30 words:"
        res = openai.Completion.create(
            model = "text-davinci-003",
            prompt = prompt,
            max_tokens = 2048,
            temperature = 0
        )
        return res.choices[0].text
    
    def get_plan(self, assessment):
        prompt = "find how to plan treatment for this patient based on assessment:" + str(assessment)
        res = openai.Completion.create(
            model = "text-davinci-003",
            prompt = prompt,
            max_tokens = 2048,
            temperature = 0
        )
        return res.choices[0].text

