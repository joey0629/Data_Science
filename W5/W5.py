import pandas as pd
data = pd.read_csv('data.csv')
final = [['High school system','Gender','Num of graduates','Num of enroll in police university','Num of enroll police college','average num of enroll in military school','Police university rate','Police college rate','Military school enrollment rate']]
def countnum_of_graduates(data,system,gender):
    sum = 0
    for i in range(0, 30):
        if data['High school system'][i] == system and data['Gender'][i] == gender:
            sum = sum + data['Num of graduates'][i]
    return sum
def countnum_of_police_uni(data,system,gender):
    sum = 0
    for i in range(0, 30):
        if data['High school system'][i] == system and data['Gender'][i] == gender:
            sum = sum + data['Num of enroll in police university'][i]
    return sum
def countnum_of_police_coll(data,system,gender):
    sum = 0
    for i in range(0, 30):
        if data['High school system'][i] == system and data['Gender'][i] == gender:
            sum = sum + data['Num of enroll in police college'][i]
    return sum
def countnum_of_system(data,system,gender):
    sum  = 0
    for i in range(0, 30):
        if data['High school system'][i] == system:
            sum = sum + 1
    return sum
def countavg_of_military_school(data,system,gender):
    sum = 0
    total = 0
    for i in range(0, 30):
        if data['High school system'][i] == system and data['Gender'][i] == gender:
            sum = sum + data['Num of enroll in military school'][i]
    n = countnum_of_system(data,system,gender)
    total = round(sum / n,2)
    return total
def countpolice_uni_rate(data,system,gender):
    total = countnum_of_police_uni(data,system,gender)
    n = countnum_of_graduates(data,system,gender)
    return round(total/n,2)*100
def countpolice_coll_rate(data,system,gender):
    total = countnum_of_police_coll(data,system,gender)
    n = countnum_of_graduates(data,system,gender)
    return round(total/n,2)*100
def countnum_of_mili_school(data,system,gender):
    sum = 0
    for i in range(0, 30):
        if data['High school system'][i] == system and data['Gender'][i] == gender:
            sum = sum + data['Num of enroll in military school'][i]
    return sum
def countmili_school_rate(data,system,gender):
    total = countnum_of_mili_school(data,system,gender)
    n = countnum_of_graduates(data,system,gender)
    return round(total/n,2)*100
systems  = ['National','county & city','private']
genders = ['male','female']
for system in systems:
    for gender in genders:
        temp = []
        temp.append(system)
        temp.append(gender)
        temp.append(countnum_of_graduates(data,system,gender))
        temp.append(countnum_of_police_uni(data,system,gender))
        temp.append(countnum_of_police_coll(data,system,gender))
        temp.append(countavg_of_military_school(data,system,gender))
        temp.append(str(countpolice_uni_rate(data,system,gender))+'%')
        temp.append(str(countpolice_coll_rate(data,system,gender))+'%')
        temp.append(str(countmili_school_rate(data,system,gender))+'%')
        final.append(temp)
final= pd.DataFrame(final)
print(final)
