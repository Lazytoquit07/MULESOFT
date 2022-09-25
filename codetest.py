import sqlite3 as sql
connection = sql.connect("dabaseMovies.db")
pointer = connection.cursor()
print("INSIDE THE DATABASE")
pointer.execute("INSERT INTO MOVIES VALUES('Jon Watts','Spider-Man: Homecoming','Tom Holland','Zendaya',,2017)")
pointer.execute("INSERT INTO MOVIES VALUES('Spider-Man: Far From Home','Tom Holland','Zendaya','Jon Watts',2019)")
pointer.execute("INSERT INTO MOVIES VALUES('Zendaya','Jon Watts'Spider-Man: No Way Home','Tom Holland',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Shang-Chi and the Legend of the Ten Rings','Simu Liu','Awkwafina','Destin Daniel Cretton',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Dune','Timothée Chalamet','Rebecca Ferguson','Denis Villeneuve',2021)")

allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("END")
print("FOR THE LIST OF ACTORS*")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Jon Watts'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("THANKYOU")
  