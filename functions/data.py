import json
import numpy as np
import pandas as pd
from .formatting.text_tools import title_to_snake_case, replace_char_with_space

pd.set_option('mode.chained_assignment', None)


# Objects included in this file:
# stationary_neighborhoods
# non_stationary_neighborhoods

# Functions included in this file:
# # preprocess


stationary_neighborhoods = [
    "Chinatown",
    "Financial District/South Beach",
    "Glen Park",
    "Golden Gate Park",
    "Japantown",
    "Lakeshore",
    "Lincoln Park",
    "McLaren Park",
    "Mission Bay",
    "Nob Hill",
    "Oceanview/Merced/Ingleside",
    "Portola",
    "Potrero Hill",
    "Seacliff",
    "South of Market",
    "Treasure Island",
    "Twin Peaks",
    "Visitacion Valley",
    "West of Twin Peaks",
]


non_stationary_neighborhoods = [
    "Bayview Hunters Point",
    "Bernal Heights",
    "Castro/Upper Market",
    "Excelsior",
    "Haight Ashbury",
    "Hayes Valley",
    "Inner Richmond",
    "Inner Sunset",
    "Lone Mountain/USF",
    "Marina",
    "Mission",
    "Noe Valley",
    "Outer Richmond",
    "Pacific Heights",
    "Russian Hill",
    "Sunset/Parkside",
    "Tenderloin",
    "North Beach",
    "Outer Mission",
    "Presidio Heights",
    "Western Addition",
]


def preprocess(df):
    """Use this to clean dataframe prior to dumping into SQL database
    """
    # Column names
    df.columns = [replace_char_with_space(col, ['(', ')', '@', ':', '-', '&']) for col in df.columns]
    df.columns = [' '.join(col.split()) for col in df.columns]
    df.columns = [title_to_snake_case(col) for col in df.columns]
    df = df.rename(columns={'date_filed': 'date',
                            'petition_source_zipcode': 'zip_code',
                            'neighborhoods_analysis_boundaries': 'neighborhood_name',
                            'location': 'latlong',
                            'analysis_neighborhoods': 'neighborhood_number', })

    # Zip Code
    df['zip_code'] = df['zip_code'].replace('[-][0-9]{4}', '', regex=True).str.extract(r'(\d+)', expand=False)
    df['zip_code'] = df['zip_code'].apply(lambda x: np.int64(x) if not pd.isnull(x) else x)

    # Location
    df['latlong'] = df['latlong'].apply(
        lambda x: json.loads(x.replace('(', '[').replace(')', ']')) if not pd.isnull(x) else [])
    df['latitude'] = df['latlong'].apply(lambda x: x[0] if x else None)
    df['longitude'] = df['latlong'].apply(lambda x: x[1] if x else None)
    df['latlong'] = df['latlong'].apply(json.dumps)

    # Moves all petition_id's from same date and address to a list in linked_petition_ids
    df = df.merge(df.groupby(['date', 'address'])['petition_id'].apply(
        list).to_frame('linked_petition_ids').reset_index(), on=['date', 'address'])  # used to be petition_id_list
    df['num_petition_id'] = df['linked_petition_ids'].map(len)  # used to be petition_id_len
    df = df.drop(columns=['petition_id']).drop_duplicates(subset=['date', 'address']).reset_index(drop=True)
    df['linked_petition_ids'] = df['linked_petition_ids'].apply(json.dumps)

    return df
