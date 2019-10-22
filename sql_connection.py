import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password='ardit700_student',
    host='108.167.140.122',
    database='ardit700_pm1database'
)

cursor = con.cursor()
consulta = input('Dame una palabra: ')
# con %s y un % al final defines el valor de %s
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression ='%s' " % consulta)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print('Sin resultados')
