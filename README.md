# Avalanche Prediction
Objective: Predicting avalanche danger ratings with weather data in the Sea to Sky corridor.

Avalanche danger rating as labeled by [Avalanche Canada](https://www.avalanche.ca/map/forecasts/sea-to-sky) in Alpine/Treeline/Below Treeline

## Modus Operandi

Weather data is gathered from weather stations in the Sea to Sky Corridor. See /data_gathering/

We use the data to generate an image that represents the the temperature + precipitation over the past 30 days. The images are fed into a convolutional neural network to predict the avalanche rating.

### Generating Images
This repository contains the weather data and avalanche rating CSV files in /data/

Copy the template folders in /data/temp_prec_images/ and rename them without "Template". For example, "Treeline Template" -> "Treeline"

Run /data_gathering/temp_precip_images.ipnyb in Jupyter Notebooks to create images. They will be saved in the folders you just created, organized by avalanche ratings.

### Training a Conv Net
Run /models/convNet_classifier.ipynb or a newer model if it exists.