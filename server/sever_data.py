# os module allows us to interact with the file paths on the computer.
import os
# I think this will help manipulate the cvs file to make it more readable.
import pandas as pd
from uuid import UUID # Do we need this?

# The CVS file has the list of all the cadidates and their IDs. Built a class to get the names and IDs of the candidates. 
class ServerData():
    # This line initializes objects of the class when they're made. Makes the object but doesn't return anything.
    def __init__(self) -> None:
        # This line finds and reads the CVS file and stores it in a Pnadas dataframe assigned as the basic_data attribute in ServerData class.
        self.basic_data = pd.read_csv(os.path.join('data', 'candidate_basic.csv'))
    
    # This function takes in self and returns a string of the names and IDs of the candidates in the basic_data attribute in JSON records format.
    def get_name_id(self) -> str:
        return self.basic_data[['name', 'candidate_id']].to_json(orient='records')
    
    trait_data = {
        "Economy and Taxes": [ 
            {'question': 'Supports increasing taxes for the rich in order to reduce interest rates for student loans?', 'response': 'Response'},
            {'question': 'Opinion on the highest marginal tax rate?', 'response': 'Response'},
            {'question': 'Supports a wealth tax in order to pay for public programs?', 'response': 'Response'},
            {'question': 'Should the federal minimum wage be increased, and if so, to what level?', 'response': 'Response'},
        ],
        "Education": [
            {'question': 'Supports President Biden\’s student loan forgiveness program and the forgiveness of federal student loan debt?', 'response': 'Response'},
            {'question': 'Should the federal government pay for tuition at four-year colleges and universities?', 'response': 'Response'},
        ],
        "Environment and Energy": [
            {'question': 'Should the government increase environmental regulations to prevent climate change?', 'response': 'Response'},
            {'question': 'Stance on the development of renewable energy (e.g., solar, wind, geo-thermal) and permits for drilling on public lands?', 'response': 'Response'},
        ],
        "Foreign Policy": [
            {'question': 'Stance on economic intervention as a means of resolving international conflicts?', 'response': 'Response'},
            {'question': 'How should the US handle its involvement in international conflicts such as the Russia-Ukraine war and the Israel-Palestine conflict?', 'response': 'Response'},
        ],
        "Gun Control": [
            {'question': 'Should there be more restrictions on the current process of purchasing a gun?', 'response': 'Response'},
            {'question': '26. Do they generally support gun-control legislation (e.g., red flag laws, boyfriend loopholes)?', 'response': 'Response'}, 
        ],
        "Healthcare": [ 
            {'question': 'What steps would they take to ensure all Americans have access to quality and affordable health care, including reproductive care and prescription drug coverage?', 'response': 'Response'},
            {'question': 'Should the government regulate the prices of life-saving drugs?', 'response': 'Response'},
            {'question': 'Supports a government-run (e.g., single-payer) healthcare program, such as Medicare-for-All?', 'response': 'Response'},
            {'question': 'Stance on abortion and do they support the Supreme Court\'s decision to overturn Roe v. Wade?', 'response': 'Response'},
        ],
        "Immigration": [
            {'question': 'What steps would they take to create an accessible path to citizenship, including for Deferred Action for Childhood Arrivals (DACA) recipients?', 'response': 'Response'},
            {'question': 'How should the country handle undocumented immigrants currently in the U.S.?', 'response': 'Response'},
            {'question': 'Supports increasing security along the southern US border?', 'response': 'Response'},
        ],
        "Social Issues": [
            {'question': 'Should “gender identity” be added to anti-discrimination laws?', 'response': 'Response'},
            {'question': 'Should issues related to LGBTQ+ rights, such as adoption by gay couples, be handled at the federal level or left to the states?', 'response': 'Response'},
        ],
        "Technology and Data Privacy": [
            {'question': 'Should the government impose stricter regulations on the collection and use of personal data by companies?', 'response': 'Response'},
            {'question': 'Should the government increase regulations on social media companies (e.g., TikTok, Facebook)?', 'response': 'Response'},
        ],
        "Voting and Elections": [
            {'question': 'What measures do they support to expand voter access and restore trust in our elections?', 'response': 'Response'},
            {'question': 'Supports requiring a government-issued identification in order to vote at the polls?', 'response': 'Response'},
        ]
    }

    def get_candidate(self, candidate_id: int) -> tuple:
        """
        Return a dictionary of the candidate's data and a status code.
        """

        try:
            candidate_info = self.basic_data.loc[self.basic_data['candidate_id'] == candidate_id, 'name'].iloc[0]
            # name = self.basic_data.loc[self.basic_data['candidate_id'] == candidate_id, 'name'].values[0]
            name = candidate_info['name']
            party = candidate_info['party']
            age = candidate_info['age']
            state = candidate_info['state']
            incumbent = candidate_info['incumbent']
        except:
            name = 'TEST NAME'
            party = 'Unknown'
            age = 0
            state = 'Unknown'
            incumbent = False

        categories = []
        # Filter out traits with missing responses
        for title, traits in self.trait_data.items():
            valid_traits = [trait for trait in traits if trait.get('response', '').strip()]
             # Only add the category if there are valid traits
            if valid_traits:
                categories.append({"title": title, "traits": valid_traits})

        candidate = {
            'candidate_id': candidate_id,
            'name': name,
            'party': party,
            'state': state,
            'age': age,
            'incumbent': incumbent,
            'categories': categories
        }
        
        return candidate, 200
