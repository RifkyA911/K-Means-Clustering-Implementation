
# Measuring City Air Quality Index Using K-means Python-Jupyter

## Overview
This is a simple implementation of the K-Means clustering algorithm using Python through to Jupyter. The program reads data from the `ISPU.csv` file, selects the `pm10` and `pm25` columns, and performs K-Means clustering on the data.


## Acknowledgements

 - [Python 3.x](https://www.python.org/)
 - [NumPy](https://numpy.org/)
 - [pandas](https://pandas.pydata.org/)


## Program Sequential

- **NumPy** and **pandas** are imported for data manipulation and analysis.
- **Read Data:** The program reads data from the "ISPU.csv" file using pandas.

- **Select Columns:** The 'pm10' and 'pm25' columns are selected from the dataset and stored in a new DataFrame.
- **Initialize Centroids:** Initial centroids are randomly selected from the dataset.
- **K-Means Clustering:** The program iteratively performs K-Means clustering. In each iteration, it calculates the Euclidean distance between each data point and the centroids, assigns the data points to the nearest centroid, and recalculates the centroids based on the assigned data points.
- **Print Results:** The program prints the clusters and updated centroids after each iteration.

## Usage/Examples

Ensure that Python and the required libraries are installed on your system.
Clone the repository or download all files.

- (**Recomended**) Run the script `index.ipnyb` using a Python interpreter. you can using [Ananconda](https://www.anaconda.com/) or [Google Colab](https://colab.google/) plaform for running the codes.

- If you want to use Python only, then you must open your terminal wether is `CMD` or `Shell` and just run command below:
#### Bash:

```python
    python index.py
```

The program will read the data from `ISPU.csv` randomly select initial `centroids`, and iteratively perform the K-Means clustering process.

## Result
- The program displays the clusters for each iteration, showing the data points assigned to each centroid.
- The updated centroids are printed after each iteration.
- You can check the example of the record by click this link file :  [**index.ipnyb**](https://github.com/RifkyA911/K-Means-Clustering-Implementation/blob/master/index.ipynb)

## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?

