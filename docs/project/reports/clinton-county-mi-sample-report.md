# Agricultural Field Analysis: Clinton County, MI

> **Sample Dataset** — 10-field subset from 50-field Clinton County, Michigan agricultural dataset

---

## Executive Summary

This report presents a comprehensive analysis of agricultural field data for Clinton County, Michigan. The sample dataset includes 10 randomly selected fields representing typical corn-soybean rotation operations in the region.

| Metric             | Value                                |
| ------------------ | ------------------------------------ |
| **Location**       | Clinton County, MI (FIPS: 26037)     |
| **Sample Size**    | 10 fields                            |
| **Total Area**     | 794.7 acres                          |
| **Primary Crops**  | Corn (5 fields), Soybeans (5 fields) |
| **Soil Series**    | 3 dominant (Lenawee, Miami, Fox)     |
| **Weather Period** | 2020-2024 (NASA POWER)               |

---

## Field Summary

### Field Inventory

| Field ID      | Crop (2024) | Area (acres) | Latitude | Longitude |
| ------------- | ----------- | ------------ | -------- | --------- |
| CSB2603700014 | Soybeans    | 76.3         | 43.0535  | -84.6580  |
| CSB2603700018 | Corn        | 129.9        | 42.9883  | -84.7766  |
| CSB2603700020 | Soybeans    | 56.6         | 42.7222  | -84.7823  |
| CSB2603700026 | Corn        | 40.4         | 42.8494  | -84.4305  |
| CSB2603700027 | Corn        | 108.4        | 42.7086  | -84.6721  |
| CSB2603700031 | Corn        | 65.2         | 42.8014  | -84.3730  |
| CSB2603700033 | Corn        | 144.8        | 42.7122  | -84.4831  |
| CSB2603700040 | Soybeans    | 52.9         | 42.7183  | -84.5637  |
| CSB2603700046 | Soybeans    | 119.1        | 42.9964  | -84.6926  |
| CSB2603700049 | Soybeans    | 101.3        | 42.9378  | -84.6913  |

**Total: 794.7 acres** (Average: 79.5 acres/field)

---

## Soil Analysis

### Soil Properties by Field

| Field ID      | Soil Series | OM (%) | pH  | Clay (%) | Drainage Class |
| ------------- | ----------- | ------ | --- | -------- | -------------- |
| CSB2603700014 | Fox         | 1.94   | 6.1 | 19.7     | Well drained   |
| CSB2603700018 | Miami       | 2.09   | 7.0 | 19.6     | Well drained   |
| CSB2603700020 | Lenawee     | 3.28   | 7.1 | 26.7     | Poorly drained |
| CSB2603700026 | Miami       | 2.28   | 6.5 | 19.3     | Well drained   |
| CSB2603700027 | Lenawee     | 3.26   | 6.2 | 25.2     | Poorly drained |
| CSB2603700031 | Lenawee     | 2.88   | 6.0 | 28.7     | Poorly drained |
| CSB2603700033 | Lenawee     | 2.90   | 6.1 | 28.0     | Poorly drained |
| CSB2603700040 | Fox         | 1.88   | 7.0 | 16.8     | Well drained   |
| CSB2603700046 | Miami       | 2.12   | 7.2 | 21.0     | Well drained   |
| CSB2603700049 | Lenawee     | 3.16   | 6.9 | 27.0     | Poorly drained |

### Soil Series Distribution

| Soil Series | Fields | Avg OM (%) | Avg Clay (%) | Typical Drainage |
| ----------- | ------ | ---------- | ------------ | ---------------- |
| Lenawee     | 5      | 3.10       | 27.1         | Poorly drained   |
| Miami       | 3      | 2.16       | 20.0         | Well drained     |
| Fox         | 2      | 1.91       | 18.3         | Well drained     |

### Soil Interpretation for Corn Production

| Factor         | Optimal Range | Observed Range | Assessment   |
| -------------- | ------------- | -------------- | ------------ |
| Organic Matter | 2.0-4.0%      | 1.9-3.3%       | ✓ Adequate   |
| pH             | 5.8-7.0       | 6.0-7.2        | ✓ Acceptable |
| Clay Content   | 15-35%        | 16.8-28.7%     | ✓ Suitable   |
| Drainage       | Well-Mod      | Mix            | ⚠ Variable   |

---

## Weather Data (2020-2024)

### Data Source

Weather data sourced from **NASA POWER** (Prediction Of Worldwide Energy Resources) API[^1].

[^1]: NASA Langley Research Center. (2024). _POWER Data Access Viewer_. https://power.larc.nasa.gov/

### Annual Summary

| Year | Avg Temp (°C) | Avg Max (°C) | Avg Min (°C) | Precip (mm) | Annual GDD |
| ---- | ------------- | ------------ | ------------ | ----------- | ---------- |
| 2020 | 8.9           | 14.0         | 3.8          | 910         | 1,392      |
| 2021 | 9.5           | 14.8         | 4.3          | 914         | 1,640      |
| 2022 | 8.5           | 13.8         | 3.2          | 796         | 1,479      |
| 2023 | 9.5           | 14.9         | 4.3          | 919         | 1,429      |
| 2024 | 10.4          | 15.9         | 5.3          | 868         | 1,684      |

### Monthly Climate Normals

| Month     | Avg Temp (°C) | Avg Precip (mm) | Avg GDD |
| --------- | ------------- | --------------- | ------- |
| January   | -4.4          | 299             | 0       |
| February  | -3.6          | 244             | 0       |
| March     | 2.4           | 370             | 0       |
| April     | 7.6           | 364             | 1       |
| May       | 14.4          | 375             | 5       |
| June      | 20.1          | 442             | 10      |
| July      | 22.0          | 556             | 12      |
| August    | 21.4          | 528             | 11      |
| September | 17.5          | 292             | 8       |
| October   | 10.9          | 415             | 3       |
| November  | 4.0           | 251             | 1       |
| December  | -0.8          | 269             | 0       |

### 5-Year Climate Summary

| Metric                        | Value               |
| ----------------------------- | ------------------- |
| **Average Temperature**       | 9.4°C (48.8°F)      |
| **Total Precipitation**       | 4,406 mm (173.5 in) |
| **Annual Average Precip**     | 881 mm (34.7 in)    |
| **Average Solar Radiation**   | 3.80 kWh/m²/day     |
| **Total Growing Degree Days** | 7,624               |

### Growing Season Analysis (May-September)

| Month     | Avg Temp | Precip       | GDD    |
| --------- | -------- | ------------ | ------ |
| May       | 14.4°C   | 375 mm       | 5      |
| June      | 20.1°C   | 442 mm       | 10     |
| July      | 22.0°C   | 556 mm       | 12     |
| August    | 21.4°C   | 528 mm       | 11     |
| September | 17.5°C   | 292 mm       | 8      |
| **Total** | —        | **2,193 mm** | **46** |

---

## Crop Rotation History (CDL)

### 2020-2024 Crop Sequence by Field

| Field         | 2020     | 2021     | 2022     | 2023     | 2024     |
| ------------- | -------- | -------- | -------- | -------- | -------- |
| CSB2603700014 | Soybeans | Corn     | Corn     | Soybeans | Soybeans |
| CSB2603700018 | Corn     | Soybeans | Corn     | Corn     | Corn     |
| CSB2603700020 | Soybeans | Corn     | Soybeans | Soybeans | Soybeans |
| CSB2603700026 | Corn     | Soybeans | Corn     | Soybeans | Corn     |
| CSB2603700027 | Corn     | Soybeans | Corn     | Corn     | Corn     |
| CSB2603700031 | Corn     | Corn     | Corn     | Corn     | Corn     |
| CSB2603700033 | Corn     | Corn     | Corn     | Soybeans | Corn     |
| CSB2603700040 | Soybeans | Corn     | Corn     | Soybeans | Soybeans |
| CSB2603700046 | Corn     | Soybeans | Soybeans | Corn     | Soybeans |
| CSB2603700049 | Soybeans | Corn     | Corn     | Corn     | Soybeans |

### Rotation Pattern Analysis

| Pattern                    | Fields | Percentage |
| -------------------------- | ------ | ---------- |
| Corn → Soybeans → Corn     | 4      | 40%        |
| Corn → Corn → Corn         | 2      | 20%        |
| Soybeans → Corn → Soybeans | 2      | 20%        |
| Soybeans → Corn → Corn     | 1      | 10%        |
| Corn → Soybeans → Soybeans | 1      | 10%        |

---

## Data Dictionary

### Field Boundaries

| Field          | Type   | Description                                                     |
| -------------- | ------ | --------------------------------------------------------------- |
| `field_id`     | String | Unique CSB identifier (CSB + StateFIPS + CountyFIPS + Sequence) |
| `county_fips`  | String | 5-digit FIPS code (26037 = Clinton County, MI)                  |
| `crop_2024`    | String | Primary crop for 2024 growing season                            |
| `area_acres`   | Float  | Field area in acres                                             |
| `centroid_lat` | Float  | Centroid latitude (WGS84)                                       |
| `centroid_lon` | Float  | Centroid longitude (WGS84)                                      |

### Soil Data

| Field                | Type   | Description                     |
| -------------------- | ------ | ------------------------------- |
| `field_id`           | String | Foreign key to field boundaries |
| `soil_series`        | String | SSURGO soil series name         |
| `organic_matter_pct` | Float  | Organic matter percentage       |
| `ph`                 | Float  | Soil pH (1:1 water)             |
| `clay_pct`           | Float  | Clay content percentage         |
| `drainage_class`     | String | Natural drainage class          |

### Weather Data

| Field               | Type  | Description                                  |
| ------------------- | ----- | -------------------------------------------- |
| `date`              | Date  | Observation date                             |
| `T2M`               | Float | Mean temperature (°C)                        |
| `T2M_MAX`           | Float | Maximum temperature (°C)                     |
| `T2M_MIN`           | Float | Minimum temperature (°C)                     |
| `PRECTOTCORR`       | Float | Precipitation, bias-corrected (mm)           |
| `ALLSKY_SFC_SW_DWN` | Float | All-sky surface shortwave downward radiation |
| `GDD`               | Float | Growing degree days (base 10°C)              |

### CDL Crop Data

| Field      | Type    | Description                     |
| ---------- | ------- | ------------------------------- |
| `field_id` | String  | Foreign key to field boundaries |
| `year`     | Integer | Crop year                       |
| `cdl_code` | Integer | USDA CDL crop code              |
| `cdl_name` | String  | USDA CDL crop name              |

---

## Data Sources

| Dataset          | Source                                       | URL                                                                      |
| ---------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
| Field Boundaries | USDA NASS Crop Sequence Boundaries 2017-2024 | https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries/ |
| Soil Data        | USDA NRCS SSURGO via Soil Data Access API    | https://sdmdataaccess.sc.egov.usda.gov/                                  |
| Weather Data     | NASA POWER                                   | https://power.larc.nasa.gov/                                             |
| Cropland Data    | USDA NASS Cropland Data Layer                | https://nassgeodata.gmu.edu/VegScape/                                    |

---

## Technical Notes

- **Coordinate Reference System**: WGS84 (EPSG:4326) for all geographic data
- **Weather Station**: Representative location (42.89°N, 84.58°W) — county centroid
- **Soil Data**: Point samples at field centroids; actual fields may contain multiple soil map units
- **CDL Classification**: 30-meter resolution; may contain minor land cover impurities

---

## File Inventory

| File                                                       | Description                   |
| ---------------------------------------------------------- | ----------------------------- |
| `fields/50_fields_clinton_michigan_2024.geojson`           | Full 50-field polygon dataset |
| `fields/50_fields_clinton_michigan_centroids.csv`          | Field centroids and metadata  |
| `soil/50_fields_clinton_michigan_soil.csv`                 | SSURGO soil properties        |
| `weather/50_fields_clinton_michigan_weather_2020_2024.csv` | Daily weather observations    |
| `cdl/50_fields_clinton_michigan_cdl_2020_2024.csv`         | CDL crop history              |

---

_Report generated for data analytics review. This is a sample of 10 fields from the full 50-field Clinton County, Michigan agricultural dataset._
