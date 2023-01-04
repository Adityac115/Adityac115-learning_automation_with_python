import csv

def create_fil(file):
    with open(file,'w') as f:
        f.write("name,color,type\n")
        f.write("carnation,pink,annual\n")
        f.write("daffodil,yellow,perennial\n")
        f.write("iris,blue,perennial\n")
        f.write("poinsettia,red,perennial\n")
        f.write("sunflower,yellow,annual\n")

def create_csv(filename):
    return_string=""
    create_fil(filename)
    with open(filename,'r') as f:
        rows=csv.reader(f)
        line=0
        for row in rows:
            if line==0:
                return_string+=f' {row[0]} ,{row[1]}, {row[2]}\n'
                line+=1
            else:
                return_string+=f'a {row[0]} {row[1]} is {row[2]}\n'
                line+=1
    return return_string

print(create_csv("./csv_files/flowers.csv"))