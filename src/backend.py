
def insert1(lt):

 import mysql.connector as sql

 mycon = sql.connect(host="localhost", user="root", passwd="nikjan09578", database="firstcodes")
 if mycon.is_connected() == False:
   print("error")


 cursor = mycon.cursor()
 e="delete from project"
 cursor.execute(e)

 for i in lt:
         print(i[0],i[1])
         a="select count(*) from project where app='{}'".format(i[0])
         cursor.execute(a)
         row=cursor.fetchone()

         if row[0] == 0:
             q="insert into project values('{}',{})".format(i[0],i[1])
             cursor.execute(q)
             mycon.commit()

         if row[0] != 0:
             r="update project set time={} where app='{}'".format(i[1],i[0])
             cursor.execute(r)
             mycon.commit()


 a='update project set time=time/60'
 cursor.execute(a)
 mycon.commit()
 cursor=mycon.cursor()
 c1="select count(*) from weekly_use"
 cursor.execute(c1)
 s1=cursor.fetchone()

 if s1[0]==7:
    c2="delete from weekly_use"
    cursor.execute(c2)
    mycon.commit()

    c3="select dayname(sysdate())"
    cursor.execute(c3)
    s3=cursor.fetchone()
    v1=s3[0]     #dayname is stored(string)

    c4="select sum(time) from project"
    cursor.execute(c4)
    s4=cursor.fetchone()
    v2=s4[0]  #total time for the day is stored(floating point number)

    c5="insert into weekly_use values('{}',{})".format(v1,v2)
    cursor.execute(c5)
    mycon.commit()


 else:
    c3 = "select dayname(sysdate())"
    cursor.execute(c3)
    s3 = cursor.fetchone()
    v1 = s3[0]  # dayname is stored

    c4 = "select sum(time) from project"
    cursor.execute(c4)
    s4 = cursor.fetchone()
    v2 = s4[0]  # total time for the day is stored

    c5 = "insert into weekly_use values('{}',{})".format(v1, v2)
    cursor.execute(c5)
    mycon.commit()












#thread = threading.Thread(target=run)
   #thread.start()














'''def pausetime():
    times1= {}
    timestamp1 = {}

    while True:
        ca = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe","")
        ca = str(ca)
        ca = ca.strip()
        timestamp1[ca] = int(time.time())
        time.sleep(10)
        if ca not in times1.keys():
            times1[ca] = 0
        times1[ca] = (times1[ca] + int(time.time()) - timestamp1[ca])
        ls=times.items()
        tb=list(ls)

        li = times1.items()
        l2 = list(li)

        for i in l2:
            if i[0] == l1[[0]]'''









'''cursor=mycon.cursor()
s="select * from project"
cursor.execute(s)
new= cursor.fetchall()
for j in new:
    print(j)'''





''''
##applying background
bg=PhotoImage(file = "C:/Users/nikja/OneDrive/Pictures/Screenshots/pythonimage.png")
l= Label(root, image=bg)
l.place(x=0,y=0,relwidth=1,relheight=1)

  OR JUST USE A STANDARD BG COLOUR.......FIRST DO THE IMPORTANT PART.....DO THIS LATER
'''



