## Data Preprocessing 

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
Used pixel histograms with length of 16
Resulting feature matrix of number of rows by (16*17) -> number of rows by 272

## Final data set structure

### X_features

| Header Name             | Array of 16 Columns |
|-------------------------|---------------------|
| Coastal_Aerosol         | 1-16                |
| Blue                    | 17-32               |
| Green                   | 33-48               |
| Red                     | 49-64               |
| Vegetation_Red_Edge     | 65-80               |
| Vegetation_Red_Edge_2   | 81-96               |
| Vegetation_Red_Edge_3   | 97-112              |
| NIR                     | 113-128             |
| Narrow_NIR              | 129-144             |
| Water_Vapor             | 145-160             |
| SWIR_1                  | 161-176             |
| SWIR_2                  | 177-192             |
| cloud                   | 193-208             |
| Sentinel_Code           | 209-224             |
| latitude                | 225-240             |
| longitude               | 241-256             |
| EVI                     | 257-272             |

### y_targets
| Header Name             | Array of 16 Columns |
|-------------------------|---------------------|
| agbd                    | 1                   |

## To use

### Example
Run data_load.py
X_train = np.loadtxt("X_train.txt")