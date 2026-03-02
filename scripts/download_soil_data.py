#!/usr/bin/env python3
"""
Generate representative soil data for Clinton County, MI fields.
Based on actual SSURGO soil series common in the region.
"""

import pandas as pd
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path("data/ag-skills/soil")
OUTPUT_FILE = OUTPUT_DIR / "soil_data.csv"

# Clinton County, MI typical soil series
# Source: USDA SSURGO - common soils in Clinton County
SOIL_SERIES = [
    {
        "series": "Lenawee",
        "name": "Lenawee silt loam, 0 to 2 percent slopes, occasionally flooded",
        "om": 3.2, "ph": 6.5, "awc": 0.22, "clay": 27, "sand": 35, "drainage": "Poorly drained",
        "cec": 18, "kb": 2.8
    },
    {
        "series": "Miami",
        "name": "Miami silt loam, 2 to 6 percent slopes",
        "om": 2.1, "ph": 6.8, "awc": 0.20, "clay": 20, "sand": 40, "drainage": "Well drained",
        "cec": 14, "kb": 3.2
    },
    {
        "series": "Fox",
        "name": "Fox silt loam, 2 to 6 percent slopes",
        "om": 1.8, "ph": 6.5, "awc": 0.18, "clay": 18, "sand": 45, "drainage": "Well drained",
        "cec": 12, "kb": 3.5
    },
    {
        "series": "Boyer",
        "name": "Boyer loamy sand, 2 to 6 percent slopes",
        "om": 1.2, "ph": 6.2, "awc": 0.12, "clay": 8, "sand": 70, "drainage": "Excessively drained",
        "cec": 6, "kb": 2.1
    },
    {
        "series": "Capac",
        "name": "Capac clay loam, 0 to 3 percent slopes",
        "om": 2.8, "ph": 7.0, "awc": 0.24, "clay": 35, "sand": 25, "drainage": "Somewhat poorly drained",
        "cec": 22, "kb": 2.5
    },
    {
        "series": "Blount",
        "name": "Blount silt loam, 2 to 4 percent slopes",
        "om": 2.5, "ph": 6.6, "awc": 0.21, "clay": 25, "sand": 32, "drainage": "Somewhat poorly drained",
        "cec": 16, "kb": 2.7
    },
    {
        "series": "Glynwood",
        "name": "Glynwood silt loam, 2 to 6 percent slopes",
        "om": 2.3, "ph": 6.7, "awc": 0.19, "clay": 22, "sand": 38, "drainage": "Well drained",
        "cec": 15, "kb": 3.0
    },
]


def main():
    print("=" * 60)
    print("SSURGO Soil Data - Clinton County, MI")
    print("=" * 60)
    print("\n[1/2] Generating soil data based on SSURGO soil series...")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    np.random.seed(26037)
    
    # Read field centroids
    fields_df = pd.read_csv("data/ag-skills/fields/clinton_50_centroids.csv")
    
    soil_data = []
    
    for _, row in fields_df.iterrows():
        # Weight towards more common soils (Miami, Lenawee, Blount)
        weights = [0.25, 0.22, 0.18, 0.10, 0.12, 0.08, 0.05]
        soil = np.random.choice(SOIL_SERIES, p=weights)
        
        # Add realistic variation
        variation = lambda x: x + np.random.uniform(-x*0.1, x*0.1) if x > 0 else x
        
        soil_data.append({
            "field_id": row["field_id"],
            "mukey": f"MI{hash(soil['series']) % 10000:05d}",  # Simulated mukey
            "soil_series": soil["series"],
            "soil_name": soil["name"],
            "organic_matter_pct": round(variation(soil["om"]), 2),
            "ph": round(variation(soil["ph"]), 1),
            "available_water_capacity": round(variation(soil["awc"]), 3),
            "clay_pct": round(variation(soil["clay"]), 1),
            "sand_pct": round(variation(soil["sand"]), 1),
            "silt_pct": round(100 - variation(soil["clay"]) - variation(soil["sand"]), 1),
            "cec_meq_100g": round(variation(soil["cec"]), 1),
            "bulk_density_g_cm3": round(variation(soil["kb"]), 2),
            "drainage_class": soil["drainage"],
            "latitude": round(row["centroid_lat"], 6),
            "longitude": round(row["centroid_lon"], 6)
        })
    
    df = pd.DataFrame(soil_data)
    
    # Save to CSV
    df.to_csv(OUTPUT_FILE, index=False)
    
    print(f"   Generated {len(df)} soil records")
    print(f"   Saved to {OUTPUT_FILE}")
    
    print(f"\n[2/2] Summary:")
    print(f"   Soil series found: {', '.join(df['soil_series'].unique())}")
    print(f"   Avg organic matter: {df['organic_matter_pct'].mean():.2f}%")
    print(f"   Avg pH: {df['ph'].mean():.1f}")
    print(f"   Avg clay content: {df['clay_pct'].mean():.1f}%")
    
    print("\n" + "=" * 60)
    print("Done! Soil data saved.")
    print("=" * 60)


if __name__ == "__main__":
    main()
