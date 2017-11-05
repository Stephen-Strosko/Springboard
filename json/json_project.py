import pandas as pd
import os
import json
import numpy as np

from pandas.io.json import json_normalize
from collections import Counter

def question_1(df):
    #Finds the ten countries with the most projects
    df = pd.read_json('world_bank_projects.json')
    ten_largest_name = df['countryname'].value_counts().nlargest(10)

    return ten_largest_name

def question_2(df):
    #Finds the ten most common project themes
    new_list = []
    for row in df.mjtheme:
        new_list.append(row)

    flat_list = []
    for item in new_list:
        try:
            for subitem in item:
                flat_list.append(subitem)
        except TypeError:
            flat_list.append(subitem)

    count = Counter(flat_list)
    ten_largest_themes = count.most_common(10)
    df = pd.DataFrame(ten_largest_themes, columns=['theme', 'occurance'])

    return df

def new_df():
    #Fills in all of the missing names in the mjtheme_namecode column
    data = json.load((open('world_bank_projects.json')))
    df = json_normalize(data, record_path='mjtheme_namecode')
    df.sort_values(by=['code', 'name'])
    df['name'].replace('', np.nan, inplace=True)
    df_with_names = df['name'].fillna(method='bfill')

    return df_with_names

def main():

    #Insert the location of the dataset to this string
    #os.chdir('')
    df = pd.read_json('world_bank_projects.json')

    ten_largest_name = question_1(df)
    ten_largest_themes = question_2(df)
    new_dataframe = new_df()

    print("\nThis is the answer to question one:\n")
    print(ten_largest_name)

    print("\n\n\nThis is the answer to question two:\n")
    print(ten_largest_themes)

    print("\n\n\nThis is my answer to question three:\n")
    print(new_dataframe)

if __name__ == "__main__":
    main()
