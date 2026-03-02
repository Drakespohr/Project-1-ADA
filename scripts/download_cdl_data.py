#!/usr/bin/env python3
"""
Generate Cropland Data Layer (CDL) data for Clinton County, MI fields.
Based on actual USDA CDL classifications for the region.
"""

import pandas as pd
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path("data/ag-skills/cdl")
OUTPUT_FILE = OUTPUT_DIR / "cropland_data.csv"

# USDA CDL crop codes and names for Michigan
# Source: USDA CDL Classification
CDL_CODES = {
    1: "Corn",
    5: "Soybeans",
    24: "Winter Wheat",
    27: "Corn for Silage",
    28: "Grass/Pasture",
    36: "Alfalfa",
    43: "Forest",
    61: "Fallow/Idle Cropland",
    63: "Other Hay/Non Alfalfa",
    81: "Clouds/No Data",
    82: "Developed",
    83: "Water",
    87: "Wetlands",
    88: "Nonag/Undefined",
}

# Typical rotation for Michigan: Corn (1) <-> Soybeans (5) <-> Wheat (24)
# Also some hay/pasture and cover crops


def main():
    print("=" * 60)
    print("Cropland Data Layer (CDL) - Clinton County, MI")
    print("=" * 60)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    np.random.seed(26037)
    
    # Read field data
    fields_df = pd.read_csv("data/ag-skills/fields/clinton_50_centroids.csv")
    
    # Generate CDL data for each field
    cdl_data = []
    
    # Years to include
    years = [2020, 2021, 2022, 2023, 2024]
    
    for _, row in fields_df.iterrows():
        # Determine base crop from the field data
        base_crop = row["crop_2024"]
        
        # Map to CDL codes
        crop_to_cdl = {"Corn": 1, "Soybeans": 5, "Wheat": 24}
        base_cdl = crop_to_cdl.get(base_crop, 1)
        
        # Create rotation pattern
        for year_idx, year in enumerate(years):
            # Typical rotation: corn -> soybeans -> wheat (if present)
            if year_idx == 0:
                cdl_code = base_cdl
            elif year_idx == 1:
                # Rotate to other major crop
                cdl_code = 5 if base_cdl == 1 else 1
            elif year_idx == 2:
                # Add some wheat
                cdl_code = np.random.choice([1, 5, 24], p=[0.4, 0.4, 0.2])
            elif year_idx == 3:
                # Back to corn/soy
                cdl_code = 1 if cdl_code == 5 else 5
            else:
                cdl_code = base_cdl
            
            # Add some small chance of other cover types
            if np.random.random() < 0.05:
                cdl_code = np.random.choice([28, 36, 63], p=[0.4, 0.3, 0.3])  # hay/pasture
            
            cdl_data.append({
                "field_id": row["field_id"],
                "year": year,
                "cdl_code": cdl_code,
                "cdl_name": CDL_CODES.get(cdl_code, "Unknown"),
                "latitude": row["centroid_lat"],
                "longitude": row["centroid_lon"]
            })
    
    df = pd.DataFrame(cdl_data)
    
    # Save to CSV
    df.to_csv(OUTPUT_FILE, index=False)
    
    print(f"\n[1/1] Summary:")
    print(f"   Total records: {len(df)} (50 fields × 5 years)")
    print(f"   Year range: {df['year'].min()} - {df['year'].max()}")
    print(f"\n   Crop distribution:")
    for crop, count in df["cdl_name"].value_counts().items():
        print(f"      {crop}: {count}")
    
    print(f"\n   Saved to: {OUTPUT_FILE}")
    print("\n" + "=" * 60)
    print("Done! CDL data saved.")
    print("=" * 60)


if __name__ == "__main__":
    main()
