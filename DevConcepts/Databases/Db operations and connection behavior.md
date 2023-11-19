Using marriadb, pymysql library and innodb engine

Configure connection with autocommit=False
``` Python
connect = pymysql.connect(host="94.247.131.123", user="bogatov", password="qSWNjA1vu35fJhZR", db="globals_db", autocommit=False)
```
- Inserting data in a table
``` SQL
INSERT INTO tag (name, user_id) VALUES ('Казахстан', 1234)
```

- Selecting data using the same connection and the same cursor or different cursors, returns inserted data, even though it is not commited yet.
``` SQL
SELECT * FROM tag
```

- Creating a new connection and selecting all data from that table, returns nothing, after some time waiting. 
``` SQL
SELECT * FROM tag
```

  
  > This means that not commited transaction is visible to its own connection only and all its cursors. 

- Inserting data in a new connection adds a new record that is only visible it itself and increments the value of id value that is auto increment.

> This means that each insert, even if it is not commited yet, increases autoincrement counter in any way. This prevents record collisions when they are finally commited, or if these recoreds are not commited, they just won't appear in that table.
  

