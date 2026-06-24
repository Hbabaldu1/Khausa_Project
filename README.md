# Khausa Weather Prediction System

A machine learning-based weather prediction system developed as a B.Sc Physics final year project at Sule Lamido University, Kafin Hausa. This project uses historical weather data from Kafin Hausa to predict next-day temperatures using various machine learning regression models.

## Project Overview

This project implements and compares multiple machine learning algorithms to forecast daily temperature in Kafin Hausa, Nigeria. The system processes NASA POWER daily weather data and trains three different regression models to determine which approach provides the most accurate predictions.

## Dataset

- **Source**: NASA POWER (Prediction of Worldwide Energy Resources)
- **Location**: Kafin Hausa, Nigeria (Latitude: 12.024°N, Longitude: 9.91°E)
- **Time Period**: January 1, 2000 - January 1, 2026
- **Variables Used**:
  - T2M: Temperature at 2 meters
  - RH2M: Relative Humidity at 2 meters
  - PS: Surface Pressure
  - WS2M_MAX: Maximum Wind Speed at 2 meters

## Features

### Data Processing
- Automated CSV data loading and cleaning
- Conversion of Year + Day-of-Year to standard date format
- Automated target variable creation (next-day temperature)
- Missing value handling

### Machine Learning Models

The project implements and evaluates three regression models:

1. **Linear Regression**
   - Baseline model for comparison
   - Currently commented out but available for testing

2. **Decision Tree Regressor**
   - Non-linear approach to capture complex patterns
   - Currently commented out but available for testing

3. **Random Forest Regressor** (Active Model)
   - Ensemble method with 100 trees
   - Best performance for temperature prediction
   - Currently selected as the primary prediction model

### Evaluation Metrics

- **Mean Absolute Error (MAE)**: Average absolute difference between predicted and actual values
- **Mean Squared Error (MSE)**: Squared differences to penalize larger errors

### Analysis & Visualization

- Feature importance analysis showing which weather variables most influence temperature
- Actual vs. Predicted temperature comparison plots
- Bar charts for feature importance visualization

## Installation

### Requirements
```
Python 3.x
pandas
matplotlib
scikit-learn
```

### Setup
```bash
pip install pandas matplotlib scikit-learn
```

## Usage

1. Place the NASA POWER CSV file in the project directory:
   ```
   POWER_Point_Daily_20000101_20260101_012d24N_009d91E_LST.csv
   ```

2. Run the main script:
   ```bash
   python Khausa_Project.py
   ```

3. The script will:
   - Load and preprocess the weather data
   - Split data into training (70%) and testing (30%) sets
   - Train the Random Forest model
   - Display feature importance results
   - Show visualization plots

## Results

The system outputs:
- Feature importance scores for each weather variable
- Performance metrics (MAE and MSE)
- Visualization comparing actual vs. predicted temperatures
- Feature importance bar chart

## Project Structure

```
Khausa_Project/
├── README.md                    # Project documentation
├── Khausa_Project.py           # Main prediction script
└── POWER_Point_Daily_*.csv     # NASA POWER dataset (not included)
```

## Notes

- The dataset file is not included in the repository and must be downloaded from NASA POWER
- Model training and visualization sections for Linear Regression and Decision Tree are commented out for faster execution
- Uncomment relevant sections to compare all three models
- The Random Forest model is currently optimized for the best balance between accuracy and performance

## Future Enhancements

- Hyperparameter tuning for improved model accuracy
- Cross-validation for more robust evaluation
- Implementation of additional models (e.g., Gradient Boosting, Neural Networks)
- Time series analysis and ARIMA models
- Web interface for real-time predictions
- Extended forecasting (multiple days ahead)

## Author

**Hassan Abdullahi**  
B.Sc Physics  
Sule Lamido University, Kafin Hausa

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Last Updated**: 2026
