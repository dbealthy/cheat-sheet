Connect to shell
``` bash
psql -Umyname
```


List all databases
```
\l
```

Change selected database
```
\c dbname
```

Show all tables

``` sql
\dt
```


## Debug
Reset current sequence counter if there is a duplicate key error
``` bash
python manage.py sqlsequencereset auth | python manage.py dbshell
```

OR in psql
``` sql
SELECT MAX(id)+1 FROM auth_permission;
```

``` sql
ALTER SEQUENCE auth_permission_id_seq RESTART WITH <result of previous cmd>;
```


"acp.msb_create_subsidized_application",