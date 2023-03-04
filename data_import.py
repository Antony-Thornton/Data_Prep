import pathlib
import pandas as pd

# Import first worksheet
def create_data_frame():
    import config

    data_path = config.data_path
    file_name = config.file_name

    full_path = pathlib.Path(data_path, file_name)

    data = pd.read_excel(full_path, sheet_name='Actual Days')
    df = pd.DataFrame(data)

    return df


# Import second worksheet
def create_data_frame1():
    import config

    data_path = config.data_path
    file_name = config.file_name

    full_path = pathlib.Path(data_path, file_name)

    data = pd.read_excel(full_path, sheet_name='Available Days')
    df1 = pd.DataFrame(data)

    return df1


# Import second worksheet
def create_lookup_data_frame():
    import config

    data_path = config.data_path
    lookup_file = config.lookup_file

    full_path = pathlib.Path(data_path, lookup_file)

    data = pd.read_excel(full_path, sheet_name='Sheet1')
    ldf = pd.DataFrame(data)

    return ldf

# create_data_frame()
# create_data_frame1()
# #create_lookup_data_frame()