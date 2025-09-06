import csv
path = '..\\data\\products.csv'
products = {
    'name':'cokezero',
    'price': 1
}

def read_csv():
    with open(path,'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            print(row)

def write_csv():
    with open(path, 'a')as file :
        key = ['name','price']
        csv_writer = csv.DictWriter(file, fieldnames=key)
        for each in products:
            csv_writer.writerow(each)

read_csv()
write_csv()


        

   