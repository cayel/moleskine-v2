from database import add_artist,add_release,add_list,add_list_release

def seed_database():
    add_artist("Nick Cave & The Bad Seeds")
    add_artist("Einstürzende Neubauten")
    add_artist("New Model Army")
    add_artist("The Gun Club")
    
    add_release("From Her To Eternity", "1984-06-01", 1, "https://upload.wikimedia.org/wikipedia/en/3/38/Fromhertoeternity.jpg")
    add_release("The Firstborn Is Dead", "1985-06-03", 1, "https://upload.wikimedia.org/wikipedia/en/6/6b/The_Firstborn_Is_Dead.png")
    add_release("Kicking Against The Pricks", "1986-08-18", 1, "https://upload.wikimedia.org/wikipedia/en/e/e5/Kickingagainstthepricks.jpeg")
    add_release("Your Funeral... My Trial", "1986-11-03", 1, "https://upload.wikimedia.org/wikipedia/en/1/16/Yourfuneralmytrial.jpg")
    add_release("Tender Prey", "1988-09-19", 1, "https://upload.wikimedia.org/wikipedia/en/2/2e/Tenderprey.jpg")
    add_release("The Good Son", "1990-04-17", 1, "https://upload.wikimedia.org/wikipedia/en/f/f4/Thegoodson.jpg")
    add_release("Henry's Dream", "1992-04-27", 1,"https://upload.wikimedia.org/wikipedia/en/f/ff/Henrysdream.jpg")
    add_release("Let Love In", "1994-04-18", 1, "https://upload.wikimedia.org/wikipedia/en/f/f0/Letlovein.jpg")
    add_release("Murder Ballads", "1996-02-05", 1, "https://upload.wikimedia.org/wikipedia/en/5/56/Murderballads.jpg")
    add_release("The Boatman's Call", "1997-03-03",1,"https://upload.wikimedia.org/wikipedia/en/3/31/Nick_cave_and_the_bad_seeds-the_boatman%27s_call.jpg")
    add_release("No More Shall We Part", "2001-04-02",1, "https://upload.wikimedia.org/wikipedia/en/9/99/No_more_shall_we_part_cover.jpg")
    add_release("Nocturama", "2003-02-03",1, "https://upload.wikimedia.org/wikipedia/en/6/6e/Nocturama.jpg")
    add_release("Abattoir Blues / The Lyre of Orpheus", "2004-09-20",1, "https://upload.wikimedia.org/wikipedia/en/2/27/Abattoir_Blues%2BThe_Lyre_of_Orpheus.jpg")
    add_release("Dig, Lazarus, Dig!!!", "2008-03-03",1, "https://upload.wikimedia.org/wikipedia/en/4/42/Nick_Cave_%26_the_Bad_Seeds_-_Dig%2C_Lazarus%2C_Dig%21%21%21_coverart.JPG")
    add_release("Push The Sky Away", "2013-02-18",1, "https://upload.wikimedia.org/wikipedia/en/f/f3/Push_the_Sky_Away.jpg")
    add_release("Skeleton Tree", "2016-09-09",1, "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Nick_Cave_and_The_Bad_Seeds_-_Skeleton_Tree.jpg/440px-Nick_Cave_and_The_Bad_Seeds_-_Skeleton_Tree.jpg")
    add_release("Ghosteen", "2019-10-04",1, "https://upload.wikimedia.org/wikipedia/en/4/45/Ghosteen_-_Nick_Cave_and_the_Bad_Seeds.jpg")
    add_release("Wild God", "2024-08-30",1, "https://upload.wikimedia.org/wikipedia/en/7/7f/Nick_Cave_and_the_Bad_Seeds_-_Wild_God.png")

    add_release("Kollaps", "1981-10-05", 2, "https://www.fromthearchives.org/en/ENKollaps_LP_f.jpg")
    add_release("Zeichnungen des Patienten O. T.", "1983-11-21", 2, "https://www.fromthearchives.org/en/ENZeichnungen_LP_f.jpg")   
    add_release("80-83 Strategies Against Architecture", "1984-01-23", 2, "https://www.fromthearchives.org/en/ENStrat1CD_f.jpg")

    add_release("Vengeance", "1984-04-04", 3, "https://upload.wikimedia.org/wikipedia/en/9/91/NMA_vengeance.jpg")
    add_release("No Rest for the Wicked", "1985-01-01", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/9/92/NMA_no_rest.jpg/220px-NMA_no_rest.jpg")
    add_release("The Ghost of Cain", "1986-09-01", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/TheGhostofCain.jpg/220px-TheGhostofCain.jpg")
    add_release("Thunder and Consolation", "1989-03-15", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/ThunderConsolation.jpg/220px-ThunderConsolation.jpg")
    add_release("Impurity", "1990-09-01", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/8/86/NMA_impurity.jpg/220px-NMA_impurity.jpg")
    add_release("The Love of Hopeless Causes", "1993-03-29", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/NMA_hopeless_causes.jpg/220px-NMA_hopeless_causes.jpg")
    add_release("Strange Brotherhood", "1998-04-13", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/0/02/NMA_strange_brotherhood.jpg/220px-NMA_strange_brotherhood.jpg")    
    add_release("Eight", "2000-01-31", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/NMA_eight.jpg/220px-NMA_eight.jpg")
    add_release("Carnival", "2005-09-06", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/NMA_carnival.jpg/220px-NMA_carnival.jpg")
    add_release("High", "2007-08-20", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/High_%28New_Model_Army_album_-_cover_art%29.jpg/220px-High_%28New_Model_Army_album_-_cover_art%29.jpg")
    add_release("Today Is a Good Day", "2009-09-14", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Today_Is_a_Good_Day.jpg/220px-Today_Is_a_Good_Day.jpg")
    add_release("Between Dog and Wolf", "2013-09-30", 3, "https://upload.wikimedia.org/wikipedia/en/5/55/New_Model_Army_Between_Dog_and_Wolf_album_cover.jpg")
    add_release("Between Wine and Blood", "2014-09-05", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Between_Wine_and_Blood.jpg/220px-Between_Wine_and_Blood.jpg")    
    add_release("Winter", "2016-08-26", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/NewModelArmy_Winter.png/220px-NewModelArmy_Winter.png")  
    add_release("From Here", "2019-08-23", 3, "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/New_Model_Army_-_From_Here.jpg/220px-New_Model_Army_-_From_Here.jpg")
    add_release("Unbroken", "2024-01-26", 3, "https://m.media-amazon.com/images/I/B1f6d+CLoRL._SY240_.jpg")

    add_release("Fire of Love", "1981-08-31", 4, "https://i.discogs.com/zi2M6hCVwJp5oBImwZ1JaaEhoydNVsGVEnbXFYhpbDU/rs:fit/g:sm/q:40/h:150/w:150/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTUxODMy/MS0xMjU0NTEyODM1/LmpwZWc.jpeg")  
    add_release("Miami", "1982-08-01", 4, "https://i.discogs.com/AdDtH0Iy8gRPm5qUq9uo4KayDSNE9rTFZ8HB4TMmodU/rs:fit/g:sm/q:40/h:150/w:150/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTUwMDg2/NDktMTM4MjAwOTg4/Ni0zMzEyLmpwZWc.jpeg")
    add_release("The Las Vegas Story", "1984-08-01", 4, "https://i.discogs.com/-8mewuH1G6SrYUE4TrWmoHt9GTdKCdichxGwo_OPD6g/rs:fit/g:sm/q:40/h:150/w:150/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTgxOTE5/NS0xMzg4MjUxMTg5/LTE3MzEuanBlZw.jpeg")
    add_release("Mother Juno", "1987-08-01", 4, "https://i.discogs.com/rZkNA9XVlEtwRv7mCievMHcVsVATI6F3CIYCnscfJAA/rs:fit/g:sm/q:40/h:150/w:150/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTUxNzY5/NS0xMjY5ODgwMjAw/LmpwZWc.jpeg")
    add_release("Pastoral Hide and Seek", "1990-08-01", 4, "https://i.discogs.com/GQcnQXdy_oxxSSo3AS4sI94VGPMABf0iH1rf0jPdWEM/rs:fit/g:sm/q:40/h:150/w:150/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTEwNzk0/NzItMTE5MDU5OTMz/Ni5qcGVn.jpeg")  
    add_release("Divinity", "1991-08-01", 4, "https://i.discogs.com/wNBNv0NsqyBax20H_JeAqkc2OPBKl6oC77hK2CYscYs/rs:fit/g:sm/q:40/h:150/w:150/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE0MzMz/MDctMTM1MjA1NTE3/My0xNDA3LmpwZWc.jpeg")  
    add_release("Lucky Jim", "1993-08-01", 4, "https://i.discogs.com/gySQUvUPveSBBj3y7ZPKRAlDEdOYkW-Fk2m6rzSKmOs/rs:fit/g:sm/q:40/h:150/w:150/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTg2MDQz/MS0xMTY2MzUxNTcz/LmpwZWc.jpeg")

    add_list("Top 1988", "Mon top album 1988", True)

    add_list_release(4, 1, 5)



