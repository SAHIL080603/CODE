import mysql.connector as mc
import pymysql
import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
import random as ran
import pygame, sys
from pygame.locals import *
pas=input("Enter the password for the access to MYSQL DATABASE and other information::::")
while True :
    try: 
        print("\t\t\t 1. Create database nations")
        print("\t\t\t 2. Create table of coutries")
        print("\t\t\t 3. Register country ")
        print("\t\t\t 4. Update country")
        print("\t\t\t 5. Delete country")
        print("\t\t\t 6. search county")
        print("\t\t\t 7. statical data of countries (bar graph)")
        print("\t\t\t 8. To update country`s crucial data")
        print("\t\t\t 9. Country`s net inflow and GDP and area (bar graph)")
        print("\t\t\t 10.Alter table countries")
        print("\t\t\t 11.QUIT")
        p=int (input("\t\tEnter Your Choice :"))
        if p==1:           #CREATING DATABASE
            a=ran.randint(10000000,99999999)
            l=str(a)
            f=open("DOCPASS.txt",'w+')
            f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
            f.write(l)
            f.flush()
            f.close()
            print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
            i=int(input("\n\t\t\t Enter the PASSWORD:::::"))
            if a==i:
                while True:
                    try:
                        mydb=mc.connect(host="localhost",user="root",passwd=pas)
                        mycursor=mydb.cursor()
                        a="create database nations"
                        mycursor.execute(a)
                        print('\t\t\t SUCCESSFULLY CREATED DATABASE NATIONS :)')
                        break
                    except :
                        print('\t\t\t DATABASE ALREADY EXIST ;)')
                        print("")
                        break
            else:
                break
        
        if p==2:
            a=ran.randint(10000000,99999999)
            l=str(a)
            f=open("DOCPASS.txt",'w+')
            f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
            f.write(l)
            f.flush()
            f.close()
            print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
            i=int(input("\n\t\t\t Enter the PASSWORD:::::"))
            if a==i:
                while True:
                    try:
                        mydb=mc.connect(host="localhost",user="root",passwd=pas,database="nations")
                        mycursor=mydb.cursor()
                        mycursor.execute("use nations")
                        print(" Creating countries table")
                        sql = "CREATE TABLE countries(pcode char(6) PRIMARY KEY,cname char(30) NOT NULL,currency varchar(8) NOT NULL ,area float(12,2),population integer(30) ,continent varchar(30) NOT NULL,credit float(30,3),debt float(30,2),import float(85,2),export float(85,2),capital varchar(85) NOT NULL,avg_private_consumption float(15,2));"
                        mycursor.execute(sql)
                        print("succesfully created table countries")
                        break
                    except:
                        print("\t\t\t Table Countries already exist")
                        print("")
                        break
            else:
                break
        if p==3:          #registration to countries
            a=ran.randint(10000000,99999999)
            l=str(a)
            f=open("DOCPASS.txt",'w+')
            f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
            f.write(l)
            f.flush()
            f.close()
            print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
            i=int(input("\n\t\t\t Enter the PASSWORD:::::"))
            if i==a:
                mydb=mc.connect(host="localhost",user="root",passwd=pas,database="nations")
                mycursor=mydb.cursor()
                code=input("\t\tEnter  pcode :")
                search="SELECT count(*) from countries WHERE pcode='%s'"%(code)
                val=(code)
                mycursor.execute(search)
                for x in mycursor:
                    cnt=x[0]
                    if cnt==0:
                        name=input("Enter countries name :")
                        currency=(input("Enter country currency :"))
                        area=float(input("Enter country`s area :"))
                        pop=int(input("Enter population of your country:"))
                        cat=input("Enter continent :")
                        cre=float(input("Enter the country`s credit:"))
                        deb=float(input("Enter the country`s debt:"))
                        imp=float(input("Enter the new amount of import:"))
                        export=float(input("Enter the new amount of export:"))
                        avg_=float(input("Enter new consumption per head:"))
                        mycursor.execute("INSERT INTO countries values ('{}','{}','{}',{},{},'{}',{},{},{},{},{})".format(code,name,currency,area,pop,cat,cre,deb,inp,export,avg_))
                        mydb.commit()
                        print("Succesfully wrote data of your country into the countries table...")
                        print("")
                    else:
                        print("\t\t country already exist")
                        print("")
            else:
                break
            
            if p==4:              #update_country()
                a=ran.randint(10000000,99999999)
                l=str(a)
                f=open("DOCPASS.txt",'w+')
                f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
                f.write(l)
                f.flush()
                f.close()
                print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
                i=int(input("\n\t\t\t Enter the PASSWORD:::::"))
            if i==a:
                mydb=mc.connect(host="localhost",user="root",passwd=pas,database="nations")
                mycursor=mydb.cursor()
                code=input("Enter the pincode or zipcode code of the country you want to update :")
                credit=float(input("Enter the new credit :"))
                debt=float(input("Enter the new debt:"))
                pop=int(input("Enter the latest population:"))
                imp=float(input("Enter the new amount of import:"))
                export=float(input("Enter the new amount of export:"))
                avg_=float(input("Enter new consumption per head:"))
                sql="UPDATE countries SET credit={}, debt={}, population={}, import={}, export={}, avg_private_consumption={} WHERE pcode='{}';"
                mycursor.execute(sql.format(credit,debt,pop,imp,export,avg_,code))
                mydb.commit()
                print("\t\t country`s details updated")
                print(mycursor.rowcount," record(s) updated")
            else:
                break
    
        if p==5:               #delete_country
             a=ran.randint(10000000,99999999)
             l=str(a)
             f=open("DOCPASS.txt",'w+')
             f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
             f.write(l)
             f.flush()
             f.close()
             print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
             i=int(input("\n\t\t\t Enter the PASSWORD:::::"))
             if i==a:
                 mydb=mc.connect(host="localhost",user="root",passwd=pas,database="nations")
                 mycursor=mydb.cursor()
                 code=input("Enter the country`s pincode or zipcode:")
                 sql="DELETE FROM countries WHERE pcode = '{}';"
                 mycursor.execute(sql.format(code))
                 mydb.commit()
                 print(mycursor.rowcount," record(s) deleted")
             else:
                 break
        if p== 6 :
            a=ran.randint(10000000,99999999)
            l=str(a)
            f=open("DOCPASS.txt",'w+')
            f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
            f.write(l)
            f.flush()
            f.close()
            print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
            i=int(input("\t\t\t Enter the PASSWORD:::::"))
            if i==a:
                mydb=mc.connect(host="localhost",user="root",passwd=pas,database="nations")
                mycursor=mydb.cursor()
                while True:
                    try:
                        print("\t\t\t 1. List all countries")
                        print("\t\t\t 2. List country pincode wise")
                        print("\t\t\t 3. List country continent wise")
                        print("\t\t\t 4. Back (Main Menu)")
                        s=int (input("\t\tEnter Your Choice :"))
                        if s==1 :
                            sql="SELECT * FROM countries order by cname;"
                            mycursor.execute(sql)
                            data=mycursor.fetchall()
                            cont=mycursor.rowcount
                            print("\t\tTotal number of rows retrived in data is ",cont)
                            for row in data:
                                print(row)
                            else:
                                print("No other data found")
                        if s==2 :
                            code=input(" Enter pincode or zipcode code :")
                            mycursor.execute("SELECT * FROM countries WHERE pcode='{}'".format(code))
                            data=mycursor.fetchall()
                            cont=mycursor.rowcount
                            print("\t\tTotal number of rows retrived in data is ",cont)
                            for row in data:
                                print(row)
                            else:
                                print("No other data found")
                        if s==3 :
                            cat=input("Enter continent :")
                            mycursor.execute("SELECT * FROM countries WHERE continent='{}'".format(cat))
                            data=mycursor.fetchall()
                            cont=mycursor.rowcount
                            print("\t\tTotal number of rows retrived in data is ",cont)
                            for row in data:
                                print("\t\t\t\t\t",row)
                            else:
                                print("No other data found")
                        if s== 4 :
                            break
                        while s>4:
                            s=s-s
                            print("\n\t\t\tinvalid input")
                    except:
                        print("\n\t\t\tSomething goofy ")
                        break
                else:
                    break
        
        if p==7:
                a=ran.randint(10000000,99999999)
                l=str(a)
                f=open("DOCPASS.txt",'w+')
                f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
                f.write(l)
                f.flush()
                f.close()
                print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
                i=int(input("\n\t\t\t Enter the PASSWORD:::::"))
                if i==a:
                    mydb=mc.connect(host="localhost",user="root",passwd=pas,database="nations")
                    mycursor=mydb.cursor()
                    while True:
                        try:
                            print("\t\t\t 1.statical data of credits given to world bank")
                            print("\t\t\t 2.statical data of debt taken from world bank")
                            print("\t\t\t 3.statical data of population")
                            print("\t\t\t 4.Back to main menu")
                            s=int(input("\t\t Enter your choice:"))
                            if s==1:
                                sql="select cname,credit from countries;"
                                mycursor.execute(sql)
                                rows=mycursor.fetchall()
                                df = pd.DataFrame([[xy for xy in x] for x in rows])

                                x=df[0]
                                y=df[1]

                                mp.bar(x,y)

                                mp.show() 
                            if s==2:
                                sql="select cname,debt from countries;"
                                mycursor.execute(sql)
                                rows=mycursor.fetchall()
                                df = pd.DataFrame([[xy for xy in x] for x in rows])

                                x=df[0]
                                y=df[1]

                                mp.bar(x,y)

                                mp.show() 
 
                            if s==3:
                                sql="select cname,population from countries;"
                                mycursor.execute(sql)
                                rows=mycursor.fetchall()
                                x.label='countires'
                                df = pd.DataFrame([[xy for xy in x] for x in rows])

                                x=df[0]
                                y=df[1]

                                mp.bar(x,y)

                                mp.show() 

                            if s==4:
                                break
                            while s>4:
                                s=s-s
                                print("\n\t\t\tINVALID INPUT")
                        except:
                            print("\n\t\t\tSomething goofy")
                else:
                    break
        if p==8:
                a=ran.randint(10000000,99999999)
                l=str(a)
                f=open("DOCPASS.txt",'w+')
                f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
                f.write(l)
                f.flush()
                f.close()
                print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
                i=int(input("\n\t\t\t Enter the PASSWORD:::::"))
                if i==a:
                    mydb=mc.connect(host="localhost",user="root",passwd=pas,database="nations")
                    mycursor=mydb.cursor()
                    code=input("Enter the pincode or zipcode code of the country you want to update :")
                    pcode=input("Enter the new pincode of your country::")
                    cname=input("Enter the new country name :")
                    currency=input("Enter the new currency:")
                    area=float(input("Enter the latest area of your country:"))
                    sql="UPDATE countries SET pcode='{}',cname='{}', currency='{}', area={} WHERE pcode='{}';"
                    mycursor.execute(sql.format(pcode,cname,currency,area,code))
                    mydb.commit()
                    print("\t\t country`s details updated")
                else:
                    break
        if p==9:
                a=ran.randint(10000000,99999999)
                l=str(a)
                f=open("DOCPASS.txt",'w+')
                f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
                f.write(l)
                f.flush()
                f.close()
                print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
                o=int(input("\n\t\t\t Enter the PASSWORD:::::"))
                if o==a:
                    while True:
                        try:
                            print("\t\t\t 1.Data of net flow")
                            print("\t\t\t 2.Avrage consumption per head of each country")
                            print("\t\t\t 3.GDP of each country")
                            print("\t\t\t 4.area of countries staical")
                            print("\t\t\t 5.Back to main menu")
                            i=int(input("Enter your choice::"))
                            mydb=mc.connect(host="localhost",user="root",passwd=pas,database="nations")
                            mycursor=mydb.cursor()
                            if i==1:
                                sql="select cname,export-import from countries;"
                                mycursor.execute(sql)
                                rows=mycursor.fetchall()
                                df = pd.DataFrame([[xy for xy in x] for x in rows])

                                x=df[0]
                                y=df[1]

                                mp.bar(x,y)
                                mp.show()

                            if i==2:
                                SQ="select cname,(export-import)/population from countries;"
                                mycursor.execute(SQ)
                                rows=mycursor.fetchall()
                                df = pd.DataFrame([[xy for xy in x] for x in rows])

                                x=df[0]
                                y=df[1]

                                mp.bar(x,y)

                                mp.show()

                            if i==3:
                                so="select cname,(export-import)/avg_private_consumption/100 from countries;"
                                mycursor.execute(so)
                                rows=mycursor.fetchall()
                                df = pd.DataFrame([[xy for xy in x] for x in rows])

                                x=df[0]
                                y=df[1]

                                mp.bar(x,y)

                                mp.show()
        
                            if i==4:
                                so="select cname,area from countries;"
                                mycursor.execute(so)
                                rows=mycursor.fetchall()
                                df = pd.DataFrame([[xy for xy in x] for x in rows])

                                x=df[0]
                                y=df[1]

                                mp.bar(x,y)

                                mp.show()
            
                            if i==5:
                                break
                            while i>5:
                                i=i-i
                                print("\n\t\tinvalid input\n")
                        except:
                            print("\n\t\tSomething goofy")
                else:
                    break
                
        if p==10:
                a=ran.randint(10000000,99999999)
                l=str(a)
                f=open("DOCPASS.txt",'w+')
                f.write("$$@@  your  ## pass to %%%% acess (((())))is::::  ")
                f.write(l)
                f.flush()
                f.close()
                print('\t\t\t your pssword was sent on SAHIL FILES (pendrive) check with name DOCPASS')
                i=int(input("\n\t\t\t Enter the PASSWORD:::::"))
                if i==a:
                    mydb=mc.connect(host="localhost",user="root",passwd=pas,database="nations")
                    mycursor=mydb.cursor()
                    code='1100XX'
                    search="SELECT count(*) from countries WHERE pcode='%s'"%(code)
                    val=(code)
                    mycursor.execute(search)
                    for x in mycursor:
                        cnt=x[0]
                        if cnt==0:
                            code='1100XX'
                            name='INDIA'
                            currency='Rupees'
                            area=3.28 
                            pop=1300000000
                            cat='Asia'
                            cre=99999997952.000 
                            deb=100000000.00
                            imp= 20000000000.00 
                            exp= 54999998464.00 
                            avg_=650000.00
                            capital='New Delhi'
                            mycursor.execute("INSERT INTO countries values ('{}','{}','{}',{},{},'{}',{},{},{},{},'{}',{})".format(code,name,currency,area,pop,cat,cre,deb,imp,exp,capital,avg_))
                            mydb.commit()
                            print("Succesfully wrote data of your country into the countries table...")
                        else:
                            print("\t\t country 1 already exist")
                    code='1010XX'
                    search="SELECT count(*) from countries WHERE pcode='%s'"%(code)
                    val=(code)
                    mycursor.execute(search)
                    for x in mycursor:
                        cnt=x[0]
                        if cnt==0:
                            name='RUSSIA'
                            currency='Ruble'
                            area=17.10 
                            pop=140000000
                            cat='Asia'
                            cre= 86999998464.000
                            deb=200000000.00 
                            imp=20000000000.00 
                            exp= 49999998976.00 
                            avg_=20000000.00
                            capital='Moscow'
                            mycursor.execute("INSERT INTO countries values ('{}','{}','{}',{},{},'{}',{},{},{},{},'{}',{})".format(code,name,currency,area,pop,cat,cre,deb,imp,exp,capital,avg_))
                            mydb.commit()
                            print("Succesfully wrote data of your country into the countries table...")
                        else:
                            print("\t\t country 2 already exist")
                    code='9950XX'
                    search="SELECT count(*) from countries WHERE pcode='%s'"%(code)
                    val=(code)
                    mycursor.execute(search)
                    for x in mycursor:
                        cnt=x[0]
                        if cnt==0:
                            name='USA'
                            currency='US Dollar'
                            area=9.83 
                            pop=327200000
                            cat='North America'
                            cre= 89999998976.000
                            deb=2000000000.00
                            imp=1000000000.00
                            exp= 59999998976.00 
                            avg_=25000000.00
                            capital='Washington D.C.'
                            mycursor.execute("INSERT INTO countries values ('{}','{}','{}',{},{},'{}',{},{},{},{},'{}',{})".format(code,name,currency,area,pop,cat,cre,deb,imp,exp,capital,avg_))
                            mydb.commit()
                            print("Succesfully wrote data of your country into the countries table...")
                        else:
                            print("\t\t country 3 already exist")
                else:
                    break
            

        
        if p==11:
            pygame.init()
            windowSurface = pygame.display.set_mode((900, 800), 0, 32)
            pygame.display.set_caption('NATIONS SERVER')
            BLACK = (0, 0, 0)
            RED =(225, 0, 0)
            BLUE =(0, 0, 225)
            WHITE = (255, 255, 255)
            PURPLE=(225,0,225)
            basicFont = pygame.font.SysFont(None, 78)
            text = basicFont.render('THANKS FOR COMING!! :)', True, WHITE, BLUE )
            textRect = text.get_rect()
            textRect.centerx = windowSurface.get_rect().centerx
            textRect.centery = windowSurface.get_rect().centery

            windowSurface.fill(PURPLE)
            # draw the text's background rectangle onto the surface

            pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
            # get a pixel array of the surface

            pixArray = pygame.PixelArray(windowSurface)

            pixArray[480][380] = BLACK

            del pixArray
            # draw the text onto the surface

            windowSurface.blit(text, textRect)
            # draw the window onto the scre
            pygame.display.update()
            # run the game loop
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit() 
                                      
            
        
        while p>11:
            p=p-p
            print("\n\n\t\t\tINVALID INPUT\n")
    except:
        print("\n\n\t\t\tSOMETHING GOOFY \n PLEASE RESTART THE PROGRAM\n\n")
        break
    