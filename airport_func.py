import csv

#  finds airport name given an ident code
def get_city_from_ident(ident):
    with open("airports.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            #  checks each row for ident code
            if row[1] == ident:
                #  returns municipality name once ident code has been found
                return row[10]
    return ""

#  finds airport name given an airport name
def get_city_from_name(airport_name):
    with open("airports.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[3] == airport_name:
                return row[10]
    return ""
