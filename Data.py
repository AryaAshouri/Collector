import sqlite3, requests, datetime
from datetime import datetime

def save(message ,pollution, temperature):
    now = datetime.now()
    connection = sqlite3.connect("Database/Data.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Information(
    	Username TEXT, 
    	User_Tag int, 
    	User_ID int, 
    	Content TEXT, 
    	"Date" TEXT, 
    	"Time" TEXT,
    	Pollution INT,
    	Temperature INT)
    	''')

    cursor.execute('''INSERT INTO Information(
    	Username,
    	User_Tag,
    	User_ID,
    	Content,
    	"Date",
    	"Time",
    	Pollution,
    	Temperature)
    	
    	VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (
    		message.author.name,
    		"#"+message.author.discriminator,
    		message.author.id,
    		message.content,
    		now.strftime("%Y:%m:%d"),
    		now.strftime("%H:%M:%S"),
    		pollution, temperature))

    connection.commit()
    connection.close()