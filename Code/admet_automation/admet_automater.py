import pandas as pd
import os
from glob import glob

input_folder = "DATA/admet_results/primary_ligands"
output_file = "combined_admet.csv"

csv_files = glob(os.path.join(input_folder, "*.csv"))
all_rows = []

for file in csv_files:
    print(f"Reading file: {file}")
    
    try:
        df = pd.read_csv(file)  # Has header
        print(f"Rows found (excluding header): {df.shape[0]}")
        
        if df.shape[0] == 0:
            print(f"No data rows in {file}. Skipping.")
            continue

        # Access the only data row (index 0)
        admet_row = df.iloc[0].copy()
        admet_row["compound_name"] = os.path.splitext(os.path.basename(file))[0]
        all_rows.append(admet_row)

    except Exception as e:
        print(f"Error reading {file}: {e}")
        continue

if not all_rows:
    print("No valid data rows found.")
    exit()

# Use header from first file + compound_name
columns = list(pd.read_csv(csv_files[0]).columns) + ["compound_name"]
final_df = pd.DataFrame(all_rows, columns=columns)

final_df.to_csv(output_file, index=False)
print(f"Combined CSV saved to: {output_file}")
