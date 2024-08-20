import mysql.connector
mydb=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Abhinavsn@56',
    database = 'list1'
    )
mycursor = mydb.cursor()
def list1():
    mycursor.execute('select * from menu1')
    result = mycursor.fetchall()
    for row in result:
        print("Id",row[0],"Name",row[1],"Age",row[2],"Salary",row[3])
def add():
    id = int(input("Enter the id :"))
    name = input("Enter the name: ")
    Age = int(input("Enter the Age: "))
    sal = int(input("Enter the salary: "))
    sql = "insert into menu1 values(%s,%s,%s,%s)"
    val = (id,name,Age,sal)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Employees added succesfully!!!!!")
def edit():
    id = int(input("Enter the id :"))
    name = input("Enter the name: ")
    Age = int(input("Enter the Age: "))
    sal = int(input("Enter the salary: "))
    sql = "update data set name=%s,Age=%s,sal=%s where id=%s"
    val = (id,name,Age,sal)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Edited succesfully!!!!!!")
def delete():
    id = int(input("Enter the id :"))
    
    mycursor.execute('delete from menu1 where id=%s',(id,))
    mydb.commit()
    print("Employee deleted succesfully")
c=6
while c!=5:
    print("--------------------------------------------")
    c=int(input("Please select your input\n1.List\n2.Add\n3.Edit\n4.Delete\nSelect your choice: "))
    if c==1:
        list1()
    elif c==2:
        add()
    elif c==3:
        edit()
    elif c==4:
        delete()
    else:
        print("Wrong command")
