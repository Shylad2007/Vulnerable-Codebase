query = "SELECT * FROM users WHERE username = %s"
cursor.execute(query, (search_query,))
results = cursor.fetchall()