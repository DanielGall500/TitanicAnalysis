import unicodecsv
import numpy as np

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

titanic_data = read_csv('C:/Users/dano/Desktop/TitanicData.csv')

#Questions to ask:
#What factors made people more likely to survive?

titanic_survivors = np.array([])
titanic_non_survivors = np.array([])

for person in titanic_data:
    if (person['Survived'] == '1'):
        titanic_survivors = np.append(titanic_survivors, person)
    else:
        titanic_non_survivors = np.append(titanic_non_survivors, person)
        
print "Survivors: " + len(titanic_survivors)

print "Non-Survivors: " + len(titanic_non_survivors)

