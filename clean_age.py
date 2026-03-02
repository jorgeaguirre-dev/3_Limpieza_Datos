import pandas as pd
import re

def clean_age_contextual(age_str):
    age_str = str(age_str).upper().strip()
    
    # Casos sin información de edad
    if age_str in ['?', 'NOT KNOWN', 'UNKNOWN', 'NAN', 'MAKE LINE GREEN', 'A.M.', 'X', '!!', '!']:
        return None 

    # Conversiones sensillas
    mappings = {
        'TEEN': '15',
        'TEENS': '15',
        'ADULT': '30',
        '(ADULT)': '30',
        'MIDDLE AGE': '45',
        '"MIDDLE-AGE"': '45',
        'ELDERLY': '70',
        'YOUNG': '20',
        '"YOUNG"': '20',
        'A MINOR': '12'
    }
    if age_str in mappings:
        return mappings[age_str]
    
    return age_str