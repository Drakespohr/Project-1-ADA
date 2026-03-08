---
name: ag-skills-collection
description: Agricultural Data Analysis Skills - A collection of AI-ready skills for downloading and analyzing US agricultural data using standard Python libraries.
license: MIT
metadata:
  author: Boreal Bytes
  version: '1.0'
  source: https://github.com/borealbytes/ag-skills
---

# Agricultural Data Analysis Skills

A collection of Agent Skills for agricultural data download and analysis tasks. These skills follow the [AgentSkills.io](https://agentskills.io) specification.

## Skills Overview

### Data Download Skills

| Skill                                       | Description                        |
| ------------------------------------------- | ---------------------------------- |
| [field-boundaries](field-boundaries/)       | USDA NASS Crop Sequence Boundaries |
| [ssurgo-soil](ssurgo-soil/)                 | USDA NRCS SSURGO soil data         |
| [nasa-power-weather](nasa-power-weather/)   | NASA POWER weather data            |
| [cdl-cropland](cdl-cropland/)               | USDA NASS Cropland Data Layer      |
| [sentinel2-imagery](sentinel2-imagery/)     | ESA Sentinel-2 satellite imagery   |
| [landsat-imagery](landsat-imagery/)         | USGS Landsat satellite imagery     |
| [interactive-web-map](interactive-web-map/) | Interactive web maps               |

### Analysis Skills

| Skill                               | Description                                         |
| ----------------------------------- | --------------------------------------------------- |
| [eda-explore](eda-explore/)         | Data exploration with pandas, numpy                 |
| [eda-visualize](eda-visualize/)     | Data visualization with pandas, matplotlib, seaborn |
| [eda-correlate](eda-correlate/)     | Correlation analysis with pandas, scipy             |
| [eda-time-series](eda-time-series/) | Time series analysis with pandas, matplotlib        |
| [eda-compare](eda-compare/)         | Group comparisons with pandas, scipy                |

## Usage

When working on agricultural data tasks, check the `.skills/` directory for relevant skills. Agents supporting the AgentSkills.io specification will automatically discover these skills.

### Quick Start

```bash
# Install UV (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Example: Download field boundaries
cd .skills/field-boundaries
uv run --with geopandas python << 'EOF'
from field_boundaries import download_fields
fields = download_fields(count=2, regions=['corn_belt'])
fields.to_file('my_fields.geojson')
EOF
```

## Dependency Chain

```
field-boundaries (REQUIRED FIRST)
    │
    ├──> ssurgo-soil (uses field polygons)
    ├──> nasa-power-weather (uses field locations)
    ├──> cdl-cropland (can use fields for AOI)
    ├──> sentinel2-imagery (needs AOI)
    ├──> landsat-imagery (needs AOI)
    └──> interactive-web-map (visualizes fields)

eda-* skills (independent - work with any CSV)
```

## License

MIT License - See [LICENSE](https://github.com/borealbytes/ag-skills/blob/main/LICENSE)

## Citation

```
USDA National Agricultural Statistics Service Cropland Data Layer. 2023.
Published crop-specific data layer [Online].
Available at https://nassgeodata.gmu.edu/CropScape/
```
