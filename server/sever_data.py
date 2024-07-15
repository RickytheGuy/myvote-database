# os module allows us to interact with the file paths on the computer.
import os
# I think this will help manipulate the cvs file to make it more readable.
import pandas as pd

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
            'party': 'Republican',
            'state': 'Texas',
            'district': 1,
            'age': 45,
            'sex': 'M',  
            'incumbent': False,
            'abortion': 'Pro-life', # Is it a string?
            'gun_control': 2, # Scale of 1-5?
            'foregin_policy': '',
            'rich_pay_students' : [''], # List of strings?
            'rich_pay_students' : [''],
            'rich_pay_students' : [''],
            'rich_pay_students' : [''],
            'rich_pay_students' : [''],
            'rich_pay_students' : [''],
            'rich_pay_students' : [''],
            'rich_pay_students' : [''],
            'rich_pay_students' : [''],
            'rich_pay_students' : [''],
        }, 200