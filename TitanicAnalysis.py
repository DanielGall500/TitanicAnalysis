import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

titanic_data = read_csv('C:/Users/dano/Desktop/TitanicData.csv')

#Questions to ask:
#What factors made people more likely to survive?