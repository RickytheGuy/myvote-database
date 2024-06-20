import os
import logging
import time

import requests
import pandas as pd
import numpy as np

import timing as tm

def download_bulk_candidate_names(api_key: str) -> str:
    """
    Downloads a list of all candidate names and IDs from the FEC API.
    """
    file = os.path.join('data', 'candidate_basic.csv')
    if not tm.ready_to_download(file, update_interval=1):
        logging.info("FEC data is up to date.")
        return file
    # Download the data from the FEC API
    page = 1
    dfs = []
    last_page = np.inf
    while page <= last_page:
        response = requests.get(f'https://api.open.fec.gov/v1/candidates/?per_page=100&page={page}&is_active_candidate=true&api_key={api_key}')
        data = response.json()
        if last_page == np.inf:
            last_page = data['pagination']['pages']
        while not data.get('results', False):
            time.sleep(60)
            response = requests.get(f'https://api.open.fec.gov/v1/candidates/?per_page=100&page={page}&is_active_candidate=true&api_key={api_key}')
            data = response.json()
        df = pd.DataFrame(data['results'])
        dfs.append(df)
        logging.info(f"Downloaded page {page} of {last_page}")
        page += 1
    
    pd.concat(dfs, axis=0, ignore_index=True).to_csv(file, index=False)
    return file
