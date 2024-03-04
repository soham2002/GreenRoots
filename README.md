# Green Roots AI Model

## Overview

Welcome to the Green Roots AI Model repository! This repository contains code for an AI model designed to analyze Landsat satellite imagery from Google Earth Engine (GEE) to predict mangrove distribution and health patterns. The model utilizes machine learning techniques and interactive visualization tools to assist in environmental monitoring and conservation efforts.

## Features

- **Satellite Imagery Analysis**: The model utilizes Landsat satellite imagery from GEE to analyze mangrove distribution and health by computing relevant indices.
- **Temporal Analysis**: Green Roots provides temporal analysis of mangrove health by computing mean index values over time and visualizing temporal trends.
- **Interactive Dashboard**: The model includes an interactive dashboard built with Dash, allowing users to explore and visualize satellite imagery and mangrove trends.

## Installation

To run the Green Roots AI Model locally, follow these steps:

1. Install the required Python packages:

    ```bash
    pip install requirements.txt
    ```

2. Create your Google Earth Engine Account:

   If you already have an account in the GEE you can skip to the next step.
   Create a [Google Earth Engine](https://earthengine.google.com/signup/)Account
   
3. Authenticate and initialize Google Earth Engine by following the prompts after running the code snippet:

   ```python
    import ee
    ee.Authenticate()
    ee.Initialize(project='replace_with_your_earth_engine_project_name')
    ```

4. Launch the application.
   ```python
    python launch_app.py
    ```

## Usage

Once installed and configured, you can use the Green Roots AI Model for the following tasks:

1. **Satellite Imagery Analysis**: Analyze Landsat satellite imagery for mangrove distribution and health assessment. The model loads Landsat imagery from Landsat 7 for multiple years and computes relevant indices.
2. **Temporal Analysis**: Visualize temporal trends in mangrove health using mean index values over time. The model aggregates index values for each year and plots temporal trends.
3. **Interactive Dashboard**: Explore satellite imagery and mangrove trends through the interactive dashboard. The dashboard allows users to interactively visualize Landsat imagery and mangrove indices.

## Landsat Imagery Analysis

The Green Roots AI Model utilizes Landsat satellite imagery for vegetation analysis. It loads Landsat imagery for multiple years and computes the Normalized Difference Vegetation Index (NDVI) to assess vegetation health. The following Landsat imagery datasets are loaded:

- Landsat 1999
- Landsat 2004
- Landsat 2009
- Landsat 2014
- Landsat 2018

Exported the NDVI images to Google Drive and plotted a time series of mean NDVI values over the years.

## Model Overview
Train a RandomForestRegressor model to predict NDVI for upcoming years and visualized the original NDVI data alongside the predictions.
Setting up a machine learning pipeline for classifying mangrove areas using remote sensing data, specifically NDVI (Normalized Difference Vegetation Index) imagery.
Setting up a neural network model for classification using TensorFlow and preparing your training data.


## Contributing

Contributions to the Green Roots AI Model are welcome! If you'd like to contribute to the development of the model, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions regarding the Green Roots AI Model, feel free to contact the project owner at [greenroots@example.com](mailto:greenroots@example.com).

Thank you for your interest in Green Roots! We hope it contributes to environmental conservation efforts through advanced satellite imagery analysis and monitoring of mangroves.
