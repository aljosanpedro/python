# sample input: 2.50,4 1.25,3 1.25,3 1.00,3 1.00,3
# result: 1.46

class Subject:
    def __init__(self, grade, unit):
        self.grade = grade
        self.unit = unit

    def calculate_weight(self):
        return self.grade * self.unit

def main():
    data = input("Data [grade1,unit1 grade1,unit2 ...]: ")    

    totals = calculate_totals(data)

    gwa = calculate_gwa(totals)
    print("GWA:", gwa)
    
def calculate_totals(data):
    pairs = data.split(' ')
    
    weights,units = [],[]
    for pair in pairs:
        grade,unit = pair.split(',')
        grade,unit = float(grade),int(unit)

        subject = Subject(grade, unit)

        weight = subject.calculate_weight()
        weights.append(weight)

        units.append(unit)

    totals = {"weights":weights, "units":units}

    return totals

def calculate_gwa(totals):
    total_weight = sum(totals["weights"])
    total_units = sum(totals["units"])

    gwa = total_weight/total_units
    gwa = round(gwa,3)

    return gwa

if __name__ == '__main__':
    main()