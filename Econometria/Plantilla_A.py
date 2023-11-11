"""
1. Escribir el Modelo
2. El modelo es adecuado → Estadistico + prueba + conclusion
3. Determina si la relación entre Y y X no depende del factor (colinealidad)
4. Determina si existen problemas de heterocedasticidad
5. Determine la forma en que causa la desviacion tipica del error (interpreta valores)
"""

from numpy import mean
import pandas as pd
import statsmodels.api as sm

from utilities import backward_elimination


# Load the CSV file
file_path = "Econometria/MRL016-1.csv"
data = pd.read_csv(file_path)

# print(data.head())  # print the first 5 rows to see the data for building the model

# Define all the variables:

# Creating dummy variables for the 'NPROV' column
dummies = pd.get_dummies(
    data["NPROV"], drop_first=True
)  # drop_first=True to get K-1 dummies out of K categorical levels by removing the first one which is redundant

data = data.drop(["NPROV"], axis=1)  # drop the 'NPROV' column

# print(dummies.head())

data["CASTELLON"] = dummies["CASTELLÓN"] * 1  # interaction variable
data["VALENCIA"] = dummies["VALENCIA"] * 1  # interaction variable

# Define all the variables:
data["EMPLEOS_AGR_centered"] = data["EMPLEOS_AGR"] - mean(
    data["EMPLEOS_AGR"]
)  # variable independiente

data["EMPLEOS_CASTELLON"] = (
    data["EMPLEOS_AGR"] * dummies["CASTELLÓN"]
)  # interaction variable
data["EMPLEOS_VALENCIA"] = (
    data["EMPLEOS_AGR"] * dummies["VALENCIA"]
)  # interaction variable

# model_data = pd.concat([data, dummies])  # concatenate the data and dummies dataframes

X = data[
    [
        "EMPLEOS_AGR_centered",
        "CASTELLON",
        "VALENCIA",
        "EMPLEOS_CASTELLON",
        "EMPLEOS_VALENCIA",
    ]
]  # variables independientes

X = sm.add_constant(X)  # add a constant to the model
y = data["VAA_AGR"]  # variable dependiente

# # Create the model
model = sm.OLS(y, X).fit()  # ordinary least squares model
print(model.summary())  # print the model summary

print("Deleting the non-significant variables:")
new_model = backward_elimination(X, y)

print(new_model.summary())