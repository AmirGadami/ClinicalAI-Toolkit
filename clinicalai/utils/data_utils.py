import pandas as pd
import os
import json
import sys

class DatUtils:
    def __init__(self,data_dir):
        """
        Initialize the DataUtils class with the data directory.
        :param data_dir: Base directory for the dataset files.
        """
        self.data_dir = data_dir

    def read_data(self,file_name):
        """
        Reads a CSV file from the data directory.
        :param file_name: Name of the file to read.
        :return: DataFrame containing the data.
        """
        file_path = os.path.join(self.data_dir,file_name)
        if not os.path.exists(file_path):
            raise FileExistsError(f"File not found: {file_path}")
        if file_path.endswith(".csv"):
                return pd.read_csv(file_path)
        elif file_path.endswith(".json"):
            with open(file_path,'r') as f:
                data = json.load(f)
            return pd.DataFrame(data).T
        else:
            raise ValueError("Unsupported file format. Please provide a csv or json file.")

    def save_data(self,data,file_name):
        """
        Saves data to a JSON file in the data directory.
        :param data: Data to save (dict or list).
        :param file_name: Name of the file to save.
        """
        file_path = os.path.join(self.data_dir,file_name)
        with open(file_path,"w") as f:
            json.dump(data,f,indent=4)
        print(f"File saved: {file_path}")




if __name__ =="__main__":
    PATH_ROOT  = "/Users/amir/Desktop/GitHub/ClinicalAI-Toolkit"
    
    if PATH_ROOT not in sys.path:
        sys.path.append(PATH_ROOT)
        print("ROOT JUST ADDED")

    from config import RAW_DATA_DIR,DATASET_NAME
    print(RAW_DATA_DIR)
    D = DatUtils(RAW_DATA_DIR)
    data = D.read_data(DATASET_NAME)
    print(data.head())

