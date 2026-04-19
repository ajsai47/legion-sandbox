def find_user(db, username):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    return cursor.fetchone()
