import pandas as pd

def excel_to_dicts(excel_file_path):
    """
    Reads an Excel file and converts each column (except the first one) into a dictionary.
    The keys for the dictionaries are taken from the first column of the Excel sheet.

    Args:
    - excel_file_path (str): The path to the Excel file to be read.

    Returns:
    - dict of dict: A dictionary containing dictionaries for each column in the Excel sheet.
    """
    # Read the Excel file
    df = pd.read_excel(excel_file_path, header=0)  # Assuming the first row is the header

    # Initialize a dictionary to hold the column dictionaries
    column_dicts = {}

    # Loop through each column in the dataframe, skipping the first one
    for col in df.columns[1:]:
        # Convert the column to a dictionary with the first column as keys
        column_dicts[col] = pd.Series(df[col].values, index=df[df.columns[0]]).to_dict()

    # Replace NaN values with None in the dictionaries
    for column_dict in column_dicts.values():
        for key, value in column_dict.items():
            if pd.isna(value):
                column_dict[key] = None

    return column_dicts

# Usage example (you should replace the 'excel_file_path' with your actual file path):
# dictionaries = excel_to_dictionaries('/path/to/your/excel/file.xlsx')
if __name__ == '__main__':
    excel_file_path = r'/Users/apple/Downloads/ik_bones_rename.xlsx'
    column_dicts = excel_to_dicts(excel_file_path)
    print(column_dicts['mixamo_xiaobairen'])