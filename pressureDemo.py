from sense_hat import SenseHat
import time
#import pyodbc


#server = '<server>.database.windows.net'
#database = '<database>'
#username = '<username>'
#password = '<password>'
#driver= '{ODBC Driver 17 for SQL Server}'
#cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()
#cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
#row = cursor.fetchone()
#while row:
#    print (str(row[0]) + " " + str(row[1]))
#    row = cursor.fetchone()


sense = SenseHat()
sense.clear()



while True:
    pressure = sense.get_pressure()
    pressure = round(pressure,1)
    print(pressure)
    sense.show_message(str(pressure))
    time.sleep(5)
