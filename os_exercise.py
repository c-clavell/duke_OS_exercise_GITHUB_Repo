


import os
from turtle import clear
from local_path import pathX
import sqlite3




def walkOS(path):

     for root,dir,files in os.walk(path):

        # print(dir)
        # print("files: ",files,pathX)

        if len(files) >0:

            for _file in files:
                absolute_path= os.path.join(root,_file)
                size=os.path.getsize(absolute_path)

                name, extension = os.path.splitext(absolute_path)  #get the type of file

                #print(f"file path: {absolute_path}  ", f"Size: {size}")
                list1.append([_file,extension,size/1000000])

                dict1[_file] = size /1000000   ##size in megabytes

        if len(dir) > 0:
            for i in dir:
                pathxx=os.path.join(root, i)
                walkOS(pathxx)              ##### recursive call

            
        break






if __name__ == "__main__":
    #main()
    dict1={}
    list1=[]

    q1="CREATE TABLE files (id INTEGER primary key, name TEXT, type TEXT, size FLOAT)"
    q2="INSERT INTO files(name,type,size) VALUES (?,?,?)"
    q3="SELECT id,name, MAX(size) FROM files" 
    q4="SELECT id,name, MIN(size) FROM files"
    q5="SELECT * from files WHERE type = ?"
    q6="SELECT * FROM files ORDER BY size DESC"
    q7="SELECT DISTINCT type FROM files"
    q8="SELECT COUNT(*) FROM files"
    q9="SELECT type, COUNT(type) FROM files GROUP BY type ORDER BY size DESC"

    walkOS(pathX)

    # for k,v in dict1.items():
    #     print(k,v)

    # print(list1)

    if len(list1)>0:
        conn=sqlite3.connect(':memory:')
        cursor=conn.cursor()

        cursor.execute(q1)
        conn.commit()

        for i in list1:
            cursor.execute(q2,i)
            conn.commit()

        cursor.execute(q3)
        maxx=cursor.fetchone()
        
        cursor.execute(q4)
        minn=cursor.fetchone()

        cursor.execute(q9)
        types=cursor.fetchall()

        count=cursor.execute(q8).fetchone()

        # print("max:",maxx,"minn:",minn)
        # print("types:",types)

        print(f"""
RESULTS:
Number of files: {count[0]}
Largest File: {str(maxx[1])+"  "+ str(maxx[2])}MB
Smallest File: {str(minn[1])+"  "+str(minn[2])}MB
Type of files found: {types}

        """)