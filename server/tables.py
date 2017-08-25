import sqlite3

class Tables:

    # store the URL if it does not exist
    # return the
    def storeURL(self, url):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        insertURLQuery = "IF NOT EXISTS(SELECT 1 FROM links WHERE full_url=?) INSERT INTO links (full_url) VALUES (?)"
        cursor.execute(insertURLQuery, (url,))
        connection.commit()
        getIDQuery = "SELECT id from links where id=?"
        cursor.executemany(getIDQuery, (url,url))
        data = cursor.fetchone()
        connection.commit()
        connection.close()
        return data[0]

    # update the row containing a url with the hash_value
    # return hash_value
    def updateWithHash(self,hash_value, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        updateHashQuery = "UPDATE links SET hash=? where url=?"
        cursor.execute(insertURLQuery, (hash_value,_id))
        connection.commit()
        connection.close()
