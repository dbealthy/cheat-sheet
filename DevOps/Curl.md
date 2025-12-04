 
 - Get status code and headers of response
 
``` bash
curl -I -X 'GET' '{{URI}}' -H '{{HEADERS}}'
``` 

- Prettify json
``` bash
curl -X 'GET' '{{URI}}' -H '{{HEADERS}}' | python -mjson.tool
```