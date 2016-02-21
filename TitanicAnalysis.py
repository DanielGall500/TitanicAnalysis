import unicodecsv
import numpy as np

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

titanic_data = read_csv('C:/Users/dano/Desktop/TitanicAnalysis-master/TitanicData.csv')

#Data Columns: PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

titanic_survivors = np.array([])

titanic_non_survivors = np.array([])

for person in titanic_data:
    if (person['Survived'] == '1'):
        titanic_survivors = np.append(titanic_survivors, person)
    else:
        titanic_non_survivors = np.append(titanic_non_survivors, person)
        
print "Survivors: " + str(len(titanic_survivors))

print "Non-Survivors: " + str(len(titanic_non_survivors))

def findAvg(listData, column):
	output_list = []
	for data in listData:

		column = data[column]

		if(column == '' or column == ''):
			continue
		else:
			output_list.append(float(column))
		return sum(output_list) / len(output_list)


print "Average age of a passenger: " + str((findAvg(titanic_data, 'Age'))) + "\n"
print "Average age of a survivor: " + str((findAvg(titanic_survivors, 'Age'))) + "\n"
print "Average age of a non-survivor: " + str((findAvg(titanic_non_survivors, 'Age'))) + "\n"





