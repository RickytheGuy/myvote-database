import logging

import fec_api as fec

OPEN_FEC_API_KEY = "EOtMnBOIMUMAyA73DLcx6cYRVSWlqqID7h1ueVXJ"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

while True:
    logging.info("Launching main data aggregation program...")
    fec.download_bulk_candidate_names(OPEN_FEC_API_KEY)
    break

logging.info("Data aggregation program complete.")