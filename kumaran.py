


import mysql.connector
c=mysql.connector.connect(host='localhost',user='root',password='cumshotbiju',database='peaky')
curs=c.cursor()

#curs.execute("create table seller(seller_name varchar(20),password varchar(20),no int)")
#curs.execute("create table buyer(buyer_name varchar(20),password varchar(20))")
#curs.execute("create table details(car_model varchar(20),yom int,fuel varchar(20),price int,no int)")

c.commit()
def signup():
        print("if you want to signup as seller press 2")
        print("if you want to signup as buyer press 1")
        b=int(input())
        
        if b==2:
                sellername=input("please enter your name")
                password=input("enter your password")
                curs.execute("Select * from seller where seller_name='{}' and password='{}'".format(sellername,password))
                test=curs.fetchall()
                if test ==[]:
                 f=open("jeep.txt",'r')
                 s1=int(f.read())
                 s2=s1+1
                 f.close()
                 g=open("jeep.txt",'w')
                 s3=str(s2)
                 g.write(s3)
                 g.close()
                 curs.execute("insert into seller values('{}','{}','{}')".format(sellername,password,s1))
                 c.commit()
               
                
                 print("HI USER , YOU ARE SUCCESSFULLY LOGGED IN")
                 print("----------------------DETAILS PAGE---------------------")
                 v5=int(input("enter the number of cars you want to sell"))
                 for i in range(v5):
                          v1=input("enter your car's model")
                          v2=int(input("enter the year of manufacture of your car"))
                          v3=input("enter the fuel type")
                          v4=int(input("enter the price"))
                 curs.execute("insert into details values('{}','{}','{}','{}','{}')".format(v1,v2,v3,v4,s1))
                 c.commit()

                 print("we will connect you with the best buyers in the world")

                else:
                    print("the user with same password and username exist")
                    

                        
def logins():
        n1=input("enter the username")
        n2=input("enter the password")
        curs.execute("select * from seller where seller_name='{}' and password='{}'".format(n1,n2))
        result=curs.fetchall()
        if result==[]:
         print("This user does not exist")
        else:
                for i in result:
                        print("The car you wanted to sell is : ",i[1])
                        print("year of manufacture is : ",i[2])
                        print("The fuel type is : ",i[3])
        c.commit()
        
       
def loginb():
    v1=input("enter the username")
    v2=input("enter the password")
    curs.execute("select * from buyer where buyer_name='{}' and password='{}'".format(v1,v2))
    result=curs.fetchall()
    if result==[]:
            print("This buyer does not exist")
    else:
            curs.execute("select * from seller")
            vi=curs.fetchall()
            for i in vi:
                    print("car owner : ",i[0])
                    print("car model : ",i[1])
                    print("year of manufacture : ",i[2])
                    print("fuel type : ",i[3])
                    print("---------------------------------------------------------------------------------")
                            
            
            
    
    
def mainscreen():
    print("    **********MENU**********    ")
    print("    1 # signup                            ")
    print("    2# login as seller                    ")
    print("    3# login as buyer                    ")
    print("    4# exit                                  ")
    a=int(input())
    if a==1:
        signup()
    elif a==2:
        logins()
    elif a==3:
        loginb()
    elif a==4:
        exit()

mainscreen()




