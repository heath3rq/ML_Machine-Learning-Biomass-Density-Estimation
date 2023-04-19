# 🇨🇮 Côte d'Ivoire Biomass Density Estimation Project 
## A Comparative Study of Random Forests and CNN in Estimating Biomass and the Relative Importance of Spectral Bands, Cloud Cover, Latitude, and Longitude in the Modeling Process

This repository contains work for the final project for IDS 705. This project’s goal is to to improve the efficiency of biomass estimation using machine learning techniques in areas experiencing deforestation. Biomass has traditionally been measured manually by field experts, which is costly, time-consuming, and difficult to scale. This project explores remote sensing techniques using satellite images. Specifically, this analysis compares the performance of Random Forest models against ResNet Convolution Neural Networks in predicting Above Ground Biomass (AGB) of cocoa plantations in Côte d'Ivoire. 

The results of this project suggests that these models are ineffective at predicting biomass from Sentinel-2 satellite imagery. While other studies have successfully implemented both of these methods for predicting biomass, the referenced work appears limited to higher resolution imagery (i.e. UAV and high resolution imagery).  Additionally, this analysis compares the importance of the image data (i.e., spectral bands, cloud cover, and location), which suggests that the Infrared and vegetation red wavelengths are most important in predicting biomass.  However, due to the inconsistency in feature importance across models, and multicollinearity between bands, this analysis cannot be considered a causal effect. 

# Setup Instructions
* Python version: 3.10 and above
* Packages: run `make install` in terminal
* Please note that the data files for this project are proprietary and cannot be included in this repository. Therefore, in order to run our pre-processing files and Jupyter notebooks, you will need to download the data files first. The data files can be found in the 'Data' section of the Africa Biomass Challenge page on Zindi Africa: https://zindi.africa/competitions/africa-biomass-challenge.

# File Instructions
* Under the PreProcessing directory, you can find code and instruction on how to get and pre-process the data: 
    * Run `python data_load.py` in terminal

* Under the Models directory, you can find code for how to fit the Random Forest and ResNet Models.
    * `random_forest.ipynb`: outlines the model fitting and experiments of the Random Forest model and their results. 
    * `CNN.ipynb`: outlines the model fitting and experiments of the ResNet 50 and ResNet 32 models and their results.

# Modeling Process Map
<img width="725" alt="Screenshot 2023-04-18 at 2 18 49 PM" src="https://user-images.githubusercontent.com/105904149/232868117-6e9630b7-e675-4b93-a485-dca6fcd277b2.png">

# Best Results
|             |  Fine-Tuned Random Forest  | ResNet-32 Model Trained on All Normalized Features |
|-------------|----------------------------|----------------------------------------------------|
| RMSE        | 64.63                      | 60.27                                              |
| R-Sqaured   | 1.68%                      | 14.49%                                             |

# Presentation
[Côte d'Ivoire Biomass Density Estimation Project - Watch Video](https://www.youtube.com/watch?v=jNuOM7gzLPk)

