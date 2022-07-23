
file = "SettingParameter.csv"
try:
    myfile = open(file, 'r', encoding="utf-8")
    myline = myfile.readline()
    while myline:
        print(myline)
        myline = myfile.readline()
    myfile.close()
except IOError as e:
    print("I/O error({0}) : {1}".format(e.errno, e.strerror))
