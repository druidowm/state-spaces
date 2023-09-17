from datasets import load_dataset
import pickle

data_dir = "data/listops/"
if __name__ == "__main__":
    dataset = load_dataset("csv", data_files="data/listops/basic_test.tsv", cache_dir = "cache")
    import pdb; pdb.set_trace()
dataset = load_dataset(
"csv",
data_files={
"train": data_dir + "/basic_train.tsv",
"val": data_dir + "/basic_val.tsv",
"test": data_dir + "/basic_test.tsv",
},
delimiter="\t",
download_mode="offline",
keep_in_memory=True,
)
