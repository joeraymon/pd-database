from pd_database import PandasDatabase
from pandas.testing import assert_frame_equal

pdb = PandasDatabase("test_db")

# normal dict write
data_dict_w = {"a": 1, "b": 2, "c": 3}
pdb.write(data_dict_w, "test_dict_t", True)
pdb.write(data_dict_w, "test_dict_f", False)

# normal list write
data_list_w = [{"a": 1, "b": 2, "c": 3}]
pdb.write(data_list_w, "test_list_t", True)
pdb.write(data_list_w, "test_list_f", False)

# normal read
data_dict_t = pdb.read("test_dict_t", index_col=0)
data_dict_f = pdb.read("test_dict_f")

data_list_t = pdb.read("test_list_t", index_col=0)
data_list_f = pdb.read("test_list_f")

print(data_dict_t)
print(data_dict_f)
print(data_list_t)
print(data_list_f)

# illegal write
pdb.write({"a": 1}, "test_dict_t")

# illegal read
pdb.read("test_none")