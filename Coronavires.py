# <----- Import Pandas ----->
import pandas as pd

# <----- Data Read in CSV File ----->
df = pd.read_csv("coronavires.csv")

print("<----- The Head of DataFrame ----->")
print(df.head())       # First 5 rows

print("<----- The Tail of DataFrame ----->")
print(df.tail())       # Last 5 rows

print("<----- The Shape of DataFrame ----->")
print(df.shape)      # (rows, columns)

print("<----- The Summary info of DataFrame ----->")
print(df.info())       # Summary info

print("<----- The Statistics of DataFrame ----->")
print(df.describe())   # Statistics (mean, std, min, max, etc.)

print("<--- The Column names --->")
print(df.columns)      # Column names

print("<--- The Index values --->")
print(df.index)      # Index values

fill_num = [
    "total_deaths",
    "total_recovered",             
    "active_cases",                
    "serious_or_critical",
    "total_deaths_per_1m_population",
    "total_tests",                   
    "total_tests_per_1m_population"
]

# --> chune hue columns mein sabhi 'NaN' (Not a Number/Missing) values ko 0 se badal dein
df1 = df[fill_num] = df[fill_num].fillna(0)

# --> Count in missing value
print("--> The Analysis in Count in missing value <--")
print(df1.isnull().sum())

# --> Count in all the column missing value
print("--> Count in all the column missing value <--")
print(df.isnull().sum())



# --> The Analysis Country of Population on Highest
print("--> The Analysis Country of Population on Highest <--")
print(df1.iloc[df["population"].idxmax()]) 

# --> The Analysis Country of Population on Lowest
print(" --> The Analysis Country of Population on Lowest <--")
print(df1.iloc[df["population"].idxmin()]) 

# --> The Analysis Country of total_deaths Highest
print(" --> The Analysis Country of total_deaths Highest <--")
print(df1.iloc[df["total_deaths"].idxmax()]) 

# --> The Analysis Country of total_deaths Lowest
print(" --> The Analysis Country of total_deaths Lowest <--")
print(df1.iloc[df["total_deaths"].idxmin()]) 


all_column = [
    'total_confirmed', 'total_deaths',
    'total_recovered', 'active_cases',
    'serious_or_critical','total_cases_per_1m_population',
    'total_deaths_per_1m_population','total_tests', 
    'total_tests_per_1m_population', 'population'
    ]

# <--- The Analysis of All Columns Highest --->
print( "<--- The Analysis of All Columns Highest --->")

# <--- The Analysis of All Columns Lowest --->
# Note : The Numerical Highest and lowest Check
top_5_deficit = df.sort_values(by=all_column, ascending=False).head(5)


top_5_deficit1 = df.sort_values(by=all_column, ascending=True).head(5)

print("Top All Column")
print("--------------------------------------------------")

print(top_5_deficit)
print( "<--- The Analysis of All Columns Lowest --->")
print(top_5_deficit1)
df1.to_csv("Coronavirus-Data-Analysis/Clean_Data.csv",index=False)