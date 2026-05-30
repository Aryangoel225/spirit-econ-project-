import pandas as pd
import numpy as np
import zipfile
import glob
import os

os.makedirs('data/clean', exist_ok=True)

cols_needed = [
    'Year', 'Quarter',
    'OriginCityMarketID', 'Origin',
    'DestCityMarketID', 'Dest',
    'TkCarrier', 'OpCarrier',
    'Passengers', 'MktFare',
    'NonStopMiles', 'MktCoupons',
    'BulkFare', 'OriginCountry', 'DestCountry'
]

def load_and_clean_one_quarter(zip_path):
    with zipfile.ZipFile(zip_path) as z:
        csv_name = [f for f in z.namelist() if f.endswith('.csv')][0]
        df = pd.read_csv(z.open(csv_name),
                        usecols=cols_needed,
                        low_memory=False)

    df = df[(df['OriginCountry'] == 'US') & (df['DestCountry'] == 'US')]
    df = df[df['MktCoupons'] == 1]
    df = df[df['BulkFare'] == 0]
    df = df[(df['MktFare'] >= 15) & (df['MktFare'] <= 1500)]
    df = df.dropna(subset=['MktFare', 'Passengers', 'NonStopMiles', 'TkCarrier'])
    df = df.drop(columns=['BulkFare', 'OriginCountry', 'DestCountry', 'MktCoupons'])

    print(f"  {zip_path}: {len(df):,} rows after cleaning")
    return df

all_quarters = []
zip_files = sorted(glob.glob('data/raw/DB1BMarket_*.zip'))
print(f"Found {len(zip_files)} zip files\n")

for zf in zip_files:
    try:
        df_q = load_and_clean_one_quarter(zf)
        all_quarters.append(df_q)
    except Exception as e:
        print(f"  ERROR on {zf}: {e}")

df_all = pd.concat(all_quarters, ignore_index=True)
print(f"\nTotal rows: {df_all.shape[0]:,}")

# ── Aggregate to route-carrier-quarter level ──────────────────────────────
print("Aggregating...")

df_agg = (
    df_all
    .groupby(['Year', 'Quarter', 'Origin', 'Dest',
              'OriginCityMarketID', 'DestCityMarketID', 'TkCarrier'])
    .agg(
        Passengers   = ('Passengers', 'sum'),
        AvgFare      = ('MktFare', 'mean'),
        MedianFare   = ('MktFare', 'median'),
        NonStopMiles = ('NonStopMiles', 'first'),
        NumObs       = ('MktFare', 'count')
    )
    .reset_index()
)

print(f"Aggregated rows: {df_agg.shape[0]:,}")
print(f"Columns: {df_agg.columns.tolist()}")

df_agg.to_csv('data/clean/db1b_agg.csv', index=False)
print("\nSaved to data/clean/db1b_agg.csv")
print("Done.")