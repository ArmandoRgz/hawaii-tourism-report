import pandas as pd

destination_folder = "processed_frames"
source_folder = "source_files"
filenames = ["hawaii-air_seats","hawaii-expenditure_patterns","hawaii-hotel_performance","hawaii-visitor_characteristics","hawaii-visitor_trends"]

raw_frames = {}
clean_frames = {}
for fname in filenames:
    path = f"{source_folder}/{fname}.csv"
<<<<<<< HEAD
    raw_frames[fname] = pd.read_csv(path)[:-4]
    raw_frames[fname].columns = raw_frames[fname].columns.str.lower()

    cols = raw_frames[fname].columns.tolist()
    id_vars = [col for col in cols if not col[0].isdigit()]
    clean_frames[fname] = raw_frames[fname].melt(id_vars = id_vars, var_name = "period_date", value_name = "value")

    clean_frames[fname]["period_date"] = pd.to_datetime(clean_frames[fname]["period_date"])
    clean_frames[fname]["value"] = pd.to_numeric(clean_frames[fname]["value"].astype(str).replace(',',''),errors='coerce')
=======
    raw_frames[fname] = pd.read_csv(path)

    cols = raw_frames[fname].columns.tolist()
    id_vars = [col for col in cols if not col[0].isdigit()]
    clean_frames[fname] = raw_frames[fname].iloc[:-4].melt(id_vars = id_vars, var_name = "period_date", value_name = "value")

    clean_frames[fname]["period_date"] = pd.to_datetime(clean_frames[fname]["period_date"])
    if clean_frames[fname]["value"].dtype != "float":
        clean_frames[fname]["value"] = clean_frames[fname]["value"].str.replace(',','').astype("float")
>>>>>>> 03dd5e64255946d688c0f7c495aca7c8ef974629

    clean_frames[fname].to_csv(f"{destination_folder}/{fname}.csv",index=False)

