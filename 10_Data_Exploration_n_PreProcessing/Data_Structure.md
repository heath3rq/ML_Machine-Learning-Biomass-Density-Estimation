## Data Preprocessing 
This document provides instruction on how to use the `data_load.py` file. 

### Datasets
Dimensions = (number of rows, 15 by 15, channel)
- Reference Data
    |_Train Set
    |_ Validation Set
    |_ Test Set
- Ground Truth data
    |_Ground Truth Set

### Features
- Above Ground Biomass Density
- cloud
- images with 12 bands 
- latitude 
- longitude
- Sentinel Classification code 
- Enhance Vegetative Index

## Transformation
Used pixel histograms with length of 3
Resulting feature matrix of number of rows by (3*17) -> number of rows by 51

## Final data set structure

### X_features

| Header Name             | Array of 16 Columns |
|-------------------------|---------------------|
| Coastal_Aerosol         | 1-3                 |
| Blue                    | 4-6                 |
| Green                   | 7-9                 |
| Red                     | 10-12               |
| Vegetation_Red_Edge     | 13-15               |
| Vegetation_Red_Edge_2   | 16-18               |
| Vegetation_Red_Edge_3   | 19-21               |
| NIR                     | 22-24               |
| Narrow_NIR              | 25-27               |
| Water_Vapor             | 28-30               |
| SWIR_1                  | 31-33               |
| SWIR_2                  | 34-36               |
| cloud                   | 37-39               |
| Sentinel_Code           | 40-42               |
| latitude                | 43-45               |
| longitude               | 46-48               |
| EVI                     | 49-51               |

### y_targets
| Header Name             | Array of 16 Columns |
|-------------------------|---------------------|
| agbd                    | 1                   |

## To use

### Example
Run `python data_load.py` in terminal

X_train = np.loadtxt("X_train.txt")
