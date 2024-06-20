import os

import pandas as pd

class ServerData():
    def __init__(self) -> None:
        self.basic_data = pd.read_csv(os.path.join('data', 'candidate_basic.csv'))
    
    def get_names(self) -> str:
        return self.basic_data[['name', 'candidate_id']].to_json(orient='records')
    