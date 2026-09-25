import networkx as nx
import numpy as np
import pandas as pd

state_names = {
    0: "AL",
    1: "AZ",
    2: "AR",
    3: "CA",
    4: "CO",
    5: "CT",
    6: "DC",
    7: "DE",
    8: "FL",
    9: "GA",
    10: "ID",
    11: "IL",
    12: "IN",
    13: "IA",
    14: "KS",
    15: "KY",
    16: "LA",
    17: "ME",
    18: "MD",
    19: "MA",
    20: "MI",
    21: "MN",
    22: "MS",
    23: "MO",
    24: "MT",
    25: "NE",
    26: "NV",
    27: "NH",
    28: "NJ",
    29: "NM",
    30: "NY",
    31: "NC",
    32: "ND",
    33: "OH",
    34: "OK",
    35: "OR",
    36: "PA",
    37: "RI",
    38: "SC",
    39: "SD",
    40: "TN",
    41: "TX",
    42: "UT",
    43: "VT",
    44: "VA",
    45: "WA",
    46: "WV",
    47: "WI",
    48: "WY"
}

state_pos = {
    "AL": (2,-2),   # AL
    "AZ": (-3,-1),  # AZ
    "AR": (0,-1),   # AR
    "CA": (-5,0),   # CA
    "CO": (-2,0),   # CO
    "CT": (6,1),    # CT
    "DC": (4,-1),   # DC
    "DE": (5,0),    # DE
    "FL": (3,-3),   # FL
    "GA": (3,-2),   # GA
    "ID": (-3,1),   # ID
    "IL": (1,1),    # IL
    "IN": (2,1),    # IN
    "IA": (0,1),    # IA
    "KS": (-1,0),   # KS
    "KY": (2,0),    # KY
    "LA": (0,-2),   # LA
    "ME": (7,3),    # ME
    "MD": (4,0),    # MD
    "MA": (6,2),    # MA
    "MI": (2,2),    # MI
    "MN": (0,2),    # MN
    "MS": (1,-2),   # MS
    "MO": (0,0),    # MO
    "MT": (-2,2),   # MT
    "NE": (-1,1),   # NE
    "NV": (-4,0),   # NV
    "NH": (6,3),    # NH
    "NJ": (5,1),    # NJ
    "NM": (-2,-1),  # NM
    "NY": (5,2),    # NY
    "NC": (4,-2),   # NC
    "ND": (-1,3),   # ND
    "OH": (3,1),    # OH
    "OK": (-1,-1),  # OK
    "OR": (-4,1),   # OR
    "PA": (4,1),    # PA
    "RI": (7,1),    # RI
    "SC": (4,-3),   # SC
    "SD": (-1,2),   # SD
    "TN": (2,-1),   # TN
    "TX": (-1,-2),  # TX
    "UT": (-3,0),   # UT
    "VT": (5,3),    # VT
    "VA": (3,-1),   # VA
    "WA": (-4,2),   # WA
    "WV": (3,0),    # WV
    "WI": (1,2),    # WI
    "WY": (-2,1),   # WY
}

state_abbr = {
    "Alabama": "AL",
    #"Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "District of Columbia": "DC",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    #"Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}

state_abbr_rev = {v: k for k, v in state_abbr.items()}

state_adjacency = pd.read_csv("../Data/adjacency_matrix.csv", index_col=0)
adjacency_matrix = state_adjacency.values
state_graph = nx.from_numpy_array(adjacency_matrix)
state_graph = nx.relabel_nodes(state_graph, state_names)

opioid_data = pd.read_csv("../Data/opioid_overdose_death_rate.csv", index_col=0)
all_drug_data = pd.read_csv("../Data/all_drug_overdose_death_rate.csv", index_col=0)