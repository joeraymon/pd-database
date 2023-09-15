import pandas as pd
from config import Logger

log = Logger()

class PandasDatabase:

    def __init__(self, mount: str="db"):
        self.dir = mount

    def qualified_table_name(self, table_name: str) -> str:
        return f"{self.dir}/{table_name}.csv"

    def read(self, table_name: str, index_col: int=None) -> pd.DataFrame:
        qualified_table_name = self.qualified_table_name(table_name)
        df = pd.read_csv(qualified_table_name, index_col=index_col)
        log.log(f"Loaded {len(df)} rows from {qualified_table_name}")
        return df
    
    def write(self, data: any, table_name: str, save_index: bool=False):
        qualified_table_name = self.qualified_table_name(table_name)
        if type(data) == dict:
            df = pd.DataFrame.from_dict(data=data, orient="index", columns=["Value"])
        elif type(data) == pd.DataFrame:
            df = data.copy()
        df.to_csv(qualified_table_name, index=save_index)
        log.log(f"Saved {len(df)} rows to {qualified_table_name}")
