## Transaction per HTTP request 
Each view call is wrapped in a transaction if we enable this setting

``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'test.db'),
        'ATOMIC_REQUEST': True,
    }
}
```

This is the same as to wrap each view with @transaction.atomic


## Savepoints
Django savepoints allow to save partial changes within transaciton