# os module allows us to interact with the file paths on the computer.
import os
# I think this will help manipulate the cvs file to make it more readable.
import pandas as pd
from uuid import UUID

# The CVS file has the list of all the cadidates and their IDs. Built a class to get the names and IDs of the candidates. 
class ServerData():
    # This line initializes objects of the class when they're made. Makes the object but doesn't return anything.
    def __init__(self) -> None:
        # This line finds and reads the CVS file and stores it in a Pnadas dataframe assigned as the basic_data attribute in ServerData class.
        self.basic_data = pd.read_csv(os.path.join('data', 'candidate_basic.csv'))
    
    # This function takes in self and returns a string of the names and IDs of the candidates in the basic_data attribute in JSON records format.
    def get_name_id(self) -> str:
        return self.basic_data[['name', 'candidate_id']].to_json(orient='records')
    
    def get_candidate(self, candidate_id: int) -> tuple:
        """
        Return a dictionary of the candidate's data and a status code.
        For now we us
        """
        try:
            name = self.basic_data.loc[self.basic_data['candidate_id'] == candidate_id, 'name'].values[0]
        except:
            name = 'TEST NAME'
        return {
            'candidate_id': candidate_id,
            'name': name,
            'party': '', #Lots of party names
            # 'district': 1, #Necesarry?
            'state': 'Texas',
            'age': int,
            'incumbent': False, #?
            'traits':[
                {'title': 'Supports increasing taxes for the rich in order to reduce interest rates for student loans?', 'response': 'Response'},
                {'title': 'Opinion on the highest marginal tax rate?', 'response': 'Response'},
                {'title': 'Supports a wealth tax in order to pay for public programs?', 'response': 'Response'},
                {'title': 'Should the federal minimum wage be increased, and if so, to what level?', 'response': 'Response'},
                {'title': 'What steps would they take to ensure all Americans have access to quality and affordable health care, including reproductive care and prescription drug coverage?', 'response': 'Response'},
                {'title': 'Should the government regulate the prices of life-saving drugs?', 'response': 'Response'},
                {'title': 'Supports a government-run (e.g., single-payer) healthcare program, such as Medicare-for-All?', 'response': 'Response'},
                {'title': 'Stance on abortion, and do you support the Supreme Court\'s decision to overturn Roe v. Wade?', 'response': 'Response'},
                {'title': 'Should “gender identity” be added to anti-discrimination laws?', 'response': 'Response'},
                {'title': 'Should transgender athletes be allowed to compete against athletes that differ from their assigned sex at birth?', 'response': 'Response'},
                {'title': 'Supports President Biden\’s student loan forgiveness program and the forgiveness of federal student loan debt?', 'response': 'Response'},
                {'title': 'Should the federal government pay for tuition at four-year colleges and universities?', 'response': 'Response'},
                {'title': 'Should the government increase environmental regulations to prevent climate change?', 'response': 'Response'},
                {'title': 'Stance on the development of renewable energy (e.g., solar, wind, geo-thermal) and permits for drilling on public lands?', 'response': 'Response'},
                {'title': 'What steps would they take to create an accessible path to citizenship, including for Deferred Action for Childhood Arrivals (DACA) recipients?', 'response': 'Response'},
                {'title': 'How should the country handle undocumented immigrants currently in the U.S.?', 'response': 'Response'},
                {'title': 'Supports increasing security along the southern US border?', 'response': 'Response'},
                {'title': 'Stance on economic intervention as a means of resolving international conflicts?', 'response': 'Response'},
                {'title': 'How should the US handle its involvement in international conflicts such as the Russia-Ukraine war and the Israel-Palestine conflict?', 'response': 'Response'},
                {'title': 'Should there be more restrictions on the current process of purchasing a gun?', 'response': 'Response'},
                {'title': '26. Do they generally support gun-control legislation (e.g., red flag laws, boyfriend loopholes)?', 'response': 'Response'},
                {'title': 'What measures do they support to expand voter access and restore trust in our elections?', 'response': 'Response'},
                {'title': 'Supports requiring a government-issued identification in order to vote at the polls?', 'response': 'Response'},
                {'title': 'Should the government impose stricter regulations on the collection and use of personal data by companies and increase regulations on social media companies (e.g., TikTok, Facebook)?', 'response': 'Response'},
                ],
        }, 200
    
            # 'rich_pay_students' : [''], # List of strings?
            # 'marginal_tax' : [''],
            # 'wealth_tax_public_programs' : [''],
            # 'fed_min_wage' : [''],
            # 'healthcare_access' : [''],
            # 'drug_price' : [''],
            # 'gov_healthcare_programs' : [''],
            # 'abortion': [''],
            # 'gender_anti-discrimination' : [''],
            # 'trans_athletes' : [''],
            # 'LGBTQ_rights' : [''],
            # 'forgive_student_loans' : [''],
            # 'gov_pay_tuition' : [''],
            # 'climate_change' : [''],
            # 'renewable_energy' : [''],
            # 'citizenship' : [''],
            # 'illegial_residents' : [''],
            # 'southern_border' : [''],
            # 'economic_international_intervention' : [''],
            # 'involve_international_conflicts' : [''],
            # 'restrict_gun_purchase' : [''],
            # 'gun_control' : [''],
            # 'voter_access' : [''],
            # 'voter_id' : [''],
            # 'social_media' : [''],
            # }, 200