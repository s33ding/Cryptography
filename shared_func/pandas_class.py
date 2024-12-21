import os
import csv
import pandas as pd
import sys

class Pd:
    def __init__(self, file_name = None):
        self.file_name = self.get_file_name(file_name)

    def get_file_name(self, file_name):
        if file_name is None: 
            if len(sys.argv) > 1:
                return sys.argv[1]
            else:
                return input("file_name:")
        else:   
            return file_name
        
    def write_file(self, df):
        file_name = self.file_name
        print("writing:", file_name)
        if file_name.endswith('.xlsx'):
            df.to_excel(file_name,index=False)

        if file_name.endswith('.json'):
            df.to_json(file_name)

        elif file_name.endswith('.parquet'):
            df.to_parquet(file_name,index=False)

        elif file_name.endswith('.pickle'):
            df.to_pickle(file_name)

        elif file_name.endswith('.csv'):
            df.to_csv(file_name,index=False)
        else:
            raise ValueError(f"Unrecognized file type for file {file_name}")

    def read_file(self):
        file_name = self.file_name
        print("reading:", file_name)

        if file_name.endswith('.xlsx'):
            self.df = pd.read_excel(file_name)
            return self.df

        if file_name.endswith('.json'):
            self.df = pd.read_json(file_name)
            return self.df

        elif file_name.endswith('.parquet'):
            self.df = pd.read_parquet(file_name)
            return self.df

        elif file_name.endswith('.pickle'):
            self.df = pd.read_pickle(file_name)
            return self.df

        elif file_name.endswith('.csv'):
            self.df = pd.read_csv(file_name)
            return self.df
        else:
            raise ValueError(f"Unrecognized file type for file {file_name}")

    def try_open_all_parquets_and_log_errors():
        """
        Tries to open all parquet files in the current directory and logs any errors in erro_log.csv.
        """
        error_log_file = 'error_log.csv'
        error_log_header = ['file_name', 'error_message']
        error_folder = 'erro'

        # Create an empty error log file or overwrite the existing one.
        with open(error_log_file, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(error_log_header)

        # Create a subfolder for erro files if it doesn't exist.
        if not os.path.exists(error_folder):
            os.makedirs(error_folder)

        # Get a list of all parquet files in the current directory.
        all_parquets = [file_name for file_name in os.listdir('.') if file_name.endswith('.parquet')]
        total_parquets = len(all_parquets)

        # Try to open each parquet file in the current directory.
        for i, file_name in enumerate(all_parquets):
            try:
                pd.read_parquet(file_name)
            except Exception as e:
                # Log the error message in the error log file.
                with open(error_log_file, mode='a') as file:
                    writer = csv.writer(file)
                    writer.writerow([file_name, str(e)])

                # Move the erro file to the erro subfolder.
                os.rename(file_name, os.path.join(error_folder, file_name))

            # Print progress message.
            print(f"Processed file {i+1} of {total_parquets}: {file_name}")

        print("Done processing all parquet files.")

    def read_multiple_files_and_integrate(directory_path='.'):
        if directory_path[-1] != '/':
            directory_path = directory_path + '/'

        print(f"directory_path: {directory_path}")

        # Get a list of all the files in the directory
        file_paths = [f"{directory_path}{f}" for f in os.listdir(directory_path)]

        df_list = []

        for file_path in file_paths:
            df = self.read_file(file_path)
            if df is not None:
                df_list.append(df)

        return pd.concat(df_list, ignore_index=True)
