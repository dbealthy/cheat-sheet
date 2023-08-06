

### Pull needed images
``` bash
docker pull mariadb
```

``` bash
docker pull phpmyadmin/phpmyadmin
```



### Create db network
```bash
docker network create localdb-network
```

### Create mariadb container
``` bash
docker run -d \
	--name mariadb-server \
	--network localdb-network \
	--restart unless-stopped \
	-v /var/lib/mysql:/var/lib/mysql \
	-e "MYSQL_ROOT_PASSWORD=z}P5rO5TzrmMaPu9" \
	-p 3306:3306 \
	mariadb
```


### Create phpmyadmin container
```bash
docker run -d \
    --name phpmyadmin \
    --network localdb-network \
    --link mariadb-server \
    --restart unless-stopped \
    -e PMA_HOST=mariadb-server \
    -e UPLOAD_LIMIT=1G \
    -p 8080:80 \
    phpmyadmin/phpmyadmin
```