import pandas as pd

def clean_duplicates(file1, file2):
    """input:  two csv files of the same format, including at minimum an 'email'
               column and a 'stage' column
       output: unique_applicants.csv: a csv file containing all unique
               applicants. Duplicates are resolved by choosing the one at the
               earliest stage
               duplicate_applicants.csv: a csv file containing all of the
               duplicate entries
    """

    # read all data and merge into one dataframe
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)
    frames = [data1, data2]
    allusers = pd.concat(frames)

    # sort in order of stage so lowest stage is always chosen
    allusers.sort_values(["email", "stage"], inplace = True)

    # get a list of unique users
    bool_series_unique = allusers['email'].duplicated(keep='first')
    allusersunique = allusers[~bool_series_unique]

    # get a list of all duplicate entries
    bool_series_dupes = allusers['email'].duplicated(keep=False)
    allusersdupes = allusers[bool_series_dupes]

    #write new files with the results
    allusersunique.to_csv('unique_applicants.csv', index=False)
    allusersdupes.to_csv('duplicate_applicants.csv', index=False)

