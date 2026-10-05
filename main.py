#Εισάγω την βιβλιοθήκη pandas και τα δεδομένα που βρίσκονται στο αρχείο Excel μου
import pandas as pd 
df = pd.read_csv(
      "World_Energy_By_Country_And_Region_1965_to_2023.csv"
)

#Δώσαμε εντολή να εμφανιστεί η λέξη Shape και στη συνέχεια ζητήσαμε να διαβάσει το μέγεθος του πίνακα 
#print("Shape:")
#print(df.shape)

#print()

#Αντίστοιχα με πριν και ζητάμε να μας διαβάσει ποιες είναι οι στήλες του πίνακα
#print("Columns:")
#print(df.columns)

#print()

#Μετατρέπουμε ανάλογα με τις μεταβλητές που επιλεγουμε να έχουμε για στήλες και παίρνουμε στην ουσία για καθε χώρα , στο κάθε έτος, την αντίστοιχη τιμή ενέργειας
long_df= df.melt(
  id_vars="Country",
  var_name="Year",
  value_name="Energy"
  )
print(long_df)

#Καθαρισμός δεδομένων
# Με την εντολη pd.to_numeric μετατρέπω μια στήλη του data frame που εχει ανγνωριστεί ως κείμενο σε αριθμητικό τύπο και η εντολή errors="coerse" , κάνει NaN οτιδήποτε δεν μπορεί να γραφεί σαν αριθμός
long_df["Year"] = pd.to_numeric(long_df["Year"], errors="coerce") 


long_df["Energy"] = pd.to_numeric(long_df["Energy"], errors="coerce")

long_df = long_df.dropna() #Διαγράφει τις τιμές NaN:=not a number

#print(long_df)

import seaborn as sns
import matplotlib.pyplot as plt

top_2023 =(
long_df[long_df["Year"] == 2023]
.sort_values("Energy", ascending=False)
.head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
data=top_2023,
x="Energy",
y="Country"
)

plt.title("Top Energy Consumers in 2023")

plt.savefig("Graph/pg1",dpi=100,bbox_inches='tight')

plt.show()

world = long_df[long_df["Country"] == "Total World"]

plt.figure(figsize=(12,6))

sns.lineplot(data=world,x="Year",y="Energy")

plt.title("Global Energy Consumption Over Time")

plt.savefig("Graph/pg2",dpi=100,bbox_inches='tight')

plt.show()

comparison = long_df[long_df["Country"].isin(["China", "US"])]
plt.figure(figsize=(12,6))

sns.lineplot(data=comparison,x="Year",y="Energy",hue="Country")

plt.title("China vs US Energy Consumption")

plt.savefig("Graph/pg3",dpi=100,bbox_inches='tight')
plt.show()

def growth(country):

  data = (long_df[long_df["Country"] == country].sort_values("Year"))

  first = data["Energy"].iloc[0]
  last = data["Energy"].iloc[-1]

  return round(((last - first) / first) * 100,2)
print("China:", growth("China"), "%")
print("India:", growth("India"), "%")
print("US:", growth("US"), "%")