import pandas as pd
from .config import Logger
import os

log = Logger()

class PandasDatabase:

    def __init__(self, mount: str = "db"):
        self.dir = mount

    def qualified_table_name(self, table_name: str, operation: str) -> str:
        """
        Args:
        table_name: csv file name where data is stored
        operation: read or write operation needs to be specified 

        Returns:
        str: qualified table name or None if invalid table_name
        """
        
        table_path = f"{self.dir}/{table_name}.csv"

        if operation == "r":
            if os.path.isfile(table_path):
                return table_path
            else:
                log.log(f"Table not found: {table_path}", level="error")
                return None
        elif operation == "w":
            if not os.path.isfile(table_path):
                return table_path
            else:
                log.log(f"Table name taken: {table_path}", level="error")
                return None

    def read(self, table_name: str, index_col: int = None) -> pd.DataFrame:
        """Simple CSV->DF Read Operation
        
        Args:
        table_name: csv file name where data is stored
        index_col: column number to set as index
        
        Returns:
        pd.DataFrame: extracted data
        """

        qualified_table_name = self.qualified_table_name(table_name)

        try:
            df = pd.read_csv(qualified_table_name, index_col=index_col)
        except FileNotFoundError:
            log.log(f"Qualified Table Name: {qualified_table_name} not found.", level="error")
            return None
        log.log(f"Loaded {len(df)} rows from {qualified_table_name}")
        return df
    
    def write(self, data: any, table_name: str, save_index: bool = None) -> None:
        """Simple DF->CSV Write Operation

        Args:
        data: data to be written
        table_name: csv file name where data is stored
        save_index: write index along with data

        Returns:
        None
        """

        qualified_table_name = self.qualified_table_name(table_name)

        if qualified_table_name is None:
            return None

        if type(data) == dict:
            # creates single-column, multi-row, vertical table
            df = pd.DataFrame.from_dict(data=data, orient="index", columns=["Value"])
            if save_index is None:
                save_index = True
        elif type(data) == list:
            # creates multi-column, one-to-multi row, horizontal table
            df = pd.DataFrame(data)
            if save_index is None:
                save_index = False
        elif type(data) == pd.DataFrame:
            df = data.copy()
            if save_index is None:
                save_index = False
        df.to_csv(qualified_table_name, index=save_index)
        log.log(f"Saved {len(df)} rows to {qualified_table_name}")
